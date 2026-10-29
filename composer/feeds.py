import os

from feedgen.feed import FeedGenerator

from .config import AUTHOR_EMAIL, AUTHOR_NAME, SITE_DESCRIPTION, SITE_TITLE, SITE_URL
from .listing import listed_summaries


def _feed_generator():
    generator = FeedGenerator()
    generator.title(SITE_TITLE)
    generator.description(SITE_DESCRIPTION)
    generator.id(SITE_URL)
    generator.link(href=SITE_URL, rel="alternate")
    generator.language("nl")
    generator.author(name=AUTHOR_NAME, email=AUTHOR_EMAIL)
    generator.generator("Composer")
    return generator


def write_feeds(output_dir, listing, contents, history):
    def last_change(entry):
        created, updated = history.get(entry["page"].source, (None, None))
        moment = updated or created
        return moment.timestamp() if moment else float("-inf")

    generator = _feed_generator()
    entries = sorted(listed_summaries(listing), key=last_change)
    for entry in entries:
        page = entry["page"]
        title = (
            f"{entry['subject']} · {entry['test_material']}"
            f" ({page.meta['year']} {page.meta['period']})"
        )
        url = f"{SITE_URL}{page.url}"
        created, updated = history.get(page.source, (None, None))

        item = generator.add_entry()
        item.title(title)
        item.link(href=url)
        item.id(url)
        item.description(contents.get(page.url) or title)
        if created:
            item.pubDate(created)
        if updated:
            item.updated(updated)

    generator.rss_file(os.path.join(output_dir, "rss.xml"), pretty=True)
    generator.atom_file(os.path.join(output_dir, "atom.xml"), pretty=True)
    return len(entries)
