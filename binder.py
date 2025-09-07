import os
import shutil
import re
import yaml
import json
import time
import threading
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone
from tqdm import tqdm
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
    vwo_pages = []
    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            for root, dirs, files in os.walk(year_path):
                vwo_pages.append((root, dirs, files))

    # Process all VWO years dynamically
    archive_data = {}
    vwo_years = sorted(
        [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)],
        key=lambda x: int(x[0]),
        reverse=True,
    )

    for year in vwo_years:
        year_pages = []
        for root, dirs, files in vwo_pages:
            if year in root:
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
    with open("site/data/test_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    site_dir = "site"
    main_dirs = [d for d in os.listdir(site_dir) if re.match(r"\dVWO", d)]

    for main_dir in main_dirs:
        main_path = os.path.join(site_dir, main_dir)
        sub_dirs = [
            d
            for d in os.listdir(main_path)
            if os.path.isdir(os.path.join(main_path, d))
        ]
        for sub_dir in sub_dirs:
            sub_path = os.path.join(main_path, sub_dir)
            files = [f for f in os.listdir(sub_path) if f.endswith(".md")]
            for file in files:
                file_path = os.path.join(sub_path, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
                if match:
                    front_matter = yaml.safe_load(match.group(1))

                    test_code = front_matter.get("test_code", [])
                    if isinstance(test_code, str):
                        test_code = [test_code]

                    summary_name = front_matter.get("summary_name", "Samenvatting")
                    summary_type = front_matter.get("summary_type", "basic")

                else:
                    front_matter = []
                    test_code = []
                    summary_name = "Samenvatting"
                    summary_type = "basic"

                for test_data in filter(
                    lambda t: t["test_code"] in test_code, data[main_dir][sub_dir]
                ):
                    if summary_type != "basic":
                        if not any(
                            summary_name in resource["title"]
                            for resource in test_data["resources"]
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
            if [
                "Ouioui"
                for test in data[year][period]
                if test.get("summary_link") or test.get("resources")
            ]:
                tests_to_include = [
                    test
                    for test in data[year][period]
                    if test.get("make_summary") or test.get("resources")
                ]
                year_data[period] = sorted(
                    tests_to_include, key=lambda subjectdata: subjectdata["subject"]
                )

        if year_data:
            sorted_data[year] = year_data

    return sorted_data


def setup_build_directory():
    build_dir = "build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    return build_dir


def copy_static_assets(build_dir):
    assets_src = "site/assets"
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, os.path.join(build_dir, "assets"))

    # Copy .well-known directory
    wellknown_src = "site/.well-known"
    if os.path.exists(wellknown_src):
        shutil.copytree(wellknown_src, os.path.join(build_dir, ".well-known"))

    # Copy robots.txt from site directory
    robots_src = "site/robots.txt"
    if os.path.exists(robots_src):
        shutil.copy2(robots_src, os.path.join(build_dir, "robots.txt"))

    # Copy images from year directories
    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            build_year_dir = os.path.join(build_dir, year_dir)
            for root, dirs, files in os.walk(year_path):
                for file in files:
                    if not file.endswith(".md"):  # Copy all non-markdown files
                        src_file = os.path.join(root, file)
                        rel_path = os.path.relpath(src_file, year_path)
                        dest_file = os.path.join(build_year_dir, rel_path)

                        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                        shutil.copy2(src_file, dest_file)

    # Copy CNAME from root if it exists
    if os.path.exists("CNAME"):
        shutil.copy2("CNAME", os.path.join(build_dir, "CNAME"))


def generate_feeds(build_dir, homepage_data, md_processor):
    fg = FeedGenerator()
    fg.title("Leermiddelenoverzicht")
    fg.description("Een verzameling van samenvattingen en leermiddelen")
    fg.id("https://school.gijs6.nl")
    fg.link(href="https://school.gijs6.nl", rel="alternate")
    fg.link(href="https://school.gijs6.nl/rss.xml", rel="self")
    fg.language("nl")
    fg.author(name="Gijs ten Berg", email="gijs6@dupunkto.org")
    fg.generator("Binder")

    for year, year_data in homepage_data.items():
        for period, tests in year_data.items():
            for test in tests:
                if test.get("summary_link"):
                    md_file_path = os.path.join(
                        "site", test["summary_link"].lstrip("/") + ".md"
                    )
                    if os.path.exists(md_file_path):
                        with open(md_file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        if content.startswith("---"):
                            _, front_matter_str, markdown_content = content.split(
                                "---", 2
                            )
                        else:
                            markdown_content = content

                        html_content = md_processor.convert(markdown_content.strip())
                        html_content = remove_base64_images(html_content)
                    else:
                        html_content = f"Samenvatting voor {test['subject']} - {test['test_material']}"

                    fe = fg.add_entry()
                    fe.title(
                        f"{test['subject']} - {test['test_material']} ({year} {period})"
                    )
                    fe.link(href=f"https://school.gijs6.nl{test['summary_link']}")
                    fe.id(f"https://school.gijs6.nl{test['summary_link']}")
                    fe.description(html_content)
                    fe.pubDate(datetime.now(timezone.utc))

                for resource in test.get("resources", []):
                    if resource.get("type") == "internal":
                        md_file_path = os.path.join(
                            "site", resource["link"].lstrip("/") + ".md"
                        )
                        if os.path.exists(md_file_path):
                            with open(md_file_path, "r", encoding="utf-8") as f:
                                content = f.read()

                            if content.startswith("---"):
                                _, front_matter_str, markdown_content = content.split(
                                    "---", 2
                                )
                            else:
                                markdown_content = content

                            html_content = md_processor.convert(
                                markdown_content.strip()
                            )
                            html_content = remove_base64_images(html_content)
                        else:
                            html_content = f"{resource['title']} voor {test['subject']} - {test['test_material']}"

                        fe = fg.add_entry()
                        fe.title(
                            f"{resource['title']} - {test['subject']} ({year} {period})"
                        )
                        fe.link(href=f"https://school.gijs6.nl{resource['link']}")
                        fe.id(f"https://school.gijs6.nl{resource['link']}")
                        fe.description(html_content)
                        fe.pubDate(datetime.now(timezone.utc))

    fg.rss_str(pretty=True)
    fg.rss_file(os.path.join(build_dir, "rss.xml"))

    fg.atom_str(pretty=True)
    fg.atom_file(os.path.join(build_dir, "atom.xml"))


def remove_base64_images(html_content):
    img_pattern = r'<img[^>]*src="data:image/[^"]*"[^>]*>'
    return re.sub(img_pattern, "", html_content)


def setup_markdown_processor():
    return Markdown(
        extensions=["meta", "codehilite", "tables", "toc"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False}
        },
    )


def process_markdown_files(build_dir, template_env, md_processor):
    # Always generate index.html from home template
    homepage_data = build_homepage_data()
    archive_data = build_archive_data()

    template = template_env.get_template("home.html")
    rendered = template.render(
        homepage_data=homepage_data,
        archive_data=archive_data,
        site={
            "data": {"homepage_data": homepage_data},
        },
        page_path="site/templates/home.html",
    )

    with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(rendered)

    # Process 404 page
    template = template_env.get_template("404.html")
    rendered = template.render()

    with open(os.path.join(build_dir, "404.html"), "w", encoding="utf-8") as f:
        f.write(rendered)

    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            build_year_dir = os.path.join(build_dir, year_dir)
            os.makedirs(build_year_dir, exist_ok=True)

            for root, dirs, files in os.walk(year_path):
                for file in files:
                    if file.endswith(".md"):
                        md_file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(md_file_path, year_path)
                        build_path = os.path.join(
                            build_year_dir, os.path.splitext(relative_path)[0] + ".html"
                        )

                        os.makedirs(os.path.dirname(build_path), exist_ok=True)

                        with open(md_file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        if content.startswith("---"):
                            _, front_matter_str, markdown_content = content.split(
                                "---", 2
                            )
                            front_matter = yaml.safe_load(front_matter_str)
                        else:
                            front_matter = {}
                            markdown_content = content

                        html_content = md_processor.convert(markdown_content.strip())
                        html_content = remove_base64_images(html_content)

                        if front_matter.get("layout") == "summary":
                            template = template_env.get_template("summary.html")
                            page_path = os.path.relpath(md_file_path, "site")
                            rendered = template.render(
                                content=html_content,
                                page=front_matter,
                                page_path=page_path,
                            )
                        else:
                            rendered = f"<html><body>{html_content}</body></html>"

                        with open(build_path, "w", encoding="utf-8") as f:
                            f.write(rendered)


class BuildHandler(FileSystemEventHandler):
    def __init__(self, build_func):
        self.build_func = build_func
        self.last_build = 0

    def on_modified(self, event):
        if event.is_directory:
            return

        # Ignore build directory changes
        if "build/" in event.src_path:
            return

        # Debounce builds (max once per second)
        now = time.time()
        if now - self.last_build < 1:
            return

        self.last_build = now
        filename = os.path.basename(event.src_path)
        print(
            f"\n{Fore.YELLOW}Restarting! {Style.BRIGHT}{filename} has changed.{Style.RESET_ALL}\n"
        )
        self.build_func()


class BuildHTTPServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="build", **kwargs)


def build():
    print(f"{Fore.CYAN}=> Binder is binding <={Style.RESET_ALL}")

    tasks = [
        ("Setup", setup_build_directory),
        ("Templates", lambda: Environment(loader=FileSystemLoader("site/templates"))),
        ("Markdown", setup_markdown_processor),
        ("Data", build_homepage_data),
        ("Assets", lambda: copy_static_assets("build")),
        (
            "Pages",
            lambda: process_markdown_files(
                "build",
                Environment(loader=FileSystemLoader("site/templates")),
                setup_markdown_processor(),
            ),
        ),
        (
            "Feeds",
            lambda: generate_feeds(
                "build", build_homepage_data(), setup_markdown_processor()
            ),
        ),
    ]

    results = {}

    with tqdm(
        total=len(tasks),
        desc="Building",
        bar_format="{desc}[{bar:60}] {percentage:3.0f}%",
        ascii="-#",
    ) as pbar:
        for desc, task in tasks:
            pbar.set_description(desc)
            if desc == "Setup":
                results["build_dir"] = task()
            elif desc == "Templates":
                results["template_env"] = task()
            elif desc == "Markdown":
                results["md_processor"] = task()
            elif desc == "Data":
                results["homepage_data"] = task()
            elif desc == "Assets":
                copy_static_assets(results["build_dir"])
            elif desc == "Pages":
                process_markdown_files(
                    results["build_dir"],
                    results["template_env"],
                    results["md_processor"],
                )
            elif desc == "Feeds":
                generate_feeds(
                    results["build_dir"],
                    results["homepage_data"],
                    results["md_processor"],
                )
            pbar.update(1)

    print(f"{Fore.GREEN}Build complete!{Style.RESET_ALL}\n")


def serve(port=8000):
    print(f"{Fore.BLUE}Development server{Style.RESET_ALL}\n")

    # Initial build
    build()

    # Set up file watcher
    event_handler = BuildHandler(build)
    observer = Observer()
    observer.schedule(event_handler, "site", recursive=True)
    observer.start()

    # Start HTTP server in a separate thread
    server = HTTPServer(("localhost", port), BuildHTTPServer)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

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
