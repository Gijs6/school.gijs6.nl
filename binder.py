import os
import sys
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
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

from feedgen.feed import FeedGenerator

from colorama import Fore, Style, init


init()


# CONSTANTS


# Directory paths
SITE_DIR = "site"
BUILD_DIR = "build"
TEMPLATES_DIR = "site/templates"
DATA_DIR = "site/data"

# File paths
RESOURCES_JSON = "site/data/resources.json"

# Web configuration
SITE_URL = "https://school.gijs6.nl"
SITE_TITLE = "Leermiddelenoverzicht"
SITE_DESCRIPTION = "Een verzameling van samenvattingen en leermiddelen"
AUTHOR_NAME = "Gijs ten Berg"
AUTHOR_EMAIL = "gijs6@dupunkto.org"

# Regex patterns
VWO_YEAR_PATTERN = re.compile(r"(\d)VWO")
ARCHIVE_YEAR_PATTERN = re.compile(r"[23]VWO")
PERIOD_PATTERN = re.compile(r"([A-Z]+)(\d+)")
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Subject icon mapping
SUBJECT_ICONS = {
    "BIOL": "fa-solid fa-seedling",
    "ENTL": "ENTL",
    "FATL": "FATL",
    "NETL": "NETL",
    "NAT": "fa-solid fa-atom",
    "SCHK": "fa-solid fa-flask-vial",
    "WISB": "fa-solid fa-calculator",
    "MAAT": "fa-solid fa-people-group",
    "NLT": "fa-solid fa-microscope",
}

SUBJECT_NAMES = {
    "BIOL": "Biologie",
    "ENTL": "Engels",
    "FATL": "Frans",
    "NETL": "Nederlands",
    "NAT": "Natuurkunde",
    "SCHK": "Scheikunde",
    "WISB": "Wiskunde B",
    "MAAT": "Maatschappijleer",
    "NLT": "NLT",
}


# HELPER FUNCTIONS


def parse_front_matter(content):
    match = FRONT_MATTER_PATTERN.match(content)
    if match:
        return yaml.safe_load(match.group(1)) or {}, content.split("---", 2)[2].strip()
    return {}, content


def get_md_file_path(link):
    if not link.startswith("/"):
        return None

    candidate = os.path.join(SITE_DIR, link.lstrip("/") + ".md")
    return candidate if os.path.isfile(candidate) else None


def sort_years(yearstr):
    match = VWO_YEAR_PATTERN.match(yearstr)
    return -int(match.group(1)) if match else float("inf")


def sort_period(period):
    match = PERIOD_PATTERN.match(period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)


def get_vwo_years():
    vwo_dirs = [d for d in os.listdir(SITE_DIR) if VWO_YEAR_PATTERN.match(d)]
    return sorted(vwo_dirs, key=lambda x: int(x[0]), reverse=True)


def build_archive_data():
    archive_data = {}

    for year in get_vwo_years():
        # Only process archive years (2VWO, 3VWO)
        if not ARCHIVE_YEAR_PATTERN.match(year):
            continue

        year_pages = []
        year_path = os.path.join(SITE_DIR, year)

        if not os.path.isdir(year_path):
            continue

        for root, _, files in os.walk(year_path):
            md_files = [f for f in files if f.endswith(".md")]

            for file in md_files:
                path_parts = root.split("/") + [file]
                link = f"/{'/'.join(path_parts[-2:]).replace('.md', '')}"
                title = file.replace(".md", "").replace("_", " ").replace("-", ": ")
                year_pages.append({"link": link, "title": title})

        archive_data[year] = sorted(year_pages, key=lambda p: p["title"])

    return archive_data


def load_json_file(filepath):
    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_test_material(front_matter):
    short = front_matter.get("short", "")
    title = front_matter.get("title", "")
    description = front_matter.get("description", "")

    parts = []
    if title:
        parts.append(title)
    if description:
        parts.append(f"({description})")

    return " ".join(parts) if parts else short


def create_test_entry(front_matter, main_dir, sub_dir, file, resources_map):
    subject = front_matter.get("subject", "").upper()

    entry = {
        "subject": subject,
        "test_material": build_test_material(front_matter),
        "icon": SUBJECT_ICONS.get(subject, "fa-solid fa-file-lines"),
        "resources": resources_map.get(f"{main_dir}/{sub_dir}/{file}", []),
        "summary_link": f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}",
    }

    return entry


