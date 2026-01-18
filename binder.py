import os
import sys
import shutil
import re
import subprocess
import time
import threading
import tempfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

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


class ProgressBar:
    LINE_WIDTH = 70

    def __init__(self, total, prefix="", width=25):
        self.total = max(total, 1)
        self.current = 0
        self.prefix = prefix[:10]
        self.width = width
        self.start_time = time.time()

    def update(self, n=1):
        self.current += n
        self._render()

    def _render(self):
        ratio = min(self.current / self.total, 1.0)
        filled = int(self.width * ratio)
        bar = "=" * filled
        if filled < self.width:
            bar += ">"
            bar += " " * (self.width - filled - 1)
        elapsed = time.time() - self.start_time
        line = f"  {self.prefix:10} [{bar}] {self.current:>3}/{self.total:<3} ({elapsed:.1f}s)"
        sys.stdout.write(f"\r{line:<{self.LINE_WIDTH}}")
        sys.stdout.flush()

    def finish(self):
        elapsed = (time.time() - self.start_time) * 1000
        count = self.current if self.current > 0 else self.total
        line = f"  {self.prefix:10} {Fore.GREEN}done{Style.RESET_ALL} ({count} items, {elapsed:.0f}ms)"
        sys.stdout.write(f"\r{line:<{self.LINE_WIDTH}}\n")
        sys.stdout.flush()


# CONSTANTS


SITE_DIR = "site"
BUILD_DIR = "build"
BUILD_DEV_DIR = "build-dev"
TEMPLATES_DIR = "site/templates"
DATA_DIR = "site/data"

RESOURCES_JSON = "site/data/resources.json"

SITE_URL = "https://school.gijs6.nl"
SITE_TITLE = "Samenvattingen :)"
SITE_DESCRIPTION = "Een verzameling van zelfgemaakte samenvattingen"
AUTHOR_NAME = "Gijs ten Berg"
AUTHOR_EMAIL = "me@gijs6.nl"

VWO_YEAR_PATTERN = re.compile(r"(\d)VWO")
ARCHIVE_YEAR_PATTERN = re.compile(r"[23]VWO")
PERIOD_PATTERN = re.compile(r"([A-Z]+)(\d+)")
FRONT_MATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

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


def parse_metadata(content):
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


def build_test_material(metadata):
    title = metadata.get("title", "")
    short = metadata.get("short", "")
    description = metadata.get("description", "")

    if title and description:
        return f"{title} ({description})"
    if title:
        return title

    if short and description:
        return f"{short} ({description})"
    if short:
        return short
    if description:
        return f"({description})"

    return ""


def create_test_entry(metadata, main_dir, sub_dir, file, resources_map):
    subject = metadata.get("subject", "").upper()

    entry = {
        "subject": subject,
        "subject_name": SUBJECT_NAMES.get(subject, subject),
        "test_material": build_test_material(metadata),
        "icon": SUBJECT_ICONS.get(subject, "fa-solid fa-file-lines"),
        "resources": resources_map.get(f"{main_dir}/{sub_dir}/{file}", []),
        "summary_link": f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}",
    }

    return entry


def copy_if_exists(src, dest):
    if not os.path.exists(src):
        return 0

    if os.path.isdir(src):
        shutil.copytree(src, dest)
        return sum(len(files) for _, _, files in os.walk(dest))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(src, dest)
        return 1


def collect_static_assets(build_dir):
    tasks = []
    tasks.append(("site/assets", os.path.join(build_dir, "assets")))
    tasks.append(("site/.well-known", os.path.join(build_dir, ".well-known")))
    tasks.append(("site/robots.txt", os.path.join(build_dir, "robots.txt")))
    tasks.append(("CNAME", os.path.join(build_dir, "CNAME")))

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
                tasks.append((src_file, dest_file))

    return tasks


def copy_static_assets(build_dir, progress=None):
    tasks = collect_static_assets(build_dir)
    for src, dest in tasks:
        copy_if_exists(src, dest)
        if progress:
            progress.update()
    return len(tasks)


