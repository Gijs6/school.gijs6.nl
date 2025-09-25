import os
import shutil
import re
import subprocess
import time
import threading
import tempfile

import argparse

from datetime import datetime, timezone

from http.server import HTTPServer, SimpleHTTPRequestHandler

import yaml
import json

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown

from feedgen.feed import FeedGenerator

from colorama import Fore, Style, init


init()


def sort_years(yearstr):
    match = re.match(r"(\d)(VWO)", yearstr)
    return -int(match.group(1)) if match else float("inf")


def sort_period(period):
    match = re.match(r"([A-Z]+)(\d+)", period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)


def build_archive_data():
    archive_data = {}
    site_dir = "site"
    vwo_years = sorted(
        [d for d in os.listdir(site_dir) if re.match(r"[0-3]VWO", d)],
        key=lambda x: int(x[0]),
        reverse=True,
    )

    for year in vwo_years:
        year_pages = []
        year_path = os.path.join(site_dir, year)
        if os.path.isdir(year_path):
            for root, _, files in os.walk(year_path):
                for file in files:
                    if file.endswith(".md"):
                        path_parts = root.split("/") + [file]
                        link = f"/{'/'.join(path_parts[-2:]).replace('.md', '.html')}"
                        title = (
                            file.replace(".md", "").replace("_", " ").replace("-", ": ")
                        )
                        year_pages.append({"link": link, "title": title})
        archive_data[year] = year_pages

    return archive_data


def build_homepage_data():
    site_dir = "site"
    with open(
        os.path.join(site_dir, "data/test_data.json"), "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    file_cache = {}
    for main_dir in [d for d in os.listdir(site_dir) if re.match(r"\dVWO", d)]:
        main_path = os.path.join(site_dir, main_dir)
        if not os.path.isdir(main_path):
            continue
        for sub_dir in [
            d
            for d in os.listdir(main_path)
            if os.path.isdir(os.path.join(main_path, d))
        ]:
            sub_path = os.path.join(main_path, sub_dir)
            for file in [f for f in os.listdir(sub_path) if f.endswith(".md")]:
                file_path = os.path.join(sub_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                front_matter = {}
                test_code = []
                summary_name = "Samenvatting"
                summary_type = "basic"

                match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
                if match:
                    front_matter = yaml.safe_load(match.group(1))
                    test_code = front_matter.get("test_code", [])
                    if isinstance(test_code, str):
                        test_code = [test_code]
                    summary_name = front_matter.get("summary_name", "Samenvatting")
                    summary_type = front_matter.get("summary_type", "basic")

                file_cache[file_path] = (test_code, summary_name, summary_type)

                for test_data in filter(
                    lambda t: t["test_code"] in test_code, data[main_dir][sub_dir]
                ):
                    if summary_type != "basic":
                        if not any(
                            summary_name in r["title"] for r in test_data["resources"]
                        ):
                            test_data["resources"].append(
                                {
                                    "link": f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}",
                                    "title": summary_name,
                                    "type": "internal",
                                }
                            )
                        test_data["resources"].sort(key=lambda r: r["title"])
                    else:
                        test_data["summary_link"] = (
                            f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}"
                        )
                        test_data["summary_name"] = summary_name
                    if not test_data.get("summary_link") and "summary" in summary_type:
                        test_data["summary_made"] = True

    sorted_data = {}
    for year in sorted(data.keys(), key=sort_years):
        year_data = {}
        for period in sorted(data[year].keys(), key=sort_period, reverse=True):
            if any(
                test.get("summary_link") or test.get("resources")
                for test in data[year][period]
            ):
                year_data[period] = sorted(
                    [
                        test
                        for test in data[year][period]
                        if test.get("make_summary") or test.get("resources")
                    ],
                    key=lambda t: t["subject"],
                )
        if year_data:
            sorted_data[year] = year_data

    return sorted_data