def process_modern_year(year_dir, resources_map, dev=False):
    year_data = {}
    year_path = os.path.join(SITE_DIR, year_dir)

    subdirs = [
        d for d in os.listdir(year_path) if os.path.isdir(os.path.join(year_path, d))
    ]

    for sub_dir in subdirs:
        sub_path = os.path.join(year_path, sub_dir)
        md_files = [f for f in os.listdir(sub_path) if f.endswith(".md")]

        for file in md_files:
            file_path = os.path.join(sub_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            front_matter, _ = parse_front_matter(content)

            # Skip if no subject
            if not front_matter.get("subject"):
                continue

            # Skip if hidden (unless in dev mode)
            if not dev and front_matter.get("hidden"):
                continue

            entry = create_test_entry(
                front_matter, year_dir, sub_dir, file, resources_map
            )
            year_data.setdefault(sub_dir, []).append(entry)

    return year_data


def build_homepage_data(dev=False):
    resources_map = load_json_file(RESOURCES_JSON)
    data = {}

    for year_dir in get_vwo_years():
        year_path = os.path.join(SITE_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue

        # Archive years (2VWO, 3VWO) - skip, handled by build_archive_data()
        if ARCHIVE_YEAR_PATTERN.match(year_dir):
            continue

        # Modern years (4VWO, 5VWO, 6VWO) - use front matter
        data[year_dir] = process_modern_year(year_dir, resources_map, dev)

    # Sort and filter data
    sorted_data = {}
    for year in sorted(data.keys(), key=sort_years):
        year_data = {}

        for period in sorted(data[year].keys(), key=sort_period, reverse=True):
            tests = data[year][period]

            # Only include periods with content
            has_content = any(
                t.get("summary_link") or t.get("resources") for t in tests
            )
            if not has_content:
                continue

            # Filter and sort tests
            filtered_tests = [
                t for t in tests if t.get("summary_link") or t.get("resources")
            ]
            year_data[period] = sorted(filtered_tests, key=lambda t: t["subject"])

        if year_data:
            sorted_data[year] = year_data

    return sorted_data


def copy_if_exists(src, dest):
    if not os.path.exists(src):
        return

    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy2(src, dest)


def copy_static_assets(build_dir):
    # Copy standard directories and files
    copy_if_exists("site/assets", os.path.join(build_dir, "assets"))
    copy_if_exists("site/.well-known", os.path.join(build_dir, ".well-known"))
    copy_if_exists("site/robots.txt", os.path.join(build_dir, "robots.txt"))
    copy_if_exists("CNAME", os.path.join(build_dir, "CNAME"))

    # Copy non-markdown files from VWO year directories
    for year_dir in get_vwo_years():
        year_path = os.path.join(SITE_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue

        build_year_dir = os.path.join(build_dir, year_dir)

        for root, _, files in os.walk(year_path):
            non_md_files = [f for f in files if not f.endswith(".md")]

            for file in non_md_files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(
                    build_year_dir, os.path.relpath(src_file, year_path)
                )
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)


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

        return (
            datetime.fromtimestamp(first_commit_ts, tz=timezone.utc),
            datetime.fromtimestamp(last_commit_ts, tz=timezone.utc),
        )

    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return (None, None)


def setup_feed_generator():
    fg = FeedGenerator()
    fg.title(SITE_TITLE)
    fg.description(SITE_DESCRIPTION)
    fg.id(SITE_URL)
    fg.link(href=SITE_URL, rel="alternate")
    fg.language("nl")
    fg.author(name=AUTHOR_NAME, email=AUTHOR_EMAIL)
    fg.generator("Binder")
    return fg


def create_feed_entry_list(test):
    entries = []

    # Add summary link if exists
    if test.get("summary_link"):
        entries.append(
            {
                "link": test["summary_link"],
                "title": f"{test['subject']} - {test['test_material']}",
            }
        )

    # Add resource links
    for resource in test.get("resources", []):
        entries.append(
            {
                "link": resource.get("link"),
                "title": f"{resource.get('title', '')} - {test['subject']}".strip(" -"),
                "internal": resource.get("type") == "internal",
            }
        )

    return entries


def generate_feeds(build_dir, homepage_data, md_cache):
    fg = setup_feed_generator()

    feed_items = []

    for year, year_data in homepage_data.items():
        for period, tests in year_data.items():
            for test in tests:
                entries = create_feed_entry_list(test)

                for entry in entries:
                    link = entry.get("link")
                    if not link:
                        continue

                    # Get markdown file path if it's an internal link
                    is_internal = entry.get("internal", False) or link.startswith("/")
                    md_file_path = get_md_file_path(link) if is_internal else None
                    if not md_file_path:
                        continue

                    html_content = md_cache.get(link, entry["title"])
                    first_commit, last_commit = get_git_dates(md_file_path)

                    feed_items.append(
                        {
                            "link": link,
                            "title": f"{entry['title']} ({year} {period})",
                            "html": html_content,
                            "first_commit": first_commit,
                            "last_commit": last_commit,
                        }
                    )

    def item_sort_key(it):
        if it["last_commit"]:
            return int(it["last_commit"].timestamp())
        if it["first_commit"]:
            return int(it["first_commit"].timestamp())
        return float("-inf")

    feed_items.sort(key=item_sort_key)

    for item in feed_items:
        fe = fg.add_entry()
        fe.title(item["title"])
        fe.link(href=f"{SITE_URL}{item['link']}")
        fe.id(f"{SITE_URL}{item['link']}")
        fe.description(item["html"] or item["title"])

        if item["first_commit"]:
            fe.pubDate(item["first_commit"])
        if item["last_commit"]:
            fe.updated(item["last_commit"])

    with open(os.path.join(build_dir, "rss.xml"), "wb") as f:
        f.write(fg.rss_str(pretty=True))
    with open(os.path.join(build_dir, "atom.xml"), "wb") as f:
        f.write(fg.atom_str(pretty=True))


# CONTENT PROCESSING


def remove_base64_images(html_content):
    return re.sub(r'<img[^>]*src="data:image/[^"]*"[^>]*>', "", html_content)


class MathProtectPreprocessor(Preprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.math_store = {}
        self.counter = 0

    def run(self, lines):
        text = "\n".join(lines)

        def replace_display(match):
            key = f"MATH_DISPLAY_{self.counter}"
            self.counter += 1
            self.math_store[key] = match.group(0)
            return key

        def replace_inline(match):
            key = f"MATH_INLINE_{self.counter}"
            self.counter += 1
            self.math_store[key] = match.group(0)
            return key

        text = re.sub(r"\$\$([^\$]+)\$\$", replace_display, text)
        text = re.sub(r"\$([^\$\n]+)\$", replace_inline, text)

        return text.split("\n")


class MathProtectPostprocessor(Postprocessor):
    def __init__(self, md, math_store):
        super().__init__(md)
        self.math_store = math_store

    def run(self, text):
        for key, value in self.math_store.items():
            text = text.replace(key, value)
        return text


class MathProtectExtension(Extension):
    def extendMarkdown(self, md):
        preprocessor = MathProtectPreprocessor(md)
        md.preprocessors.register(preprocessor, "math_protect", 27)

        postprocessor = MathProtectPostprocessor(md, preprocessor.math_store)
        md.postprocessors.register(postprocessor, "math_restore", 0)


def setup_markdown_processor():
    return Markdown(
        extensions=[
            "meta",
            "codehilite",
            "tables",
            "toc",
            MathProtectExtension(),
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False},
        },
        tab_length=2,
    )


def render_special_pages(build_dir, template_env, homepage_data, archive_data):
    # index.html
    with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            template_env.get_template("home.html").render(
                homepage_data=homepage_data,
                archive_data=archive_data,
                site={"data": {"homepage_data": homepage_data}},
                page_path=f"{TEMPLATES_DIR}/home.html",
            )
        )

    # 404.html
    with open(os.path.join(build_dir, "404.html"), "w", encoding="utf-8") as f:
        f.write(template_env.get_template("404.html").render())


def process_markdown_file(
    md_file_path, year_path, build_year_dir, md_processor, template_env
):
    relative_path = os.path.relpath(md_file_path, year_path)
    build_path = os.path.join(
        build_year_dir, os.path.splitext(relative_path)[0] + ".html"
    )

    # Read and parse markdown
    with open(md_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    front_matter, markdown_content = parse_front_matter(content)

    # Add full subject name to front matter
    if front_matter.get("subject"):
        subject_abbr = front_matter["subject"].upper()
        front_matter["subject_name"] = SUBJECT_NAMES.get(subject_abbr, subject_abbr)

    # Convert to HTML
    html_content = remove_base64_images(md_processor.convert(markdown_content))
    md_processor.reset()

    # Render template
    rendered = template_env.get_template("summary.html").render(
        content=html_content,
        page=front_matter,
        page_path=md_file_path,
    )

    # Write output
    os.makedirs(os.path.dirname(build_path), exist_ok=True)
    with open(build_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    # Mark as hidden if hidden flag is set (for feed exclusion)
    is_hidden = front_matter.get("hidden")

    return relative_path, html_content, is_hidden


def process_markdown_files(build_dir, template_env, md_processor, dev=False):
    homepage_data = build_homepage_data(dev)
    archive_data = build_archive_data()
    md_cache = {}

    # Render special pages
    render_special_pages(build_dir, template_env, homepage_data, archive_data)

    # Process markdown files for each VWO year
    for year_dir in get_vwo_years():
        year_path = os.path.join(SITE_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue

        build_year_dir = os.path.join(build_dir, year_dir)
        os.makedirs(build_year_dir, exist_ok=True)

        for root, _, files in os.walk(year_path):
            md_files = [f for f in files if f.endswith(".md")]

            for file in md_files:
                md_file_path = os.path.join(root, file)
                relative_path, html_content, is_hidden = process_markdown_file(
                    md_file_path, year_path, build_year_dir, md_processor, template_env
                )

                # Cache HTML content for feed generation (unless hidden)
                if not is_hidden:
                    cache_key = f"/{year_dir}/{os.path.splitext(relative_path)[0]}"
                    md_cache[cache_key] = html_content

    return homepage_data, md_cache


# DEV SERVER


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

        if os.path.basename(event.src_path) == "binder.py":
            print(
                f"\n{Fore.YELLOW}Binder changed! Restarting process...{Style.RESET_ALL}\n"
            )
            os.execv(sys.executable, [sys.executable] + sys.argv)

        print(
            f"\n{Fore.YELLOW}Restarting! {Style.BRIGHT}{os.path.basename(event.src_path)} changed.{Style.RESET_ALL}\n"
        )
        self.build_func()


class BuildHTTPServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="build", **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)

        # root or directory request -> try index.html
        if self.path.endswith("/") or self.path == "":
            index_path = os.path.join(path, "index.html")
            if os.path.isfile(index_path):
                self.path = (
                    self.path.rstrip("/") + "/index.html"
                    if not self.path.endswith("index.html")
                    else self.path
                )
                return super().do_GET()

        # direct file
        if os.path.isfile(path):
            return super().do_GET()

        # try with ".html" extension
        if not self.path.endswith("/") and "." not in os.path.basename(self.path):
            html_path = path + ".html"
            if os.path.isfile(html_path):
                self.path += ".html"
                return super().do_GET()

        # serve 404.html if nothing matches
        not_found_path = os.path.join(self.directory, "404.html")
        if os.path.isfile(not_found_path):
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(not_found_path, "rb") as f:
                self.wfile.write(f.read())
            return

        # fallback: plain 404 if 404.html missing
        self.send_error(404, "File not found")


# BUILD PROCESS


def build(dev=False):
    print(f"{Fore.CYAN}=> Binder is binding <={Style.RESET_ALL}")
    if dev:
        print(
            f"{Fore.YELLOW}Development mode enabled (including hidden pages){Style.RESET_ALL}"
        )

    # Setup temporary build directory
    print("> Setup... ", end="", flush=True)
    temp_build_dir = tempfile.mkdtemp()
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Initialize template environment
    print("> Templates... ", end="", flush=True)
    template_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Initialize markdown processor
    print("> Markdown... ", end="", flush=True)
    md_processor = setup_markdown_processor()
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Copy static assets
    print("> Assets... ", end="", flush=True)
    copy_static_assets(temp_build_dir)
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Process markdown files
    print("> Pages... ", end="", flush=True)
    homepage_data, md_cache = process_markdown_files(
        temp_build_dir, template_env, md_processor, dev
    )
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Generate RSS and Atom feeds
    print("> Feeds... ", end="", flush=True)
    generate_feeds(temp_build_dir, homepage_data, md_cache)
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    # Move to final build directory
    print("> Output... ", end="", flush=True)
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    shutil.move(temp_build_dir, BUILD_DIR)
    print(f"{Fore.GREEN}done!{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Build complete!{Style.RESET_ALL}\n")


def serve(port=8000, dev=False):
    print(f"{Fore.BLUE}Server{Style.RESET_ALL}\n")

    # Initial build
    build(dev)

    # Setup file watcher
    observer = Observer()
    handler = BuildHandler(lambda: build(dev))
    observer.schedule(handler, SITE_DIR, recursive=True)
    observer.schedule(handler, ".", recursive=False)
    observer.start()

    # Start HTTP server
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


# CLI ENTRY POINT


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Binder - Static site generator for school summaries"
    )
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
        help="Port for server (default: 8000)",
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Enable development mode (include hidden pages)",
    )

    args = parser.parse_args()

    if args.command == "serve":
        serve(args.port, dev=args.dev)
    else:
        build(dev=args.dev)
