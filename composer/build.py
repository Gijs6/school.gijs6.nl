import os
import shutil
import tempfile
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from colorama import Fore, Style
from jinja2 import Environment, FileSystemLoader

from .config import (
    SITE_DIR,
    BUILD_DIR,
    TEMPLATES_DIR,
    RESOURCES_JSON,
    SUBJECT_NAMES,
    ARCHIVE_DIR_PATTERN,
    YEAR_DIR_PATTERN,
)
from .utils import (
    ProgressBar,
    parse_metadata,
    sort_years,
    sort_period,
    get_year_dirs,
    build_archive_data,
    load_json_file,
    create_test_entry,
    remove_base64_images,
)
from .markdown_ext import setup_markdown_processor
from .assets import collect_static_assets, copy_static_assets
from .feeds import generate_feeds
from .git import get_all_git_dates

_thread_local = threading.local()


def _thread_md():
    if not hasattr(_thread_local, "md"):
        _thread_local.md = setup_markdown_processor()
    return _thread_local.md


def _thread_env():
    if not hasattr(_thread_local, "env"):
        _thread_local.env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    return _thread_local.env


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


def process_single_file(args):
    md_file_path, year_path, build_year_dir, year_dir, resources_map, dev = args

    md_processor = _thread_md()
    template_env = _thread_env()

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
    metadata["canonical_url"] = f"/{year_dir}/{os.path.splitext(relative_path)[0]}"

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

    entry = None
    if metadata.get("subject") and not ARCHIVE_DIR_PATTERN.match(year_dir):
        if dev or not is_hidden:
            entry = create_test_entry(
                metadata,
                year_dir,
                period_dir,
                os.path.basename(md_file_path),
                resources_map,
            )

    return cache_key, html_content, is_hidden, year_dir, period_dir, entry


def rebuild_single_markdown(src_path, build_dir):
    start_time = time.time()

    rel_to_site = os.path.relpath(src_path, SITE_DIR)
    parts = rel_to_site.split(os.sep)

    if len(parts) < 2 or not YEAR_DIR_PATTERN.match(parts[0]):
        return False

    year_dir = parts[0]
    year_path = os.path.join(SITE_DIR, year_dir)
    build_year_dir = os.path.join(build_dir, year_dir)
    resources_map = load_json_file(RESOURCES_JSON)

    process_single_file(
        (src_path, year_path, build_year_dir, year_dir, resources_map, True)
    )

    elapsed = (time.time() - start_time) * 1000
    print(f"{Fore.GREEN}Rebuilt in {elapsed:.0f}ms{Style.RESET_ALL}\n")
    return True


def process_markdown_files(build_dir, template_env, dev=False):
    resources_map = load_json_file(RESOURCES_JSON)
    archive_data = build_archive_data()
    md_cache = {}
    homepage_data = defaultdict(lambda: defaultdict(list))

    tasks = []
    for year_dir in get_year_dirs():
        year_path = os.path.join(SITE_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue
        build_year_dir = os.path.join(build_dir, year_dir)
        os.makedirs(build_year_dir, exist_ok=True)
        for root, _, files in os.walk(year_path):
            for file in (f for f in files if f.endswith(".md")):
                tasks.append(
                    (
                        os.path.join(root, file),
                        year_path,
                        build_year_dir,
                        year_dir,
                        resources_map,
                        dev,
                    )
                )

    progress = ProgressBar(len(tasks), prefix="Pages")
    with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 4) * 2)) as executor:
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
            filtered = [
                t
                for t in homepage_data[year][period]
                if t.get("summary_link") or t.get("resources")
            ]
            if filtered:
                year_data[period] = sorted(filtered, key=lambda t: t["subject"])
        if year_data:
            sorted_data[year] = year_data

    render_special_pages(build_dir, template_env, sorted_data, archive_data)
    return sorted_data, md_cache


def build(dev=False, output_dir=None):
    if output_dir is None:
        output_dir = BUILD_DIR

    start_time = time.time()
    print(f"{Fore.CYAN}Composer{Style.RESET_ALL}")
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
    years = get_year_dirs()
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