def copy_static_assets(build_dir):
    assets_src = "site/assets"
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, os.path.join(build_dir, "assets"))

    wellknown_src = "site/.well-known"
    if os.path.exists(wellknown_src):
        shutil.copytree(wellknown_src, os.path.join(build_dir, ".well-known"))

    robots_src = "site/robots.txt"
    if os.path.exists(robots_src):
        shutil.copy2(robots_src, os.path.join(build_dir, "robots.txt"))

    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            build_year_dir = os.path.join(build_dir, year_dir)
            for root, _, files in os.walk(year_path):
                for file in files:
                    if not file.endswith(".md"):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(
                            build_year_dir, os.path.relpath(src_file, year_path)
                        )
                        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                        shutil.copy2(src_file, dest_file)

    if os.path.exists("CNAME"):
        shutil.copy2("CNAME", os.path.join(build_dir, "CNAME"))


def get_git_dates(filepath):
    try:
        output = subprocess.check_output(
            ["git", "log", "--follow", "--format=%H %ct", "--", filepath],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()

        if not output:
            raise ValueError("No git history found for the file.")

        lines = output.split("\n")
        first_commit_ts = int(lines[-1].split()[1])
        last_commit_ts = int(lines[0].split()[1])

        return datetime.fromtimestamp(
            first_commit_ts, tz=timezone.utc
        ), datetime.fromtimestamp(last_commit_ts, tz=timezone.utc)

    except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
        return datetime.now(timezone.utc), datetime.now(timezone.utc)


def generate_feeds(build_dir, homepage_data, md_cache):
    fg = FeedGenerator()
    fg.title("Leermiddelenoverzicht")
    fg.description("Een verzameling van samenvattingen en leermiddelen")
    fg.id("https://school.gijs6.nl")
    fg.link(href="https://school.gijs6.nl", rel="alternate")
    fg.language("nl")
    fg.author(name="Gijs ten Berg", email="gijs6@dupunkto.org")
    fg.generator("Binder")

    for year, year_data in homepage_data.items():
        for period, tests in year_data.items():
            for test in tests:
                entries = (
                    [
                        {
                            "link": test.get("summary_link"),
                            "title": f"{test['subject']} - {test['test_material']}",
                        }
                    ]
                    if test.get("summary_link")
                    else []
                )
                entries.extend(
                    [
                        {
                            "link": r["link"],
                            "title": f"{r['title']} - {test['subject']}",
                            "internal": r.get("type") == "internal",
                        }
                        for r in test.get("resources", [])
                    ]
                )
                for entry in entries:
                    if not entry["link"]:
                        continue
                    html_content = md_cache.get(entry["link"], entry["title"])
                    fe = fg.add_entry()
                    fe.title(entry["title"] + f" ({year} {period})")
                    fe.link(href=f"https://school.gijs6.nl{entry['link']}")
                    fe.id(f"https://school.gijs6.nl{entry['link']}")
                    fe.description(html_content)
                    md_file_path = os.path.join(
                        "site", entry["link"].lstrip("/") + ".md"
                    )
                    if md_file_path:
                        first_commit, last_commit = get_git_dates(md_file_path)
                        fe.pubDate(first_commit)
                        fe.updated(last_commit)

    with open(os.path.join(build_dir, "rss.xml"), "wb") as f:
        f.write(fg.rss_str(pretty=True))
    with open(os.path.join(build_dir, "atom.xml"), "wb") as f:
        f.write(fg.atom_str(pretty=True))


def remove_base64_images(html_content):
    return re.sub(r'<img[^>]*src="data:image/[^"]*"[^>]*>', "", html_content)


def setup_markdown_processor():
    return Markdown(
        extensions=["meta", "codehilite", "tables", "toc"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False}
        },
    )


