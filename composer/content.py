import json
import os
import re
from dataclasses import dataclass

import yaml

from .config import (
    ASSETS_DIR,
    DATA_DIR,
    FAVICON,
    ONDERBOUW_DIR,
    ONDERBOUW_FAMILIES,
    RESOURCES_JSON,
    SITE_DIR,
    SUBJECTS,
    TEMPLATES_DIR,
    YEAR_DIR_PATTERN,
)

SUMMARY = "summary"
ONDERBOUW = "onderbouw"

TEMPLATE = "template"
DATA = "data"
PAGE = "page"
STATIC = "static"

FRONT_MATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
IGNORED_SUFFIXES = ("~", ".swp", ".swo", ".swx", ".tmp", ".part", "___jb_tmp___")


class ContentError(Exception):
    pass


@dataclass
class Page:
    kind: str
    source: str
    url: str
    meta: dict
    body: str

    @property
    def output(self):
        return page_output(self.url)

    @property
    def hidden(self):
        return bool(self.meta.get("hidden"))


def year_number(name):
    match = YEAR_DIR_PATTERN.fullmatch(name)
    return int(match.group(1)) if match else None


def year_dirs(directory):
    if not os.path.isdir(directory):
        return []
    years = [name for name in os.listdir(directory) if year_number(name) is not None]
    return sorted(years, key=year_number, reverse=True)


def natural_key(value):
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", value)
    ]


def is_under(path, directory):
    return os.path.normpath(path).startswith(os.path.normpath(directory) + os.sep)


def is_ignored(path):
    parts = os.path.normpath(path).split(os.sep)
    name = parts[-1]
    return (
        name.startswith(".")
        or name.endswith(IGNORED_SUFFIXES)
        or name == "4913"
        or "__pycache__" in parts
    )


def _site_parts(path):
    return os.path.relpath(path, SITE_DIR).split(os.sep)


def page_kind(path):
    if not path.endswith(".md"):
        return None
    parts = _site_parts(path)
    if len(parts) >= 2 and year_number(parts[0]) is not None:
        return SUMMARY
    if (
        len(parts) >= 3
        and is_under(path, ONDERBOUW_DIR)
        and year_number(parts[1]) is not None
    ):
        return ONDERBOUW
    return None


def classify(path):
    if is_ignored(path):
        return None
    if is_under(path, TEMPLATES_DIR):
        return TEMPLATE
    if is_under(path, DATA_DIR):
        return DATA
    if page_kind(path):
        return PAGE
    if _is_static(path):
        return STATIC
    return None


def _is_static(path):
    if os.path.normpath(path) == FAVICON or is_under(path, ASSETS_DIR):
        return True
    parts = _site_parts(path)
    return (
        len(parts) >= 2
        and year_number(parts[0]) is not None
        and not path.endswith(".md")
    )


def page_url(source):
    parts = _site_parts(source)
    if page_kind(source) == ONDERBOUW:
        stem = os.path.splitext(parts[-1])[0]
        return f"/onderbouw/{parts[1]}/{stem}"
    return "/" + "/".join(parts).removesuffix(".md")


def page_output(url):
    return url.removeprefix("/") + ".html"


def output_path(source):
    if page_kind(source):
        return page_output(page_url(source))
    return os.path.relpath(source, SITE_DIR)


def _walk(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = sorted(d for d in dirs if not is_ignored(os.path.join(root, d)))
        for name in sorted(files):
            path = os.path.join(root, name)
            if not is_ignored(path):
                yield path


def page_sources():
    for year in year_dirs(SITE_DIR):
        yield from (p for p in _walk(os.path.join(SITE_DIR, year)) if page_kind(p))
    for year in year_dirs(ONDERBOUW_DIR):
        yield from (p for p in _walk(os.path.join(ONDERBOUW_DIR, year)) if page_kind(p))


def static_sources():
    if os.path.isfile(FAVICON):
        yield FAVICON
    yield from _walk(ASSETS_DIR)
    for year in year_dirs(SITE_DIR):
        yield from (
            p for p in _walk(os.path.join(SITE_DIR, year)) if classify(p) == STATIC
        )


def parse_front_matter(text, source):
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        return {}, text
    try:
        meta = yaml.load(match.group(1), Loader=YAML_LOADER) or {}
    except yaml.YAMLError as exc:
        raise ContentError(f"{source}: invalid front matter\n{exc}") from exc
    if not isinstance(meta, dict):
        raise ContentError(f"{source}: front matter is not a mapping")
    return meta, text[match.end() :].strip()


def split_onderbouw_name(stem):
    subject, _, chapter = stem.partition("-")
    chapter = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", chapter.replace("_", " "))
    chapter = re.sub(r"\s*&\s*", " & ", chapter)
    return subject.replace("_", " "), chapter


def _summary_meta(meta, parts, url):
    meta.update(
        year=parts[0],
        period=parts[1] if len(parts) > 2 else "",
        canonical_url=url,
    )
    subject = str(meta.get("subject") or "").upper()
    if subject:
        name, family = SUBJECTS.get(subject, (subject, ""))
        meta.update(subject=subject, subject_name=name, family=family)


def _onderbouw_meta(meta, parts, url):
    subject, chapter = split_onderbouw_name(os.path.splitext(parts[-1])[0])
    meta.update(
        year=parts[1],
        period="",
        canonical_url=url,
        back_url="/onderbouw/",
        subject_name=subject,
        family=ONDERBOUW_FAMILIES.get(subject, ""),
        chapter=chapter,
    )
    if not meta.get("title") and not meta.get("short"):
        meta["short"] = chapter


def load_page(source):
    kind = page_kind(source)
    if kind is None:
        raise ContentError(f"{source}: not a page")
    with open(source, encoding="utf-8") as f:
        meta, body = parse_front_matter(f.read(), source)
    url = page_url(source)
    if kind == SUMMARY:
        _summary_meta(meta, _site_parts(source), url)
    else:
        _onderbouw_meta(meta, _site_parts(source), url)
    return Page(kind, source, url, meta, body)


def load_pages():
    return [load_page(source) for source in page_sources()]


def load_resources():
    if not os.path.isfile(RESOURCES_JSON):
        return {}
    with open(RESOURCES_JSON, encoding="utf-8") as f:
        return json.load(f)


def resource_key(page):
    return "/".join(_site_parts(page.source))