def get_all_git_dates():
    try:
        output = subprocess.check_output(
            ["git", "log", "--format=%ct", "--name-only", "--diff-filter=A"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()

        first_commits = {}
        current_ts = None
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            if line.isdigit():
                current_ts = int(line)
            elif current_ts:
                first_commits[line] = current_ts

        output = subprocess.check_output(
            ["git", "log", "--format=%ct", "--name-only"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()

        last_commits = {}
        current_ts = None
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            if line.isdigit():
                current_ts = int(line)
            elif current_ts and line not in last_commits:
                last_commits[line] = current_ts

        git_dates = {}
        all_files = set(first_commits.keys()) | set(last_commits.keys())
        for filepath in all_files:
            first_ts = first_commits.get(filepath)
            last_ts = last_commits.get(filepath)
            first_dt = (
                datetime.fromtimestamp(first_ts, tz=timezone.utc) if first_ts else None
            )
            last_dt = (
                datetime.fromtimestamp(last_ts, tz=timezone.utc) if last_ts else None
            )
            git_dates[filepath] = (first_dt, last_dt)

        return git_dates

    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return {}


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

    if test.get("summary_link"):
        entries.append(
            {
                "link": test["summary_link"],
                "title": f"{test['subject']} - {test['test_material']}",
            }
        )

    for resource in test.get("resources", []):
        entries.append(
            {
                "link": resource.get("link"),
                "title": f"{resource.get('title', '')} - {test['subject']}".strip(" -"),
            }
        )

    return entries


def generate_feeds(build_dir, homepage_data, md_cache, git_dates, progress=None):
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

                    is_internal = link.startswith("/")
                    md_file_path = get_md_file_path(link) if is_internal else None
                    if not md_file_path:
                        continue

                    html_content = md_cache.get(link, entry["title"])
                    rel_path = os.path.relpath(md_file_path)
                    first_commit, last_commit = git_dates.get(rel_path, (None, None))

                    feed_items.append(
                        {
                            "link": link,
                            "title": f"{entry['title']} ({year} {period})",
                            "html": html_content,
                            "first_commit": first_commit,
                            "last_commit": last_commit,
                        }
                    )
                    if progress:
                        progress.update()

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


BASE64_IMAGE_PATTERN = re.compile(r'<img[^>]*src="data:image/[^"]*"[^>]*>')


def remove_base64_images(html_content):
    return BASE64_IMAGE_PATTERN.sub("", html_content)


MATH_DISPLAY_PATTERN = re.compile(r"\$\$([^\$]+)\$\$")
MATH_INLINE_PATTERN = re.compile(r"\$([^\$\n]+)\$")


class MathProtectPreprocessor(Preprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.math_store = {}
        self.counter = 0

    def reset(self):
        self.math_store.clear()
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

        text = MATH_DISPLAY_PATTERN.sub(replace_display, text)
        text = MATH_INLINE_PATTERN.sub(replace_inline, text)

        return text.split("\n")


class MathProtectPostprocessor(Postprocessor):
    def __init__(self, md, math_store):
        super().__init__(md)
        self.math_store = math_store

    def run(self, text):
        for key in sorted(self.math_store.keys(), key=len, reverse=True):
            text = text.replace(key, self.math_store[key])
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
    with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            template_env.get_template("home.html").render(
                homepage_data=homepage_data,
                archive_data=archive_data,
                site={"data": {"homepage_data": homepage_data}},
                page_path=f"{TEMPLATES_DIR}/home.html",
            )
        )

    with open(os.path.join(build_dir, "404.html"), "w", encoding="utf-8") as f:
        f.write(template_env.get_template("404.html").render())


def process_markdown_file(
    md_file_path, year_path, build_year_dir, md_processor, template_env
):
    relative_path = os.path.relpath(md_file_path, year_path)
    build_path = os.path.join(
        build_year_dir, os.path.splitext(relative_path)[0] + ".html"
    )

    with open(md_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    metadata, markdown_content = parse_metadata(content)

    if metadata.get("subject"):
        subject_abbr = metadata["subject"].upper()
        metadata["subject_name"] = SUBJECT_NAMES.get(subject_abbr, subject_abbr)

    year_dir = os.path.basename(year_path)
    period_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else ""

    metadata["year"] = year_dir
    metadata["period"] = period_dir

    html_content = remove_base64_images(md_processor.convert(markdown_content))
    md_processor.reset()

    rendered = template_env.get_template("summary.html").render(
        content=html_content,
        meta=metadata,
        page_path=md_file_path,
    )

    os.makedirs(os.path.dirname(build_path), exist_ok=True)
    with open(build_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    is_hidden = metadata.get("hidden")

    return relative_path, html_content, is_hidden


def process_single_file(args):
    (
        md_file_path,
        year_path,
        build_year_dir,
        template_env,
        year_dir,
        resources_map,
        dev,
    ) = args

    md_processor = setup_markdown_processor()

    relative_path = os.path.relpath(md_file_path, year_path)
    build_path = os.path.join(
        build_year_dir, os.path.splitext(relative_path)[0] + ".html"
    )

    with open(md_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    metadata, markdown_content = parse_metadata(content)

    if metadata.get("subject"):
        subject_abbr = metadata["subject"].upper()
        metadata["subject_name"] = SUBJECT_NAMES.get(subject_abbr, subject_abbr)

    period_dir = relative_path.split(os.sep)[0] if os.sep in relative_path else ""
    metadata["year"] = year_dir
    metadata["period"] = period_dir

    html_content = remove_base64_images(md_processor.convert(markdown_content))
    md_processor.reset()

    rendered = template_env.get_template("summary.html").render(
        content=html_content,
        meta=metadata,
        page_path=md_file_path,
    )

    os.makedirs(os.path.dirname(build_path), exist_ok=True)
    with open(build_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    is_hidden = metadata.get("hidden")
    cache_key = f"/{year_dir}/{os.path.splitext(relative_path)[0]}"

    file_name = os.path.basename(md_file_path)
    entry = None
    if metadata.get("subject") and not ARCHIVE_YEAR_PATTERN.match(year_dir):
        if dev or not is_hidden:
            entry = create_test_entry(
                metadata, year_dir, period_dir, file_name, resources_map
            )

    return cache_key, html_content, is_hidden, year_dir, period_dir, entry


def process_markdown_files(build_dir, template_env, dev=False):
    resources_map = load_json_file(RESOURCES_JSON)
    archive_data = build_archive_data()
    md_cache = {}
    homepage_data = defaultdict(lambda: defaultdict(list))

    tasks = []
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
                tasks.append(
                    (
                        md_file_path,
                        year_path,
                        build_year_dir,
                        template_env,
                        year_dir,
                        resources_map,
                        dev,
                    )
                )

    progress = ProgressBar(len(tasks), prefix="Pages")
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as executor:
        futures = [executor.submit(process_single_file, task) for task in tasks]

        for future in as_completed(futures):
            cache_key, html_content, is_hidden, year_dir, period_dir, entry = (
                future.result()
            )
            if not is_hidden:
                md_cache[cache_key] = html_content
                if entry:
                    homepage_data[year_dir][period_dir].append(entry)
            progress.update()
    progress.finish()

    sorted_data = {}
    for year in sorted(homepage_data.keys(), key=sort_years):
        year_data = {}
        for period in sorted(homepage_data[year].keys(), key=sort_period, reverse=True):
            tests = homepage_data[year][period]
            has_content = any(
                t.get("summary_link") or t.get("resources") for t in tests
            )
            if not has_content:
                continue
            filtered_tests = [
                t for t in tests if t.get("summary_link") or t.get("resources")
            ]
            year_data[period] = sorted(filtered_tests, key=lambda t: t["subject"])
        if year_data:
            sorted_data[year] = year_data

    render_special_pages(build_dir, template_env, sorted_data, archive_data)

    return sorted_data, md_cache


def rebuild_single_markdown(src_path, build_dir):
    start_time = time.time()

    rel_to_site = os.path.relpath(src_path, SITE_DIR)
    parts = rel_to_site.split(os.sep)

    if len(parts) < 2 or not parts[0].endswith("VWO"):
        return False

    year_dir = parts[0]
    year_path = os.path.join(SITE_DIR, year_dir)
    build_year_dir = os.path.join(build_dir, year_dir)

    template_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    md_processor = setup_markdown_processor()

    process_markdown_file(
        src_path, year_path, build_year_dir, md_processor, template_env
    )

    elapsed = (time.time() - start_time) * 1000
    print(f"{Fore.GREEN}Rebuilt in {elapsed:.0f}ms{Style.RESET_ALL}\n")
    return True


class BuildHandler(FileSystemEventHandler):
    def __init__(self, build_func, build_dir):
        self.build_func = build_func
        self.build_dir = build_dir
        self.last_build = 0

    def on_modified(self, event):
        if event.is_directory or "build" in event.src_path:
            return
        now = time.time()
        if now - self.last_build < 0.5:
            return
        self.last_build = now

        src_path = event.src_path
        filename = os.path.basename(src_path)

        if filename == "binder.py":
            print(
                f"\n{Fore.YELLOW}Binder changed! Restarting process...{Style.RESET_ALL}\n"
            )
            os.execv(sys.executable, [sys.executable] + sys.argv)

        print(f"\n{Fore.YELLOW}Changed: {Style.BRIGHT}{filename}{Style.RESET_ALL}")

        if src_path.endswith(".md") and SITE_DIR in src_path:
            if rebuild_single_markdown(src_path, self.build_dir):
                return

        print(f"{Fore.CYAN}Full rebuild...{Style.RESET_ALL}")
        self.build_func()


class BuildHTTPServer(SimpleHTTPRequestHandler):
    directory = BUILD_DIR

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=self.directory, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)

        if self.path.endswith("/") or self.path == "":
            index_path = os.path.join(path, "index.html")
            if os.path.isfile(index_path):
                self.path = (
                    self.path.rstrip("/") + "/index.html"
                    if not self.path.endswith("index.html")
                    else self.path
                )
                return super().do_GET()

        if os.path.isfile(path):
            return super().do_GET()

        if not self.path.endswith("/") and "." not in os.path.basename(self.path):
            html_path = path + ".html"
            if os.path.isfile(html_path):
                self.path += ".html"
                return super().do_GET()

        not_found_path = os.path.join(self.directory, "404.html")
        if os.path.isfile(not_found_path):
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(not_found_path, "rb") as f:
                self.wfile.write(f.read())
            return

        self.send_error(404, "File not found")


def build(dev=False, output_dir=None):
    if output_dir is None:
        output_dir = BUILD_DIR

    start_time = time.time()
    print(f"{Fore.CYAN}Binder{Style.RESET_ALL}")
    print()

    print(f"{Fore.BLUE}[1/5] Setup{Style.RESET_ALL}")
    print("  Creating temp directory...")
    temp_build_dir = tempfile.mkdtemp()
    print(f"  Loading templates from {TEMPLATES_DIR}/")
    template_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    templates = list(template_env.list_templates())
    print(f"  Found {len(templates)} templates")
    print()

    print(f"{Fore.BLUE}[2/5] Collecting metadata{Style.RESET_ALL}")
    print("  Reading git history for file dates...")
    git_dates = get_all_git_dates()
    print(
        f"  {Fore.GREEN}done{Style.RESET_ALL} - tracked {len(git_dates)} files in repository"
    )
    print()

    print(f"{Fore.BLUE}[3/5] Copying static assets{Style.RESET_ALL}")
    asset_tasks = collect_static_assets(temp_build_dir)
    print(f"  Found {len(asset_tasks)} files to copy")
    asset_progress = ProgressBar(len(asset_tasks), prefix="Copying")
    copy_static_assets(temp_build_dir, progress=asset_progress)
    asset_progress.finish()
    print()

    print(f"{Fore.BLUE}[4/5] Processing markdown{Style.RESET_ALL}")
    years = get_vwo_years()
    print(f"  Found {len(years)} year directories: {', '.join(years)}")
    homepage_data, md_cache = process_markdown_files(temp_build_dir, template_env, dev)
    print(f"  Generated {len(md_cache)} HTML pages")
    print()

    print(f"{Fore.BLUE}[5/5] Generating feeds{Style.RESET_ALL}")
    print("  Creating RSS and Atom feeds...")
    feed_progress = ProgressBar(len(md_cache), prefix="Entries")
    generate_feeds(
        temp_build_dir, homepage_data, md_cache, git_dates, progress=feed_progress
    )
    feed_progress.finish()
    print("  Wrote rss.xml and atom.xml")
    print()

    print(f"{Fore.BLUE}Finalizing{Style.RESET_ALL}")
    if os.path.exists(output_dir):
        print("  Removing old build directory...")
        shutil.rmtree(output_dir)
    print(f"  Moving build to {output_dir}/")
    shutil.move(temp_build_dir, output_dir)

    total_time = time.time() - start_time
    print()
    print(f"{Fore.GREEN}Build complete in {total_time * 1000:.0f}ms{Style.RESET_ALL}")
    print()


def serve(port=8000, dev=False):
    print(f"{Fore.BLUE}Server{Style.RESET_ALL}\n")

    build(dev, output_dir=BUILD_DEV_DIR)

    observer = Observer()
    handler = BuildHandler(lambda: build(dev, output_dir=BUILD_DEV_DIR), BUILD_DEV_DIR)
    observer.schedule(handler, SITE_DIR, recursive=True)
    observer.schedule(handler, ".", recursive=False)
    observer.start()

    class DevHTTPServer(BuildHTTPServer):
        directory = BUILD_DEV_DIR

    server = HTTPServer(("localhost", port), DevHTTPServer)
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