def process_markdown_files(build_dir, template_env, md_processor):
    homepage_data = build_homepage_data()
    archive_data = build_archive_data()

    md_cache = {}

    # index.html
    with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            template_env.get_template("home.html").render(
                homepage_data=homepage_data,
                archive_data=archive_data,
                site={"data": {"homepage_data": homepage_data}},
                page_path="site/templates/home.html",
            )
        )

    # 404.html
    with open(os.path.join(build_dir, "404.html"), "w", encoding="utf-8") as f:
        f.write(template_env.get_template("404.html").render())

    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if not os.path.isdir(year_path):
            continue
        build_year_dir = os.path.join(build_dir, year_dir)
        os.makedirs(build_year_dir, exist_ok=True)

        for root, _, files in os.walk(year_path):
            for file in files:
                if not file.endswith(".md"):
                    continue
                md_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_file_path, year_path)
                build_path = os.path.join(
                    build_year_dir, os.path.splitext(relative_path)[0] + ".html"
                )
                os.makedirs(os.path.dirname(build_path), exist_ok=True)
                with open(md_file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                if content.startswith("---"):
                    _, front_matter_str, markdown_content = content.split("---", 2)
                    front_matter = yaml.safe_load(front_matter_str)
                else:
                    front_matter = {}
                    markdown_content = content

                html_content = remove_base64_images(
                    md_processor.convert(markdown_content.strip())
                )
                md_processor.reset()  # reset processor to reuse

                md_cache[f"/{year_dir}/{os.path.splitext(relative_path)[0]}"] = (
                    html_content
                )

                if front_matter.get("layout") == "summary":
                    rendered = template_env.get_template("summary.html").render(
                        content=html_content,
                        page=front_matter,
                        page_path=md_file_path,
                    )
                else:
                    rendered = f"<html><body>{html_content}</body></html>"

                with open(build_path, "w", encoding="utf-8") as f:
                    f.write(rendered)

    # Return md_cache for feed generation
    return homepage_data, md_cache


class BuildHandler(FileSystemEventHandler):
    def __init__(self, build_func):
        self.build_func = build_func
        self.last_build = 0

    def on_modified(self, event):
        if event.is_directory or "build/" in event.src_path:
            return
        now = time.time()
        if now - self.last_build < 1:
            return
        self.last_build = now
        print(
            f"\n{Fore.YELLOW}Restarting! {Style.BRIGHT}{os.path.basename(event.src_path)} changed.{Style.RESET_ALL}\n"
        )
        self.build_func()


class BuildHTTPServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="build", **kwargs)


def build():
    print(f"{Fore.CYAN}=> Binder is binding <={Style.RESET_ALL}")

    # Step 1: Setup build directory
    print("=> Setup ...")
    temp_build_dir = tempfile.mkdtemp()
    print(f"{Fore.GREEN}=> Setup done{Style.RESET_ALL}")

    # Step 2: Templates
    print("=> Templates ...")
    template_env = Environment(loader=FileSystemLoader("site/templates"))
    print(f"{Fore.GREEN}=> Templates done{Style.RESET_ALL}")

    # Step 3: Markdown processor
    print("=> Markdown ...")
    md_processor = setup_markdown_processor()
    print(f"{Fore.GREEN}=> Markdown done{Style.RESET_ALL}")

    # Step 4: Copy static assets
    print("=> Assets ...")
    copy_static_assets(temp_build_dir)
    print(f"{Fore.GREEN}=> Assets done{Style.RESET_ALL}")

    # Step 5: Process markdown files
    print("=> Pages ...")
    homepage_data, md_cache = process_markdown_files(
        temp_build_dir, template_env, md_processor
    )
    print(f"{Fore.GREEN}=> Pages done{Style.RESET_ALL}")

    # Step 6: Generate feeds
    print("=> Feeds ...")
    generate_feeds(temp_build_dir, homepage_data, md_cache)
    print(f"{Fore.GREEN}=> Feeds done{Style.RESET_ALL}")

    # Step 7: Output to build
    print("=> Output ...")
    final_build_dir = "build"
    if os.path.exists(final_build_dir):
        shutil.rmtree(final_build_dir)
    shutil.move(temp_build_dir, final_build_dir)
    print(f"{Fore.GREEN}=> Output donne{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Build complete!{Style.RESET_ALL}\n")


def serve(port=8000):
    print(f"{Fore.BLUE}Development server{Style.RESET_ALL}\n")
    build()
    observer = Observer()
    observer.schedule(BuildHandler(build), "site", recursive=True)
    observer.start()
    server = HTTPServer(("localhost", port), BuildHTTPServer)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print(
        f"{Fore.GREEN}Serving on {Style.BRIGHT}http://localhost:{port}{Style.RESET_ALL}"
    )
    print(f"{Fore.MAGENTA}Watching for changes...{Style.RESET_ALL}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Stopping server...{Style.RESET_ALL}")
        observer.stop()
        server.shutdown()
        observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binder - Generator for summary site")
    parser.add_argument(
        "command",
        nargs="?",
        default="build",
        choices=["build", "serve"],
        help="Command to run (default: build)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for development server (default: 8000)",
    )

    args = parser.parse_args()

    if args.command == "serve":
        serve(args.port)
    else:
        build()
