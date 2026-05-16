import os
import re
import sys
import json
import time
import yaml
import shutil
from colorama import Fore, Style

from .config import (
    SITE_DIR,
    FRONT_MATTER_PATTERN,
    YEAR_DIR_PATTERN,
    PERIOD_PATTERN,
    SUBJECT_NAMES,
    SUBJECT_ICONS,
    ONDERBOUW_DIR,
)

BASE64_IMAGE_PATTERN = re.compile(r'<img[^>]*src="data:image/[^"]*"[^>]*>')


class ProgressBar:
    # Chars in the progress line excluding the bar itself: "  " + prefix(10) + " [" + "] NNN/NNN (99.9s)" = ~31
    _OVERHEAD = 31

    def __init__(self, total, prefix="", width=25):
        self.total = max(total, 1)
        self.current = 0
        self.prefix = prefix[:10]
        self.width = width
        self.start_time = time.time()

    def update(self, n=1):
        self.current += n
        self._render()

    def _bar_width(self):
        term_width = shutil.get_terminal_size((80, 24)).columns
        return max(5, min(self.width, term_width - self._OVERHEAD))

    def _term_width(self):
        return shutil.get_terminal_size((80, 24)).columns

    def _render(self):
        ratio = min(self.current / self.total, 1.0)
        bar_width = self._bar_width()
        filled = int(bar_width * ratio)
        bar = "=" * filled
        if filled < bar_width:
            bar += ">"
            bar += " " * (bar_width - filled - 1)
        elapsed = time.time() - self.start_time
        line = f"  {self.prefix:10} [{bar}] {self.current:>3}/{self.total:<3} ({elapsed:.1f}s)"
        max_width = self._term_width() - 1
        sys.stdout.write(f"\r{line:<{max_width}}"[:max_width + 1])
        sys.stdout.flush()

    def finish(self):
        elapsed = (time.time() - self.start_time) * 1000
        count = self.current if self.current > 0 else self.total
        line = f"  {self.prefix:10} {Fore.GREEN}done{Style.RESET_ALL} ({count} items, {elapsed:.0f}ms)"
        max_width = self._term_width() - 1
        sys.stdout.write(f"\r{line:<{max_width}}\n")
        sys.stdout.flush()


def remove_base64_images(html_content):
    return BASE64_IMAGE_PATTERN.sub("", html_content)


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
    match = YEAR_DIR_PATTERN.match(yearstr)
    return -int(match.group(1)) if match else float("inf")


def sort_period(period):
    match = PERIOD_PATTERN.match(period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)


def get_year_dirs():
    year_dirs = [d for d in os.listdir(SITE_DIR) if YEAR_DIR_PATTERN.match(d)]
    return sorted(year_dirs, key=lambda x: int(x[0]), reverse=True)


def get_onderbouw_dirs():
    if not os.path.isdir(ONDERBOUW_DIR):
        return []
    year_dirs = [d for d in os.listdir(ONDERBOUW_DIR) if YEAR_DIR_PATTERN.match(d)]
    return sorted(year_dirs, key=lambda x: int(x[0]))


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
    return {
        "subject": subject,
        "subject_name": SUBJECT_NAMES.get(subject, subject),
        "test_material": build_test_material(metadata),
        "icon": SUBJECT_ICONS.get(subject, "fa-solid fa-file-lines"),
        "resources": resources_map.get(f"{main_dir}/{sub_dir}/{file}", []),
        "summary_link": f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}",
    }
