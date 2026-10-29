import os
from xml.etree.ElementTree import (
    Element,
    ElementTree,
    SubElement,
    indent,
    register_namespace,
)

from .config import SITE_URL, TIMEZONE
from .content import ONDERBOUW, SUMMARY
from .render import template_source

NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"


def _sitemap_urls(pages):
    public = [page for page in pages if not page.hidden]
    yield "/", template_source("home.jinja")
    yield from ((page.url, page.source) for page in public if page.kind == SUMMARY)
    yield "/onderbouw/", template_source("onderbouw.jinja")
    yield from ((page.url, page.source) for page in public if page.kind == ONDERBOUW)


def write_sitemap(output_dir, pages, history):
    register_namespace("", NAMESPACE)
    urlset = Element(f"{{{NAMESPACE}}}urlset")

    count = 0
    for path, source in _sitemap_urls(pages):
        url = SubElement(urlset, f"{{{NAMESPACE}}}url")
        SubElement(url, f"{{{NAMESPACE}}}loc").text = f"{SITE_URL}{path}"
        _, updated = history.get(source, (None, None))
        if updated:
            lastmod = updated.astimezone(TIMEZONE).date().isoformat()
            SubElement(url, f"{{{NAMESPACE}}}lastmod").text = lastmod
        count += 1

    tree = ElementTree(urlset)
    indent(tree, space="    ")
    with open(os.path.join(output_dir, "sitemap.xml"), "wb") as sitemap:
        sitemap.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(sitemap, encoding="utf-8", xml_declaration=False)
    return count
