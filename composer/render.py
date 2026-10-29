import os
import re
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from .config import REPO_URL, TEMPLATES_DIR, TIMEZONE
from .git import head_commit
from .markdown_ext import create_markdown

MONTHS = (
    "januari",
    "februari",
    "maart",
    "april",
    "mei",
    "juni",
    "juli",
    "augustus",
    "september",
    "oktober",
    "november",
    "december",
)

BASE64_IMAGE_PATTERN = re.compile(r'<img[^>]*src="data:image/[^"]*"[^>]*>')


def format_datetime(moment):
    return f"{moment.day} {MONTHS[moment.month - 1]} {moment.year} om {moment:%H:%M}"


def template_source(name):
    return os.path.join(TEMPLATES_DIR, name)


def site_context():
    now = datetime.now(tz=TIMEZONE)
    return {
        "repo_url": REPO_URL,
        "commit": head_commit(),
        "built_at": format_datetime(now),
        "built_at_iso": now.isoformat(timespec="seconds"),
    }


class Renderer:
    def __init__(self, context, history):
        self.history = history
        self.markdown = create_markdown()
        self.env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)
        self.env.globals.update(context)

    def template_count(self):
        return len(self.env.list_templates())

    def page(self, page):
        content = BASE64_IMAGE_PATTERN.sub("", self.markdown.convert(page.body))
        toc = self.markdown.toc
        self.markdown.reset()
        rendered = self._render(
            "summary.jinja", page.source, content=content, toc=toc, meta=page.meta
        )
        return content, rendered

    def home(self, listing):
        return self._render(
            "home.jinja", template_source("home.jinja"), homepage_data=listing
        )

    def onderbouw(self, listing):
        return self._render(
            "onderbouw.jinja",
            template_source("onderbouw.jinja"),
            onderbouw_data=listing,
        )

    def not_found(self):
        return self._render("404.jinja", template_source("404.jinja"))

    def _render(self, template, source, **values):
        return self.env.get_template(template).render(
            page_path=source, **self._dates(source), **values
        )

    def _dates(self, source):
        created, updated = self.history.get(source, (None, None))
        created = created.astimezone(TIMEZONE) if created else None
        updated = updated.astimezone(TIMEZONE) if updated else None
        return {
            "page_created_iso": created.date().isoformat() if created else None,
            "page_updated": format_datetime(updated) if updated else None,
            "page_updated_iso": updated.isoformat(timespec="seconds")
            if updated
            else None,
        }
