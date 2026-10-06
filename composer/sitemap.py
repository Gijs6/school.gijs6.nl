import os
from xml.etree.ElementTree import Element, ElementTree, SubElement, register_namespace

from .config import ONDERBOUW_DIR, SITE_DIR, SITE_URL
from .utils import get_onderbouw_dirs, get_year_dirs, parse_metadata

_SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"


def _last_modified(git_dates, path):
    _, last_commit = git_dates.get(path, (None, None))
    return last_commit.date().isoformat() if last_commit else None


def _add_url(urlset, path, git_dates, source_path):
    url = SubElement(urlset, f"{{{_SITEMAP_NAMESPACE}}}url")
    SubElement(url, f"{{{_SITEMAP_NAMESPACE}}}loc").text = f"{SITE_URL}{path}"

    last_modified = _last_modified(git_dates, source_path)
    if last_modified:
        SubElement(url, f"{{{_SITEMAP_NAMESPACE}}}lastmod").text = last_modified


def _markdown_files(root):
    for directory, directories, files in os.walk(root):
        directories.sort()
        for filename in sorted(files):
            if filename.endswith(".md"):
                yield os.path.join(directory, filename)


def generate_sitemap(build_dir, git_dates):
    """Write a sitemap for every public HTML page generated from Markdown."""
    register_namespace("", _SITEMAP_NAMESPACE)
    urlset = Element(f"{{{_SITEMAP_NAMESPACE}}}urlset")

    _add_url(urlset, "/", git_dates, "site/templates/home.jinja")
    _add_url(urlset, "/onderbouw/", git_dates, "site/templates/onderbouw.jinja")

    for year_dir in get_year_dirs():
        year_path = os.path.join(SITE_DIR, year_dir)
        for source_path in _markdown_files(year_path):
            with open(source_path, "r", encoding="utf-8") as f:
                metadata, _ = parse_metadata(f.read())
            if metadata.get("hidden"):
                continue

            relative_path = os.path.relpath(source_path, year_path)
            page_path = os.path.splitext(relative_path)[0].replace(os.sep, "/")
            _add_url(urlset, f"/{year_dir}/{page_path}", git_dates, source_path)

    for year_dir in get_onderbouw_dirs():
        year_path = os.path.join(ONDERBOUW_DIR, year_dir)
        for source_path in _markdown_files(year_path):
            page_name = os.path.splitext(os.path.basename(source_path))[0]
            _add_url(
                urlset,
                f"/onderbouw/{year_dir}/{page_name}",
                git_dates,
                source_path,
            )

    ElementTree(urlset).write(
        os.path.join(build_dir, "sitemap.xml"),
        encoding="utf-8",
        xml_declaration=True,
    )
