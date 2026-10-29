from collections import defaultdict

from .config import ONDERBOUW_FAMILIES, PERIOD_PATTERN
from .content import ONDERBOUW, SUMMARY, natural_key, resource_key, year_number


def _period_key(period):
    match = PERIOD_PATTERN.match(period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)


def _is_listed(page, kind, include_hidden):
    return page.kind == kind and (include_hidden or not page.hidden)


def test_material(meta):
    label = meta.get("title") or meta.get("short") or ""
    description = meta.get("description") or ""
    if label and description:
        return f"{label} ({description})"
    if description:
        return f"({description})"
    return label


def _summary_entry(page, resources):
    meta = page.meta
    return {
        "page": page,
        "subject": meta["subject"],
        "subject_name": meta["subject_name"],
        "family": meta["family"],
        "test_material": test_material(meta),
        "resources": resources.get(resource_key(page), []),
        "summary_link": page.url,
    }


def summary_listing(pages, resources, include_hidden=False):
    grouped = defaultdict(lambda: defaultdict(list))
    for page in pages:
        if _is_listed(page, SUMMARY, include_hidden) and page.meta.get("subject"):
            entry = _summary_entry(page, resources)
            grouped[page.meta["year"]][page.meta["period"]].append(entry)

    return {
        year: {
            period: sorted(
                grouped[year][period],
                key=lambda e: (e["subject"], natural_key(e["summary_link"])),
            )
            for period in sorted(grouped[year], key=_period_key, reverse=True)
        }
        for year in sorted(grouped, key=year_number, reverse=True)
    }


def listed_summaries(listing):
    return [
        entry
        for periods in listing.values()
        for entries in periods.values()
        for entry in entries
    ]


def onderbouw_listing(pages, include_hidden=False):
    grouped = defaultdict(lambda: defaultdict(list))
    for page in pages:
        if _is_listed(page, ONDERBOUW, include_hidden):
            grouped[page.meta["year"]][page.meta["subject_name"]].append(
                {"link": page.url, "chapter": page.meta["chapter"]}
            )

    return {
        year: [
            {
                "name": subject,
                "family": ONDERBOUW_FAMILIES.get(subject, ""),
                "pages": sorted(chapters, key=lambda c: natural_key(c["chapter"])),
            }
            for subject, chapters in sorted(grouped[year].items())
        ]
        for year in sorted(grouped, key=year_number, reverse=True)
    }
