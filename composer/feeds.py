import os
from feedgen.feed import FeedGenerator

from .config import SITE_URL, SITE_TITLE, SITE_DESCRIPTION, AUTHOR_NAME, AUTHOR_EMAIL
from .utils import get_md_file_path


def setup_feed_generator():
    fg = FeedGenerator()
    fg.title(SITE_TITLE)
    fg.description(SITE_DESCRIPTION)
    fg.id(SITE_URL)
    fg.link(href=SITE_URL, rel="alternate")
    fg.language("nl")
    fg.author(name=AUTHOR_NAME, email=AUTHOR_EMAIL)
    fg.generator("Composer")
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
                for entry in create_feed_entry_list(test):
                    link = entry.get("link")
                    if not link:
                        continue
                    md_file_path = (
                        get_md_file_path(link) if link.startswith("/") else None
                    )
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
