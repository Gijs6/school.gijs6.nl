import os
import shutil
import re
import yaml
import json
from jinja2 import Environment, FileSystemLoader
from markdown import Markdown
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone


def sort_years(yearstr):
    match = re.match(r"(\d)(VWO)", yearstr)
    return -int(match.group(1)) if match else float("inf")


def sort_period(period):
    match = re.match(r"([A-Z]+)(\d+)", period)
    if match:
        return (int(match.group(2)), match.group(1))
    return (float("inf"), period)


def build_homepage_data():
    with open("site/data/test_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    site_dir = "site"
    main_dirs = [d for d in os.listdir(site_dir) if re.match(r"\dVWO", d)]

    for main_dir in main_dirs:
        main_path = os.path.join(site_dir, main_dir)
        sub_dirs = [
            d
            for d in os.listdir(main_path)
            if os.path.isdir(os.path.join(main_path, d))
        ]
        for sub_dir in sub_dirs:
            sub_path = os.path.join(main_path, sub_dir)
            files = [f for f in os.listdir(sub_path) if f.endswith(".md")]
            for file in files:
                file_path = os.path.join(sub_path, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
                if match:
                    front_matter = yaml.safe_load(match.group(1))

                    test_code = front_matter.get("test_code", [])
                    if isinstance(test_code, str):
                        test_code = [test_code]

                    summary_name = front_matter.get("summary_name", "Samenvatting")
                    summary_type = front_matter.get("summary_type", "basic")

                else:
                    front_matter = []
                    test_code = []
                    summary_name = "Samenvatting"
                    summary_type = "basic"

                for test_data in filter(
                    lambda t: t["test_code"] in test_code, data[main_dir][sub_dir]
                ):
                    if summary_type != "basic":
                        if not any(
                            summary_name in resource["title"]
                            for resource in test_data["resources"]
                        ):
                            test_data["resources"].append(
                                {
                                    "link": f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}",
                                    "title": summary_name,
                                    "type": "internal",
                                }
                            )
                        test_data["resources"].sort(key=lambda r: r["title"])

                    else:
                        test_data["summary_link"] = (
                            f"/{main_dir}/{sub_dir}/{file.replace('.md', '')}"
                        )
                        test_data["summary_name"] = summary_name

                    if not test_data.get("summary_link") and "summary" in summary_type:
                        test_data["summary_made"] = True

    sorted_data = {}

    for year in sorted(data.keys(), key=sort_years):
        year_data = {}

        for period in sorted(data[year].keys(), key=sort_period, reverse=True):
            if [
                "Ouioui"
                for test in data[year][period]
                if test.get("summary_link") or test.get("resources")
            ]:
                tests_to_include = [
                    test
                    for test in data[year][period]
                    if test.get("make_summary") or test.get("resources")
                ]
                year_data[period] = sorted(
                    tests_to_include, key=lambda subjectdata: subjectdata["subject"]
                )

        if year_data:
            sorted_data[year] = year_data

    return sorted_data


def setup_build_directory():
    build_dir = "build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    return build_dir


def copy_static_assets(build_dir):
    assets_src = "site/assets"
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, os.path.join(build_dir, "assets"))

    static_files = ["CNAME"]
    for file in static_files:
        if os.path.exists(file):
            shutil.copy2(file, os.path.join(build_dir, file))


def generate_feeds(build_dir, homepage_data, md_processor):
    fg = FeedGenerator()
    fg.title("Leermiddelenoverzicht")
    fg.description("Een verzameling van samenvattingen en leermiddelen")
    fg.id("https://school.gijs6.nl")
    fg.link(href="https://school.gijs6.nl", rel="alternate")
    fg.link(href="https://school.gijs6.nl/rss.xml", rel="self")
    fg.language("nl")
    fg.author(name="Gijs ten Berg", email="gijs6@dupunkto.org")
    fg.generator("Binder")

    for year, year_data in homepage_data.items():
        for period, tests in year_data.items():
            for test in tests:
                if test.get("summary_link"):
                    md_file_path = os.path.join("site", test['summary_link'].lstrip('/') + '.md')
                    if os.path.exists(md_file_path):
                        with open(md_file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        if content.startswith("---"):
                            _, front_matter_str, markdown_content = content.split("---", 2)
                        else:
                            markdown_content = content
                        
                        html_content = md_processor.convert(markdown_content.strip())
                        html_content = remove_base64_images(html_content)
                    else:
                        html_content = f"Samenvatting voor {test['subject']} - {test['test_material']}"
                    
                    fe = fg.add_entry()
                    fe.title(
                        f"{test['subject']} - {test['test_material']} ({year} {period})"
                    )
                    fe.link(href=f"https://school.gijs6.nl{test['summary_link']}")
                    fe.id(f"https://school.gijs6.nl{test['summary_link']}")
                    fe.description(html_content)
                    fe.pubDate(datetime.now(timezone.utc))

                for resource in test.get("resources", []):
                    if resource.get("type") == "internal":
                        md_file_path = os.path.join("site", resource['link'].lstrip('/') + '.md')
                        if os.path.exists(md_file_path):
                            with open(md_file_path, "r", encoding="utf-8") as f:
                                content = f.read()
                            
                            if content.startswith("---"):
                                _, front_matter_str, markdown_content = content.split("---", 2)
                            else:
                                markdown_content = content
                            
                            html_content = md_processor.convert(markdown_content.strip())
                            html_content = remove_base64_images(html_content)
                        else:
                            html_content = f"{resource['title']} voor {test['subject']} - {test['test_material']}"
                        
                        fe = fg.add_entry()
                        fe.title(
                            f"{resource['title']} - {test['subject']} ({year} {period})"
                        )
                        fe.link(href=f"https://school.gijs6.nl{resource['link']}")
                        fe.id(f"https://school.gijs6.nl{resource['link']}")
                        fe.description(html_content)
                        fe.pubDate(datetime.now(timezone.utc))

    fg.rss_str(pretty=True)
    fg.rss_file(os.path.join(build_dir, "rss.xml"))

    fg.atom_str(pretty=True)
    fg.atom_file(os.path.join(build_dir, "atom.xml"))


def remove_base64_images(html_content):
    img_pattern = r'<img[^>]*src="data:image/[^"]*"[^>]*>'
    return re.sub(img_pattern, '', html_content)


def setup_markdown_processor():
    return Markdown(
        extensions=["meta", "codehilite", "tables", "toc"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False}
        },
    )


def process_markdown_files(build_dir, template_env, md_processor):
    # Always generate index.html from home template
    homepage_data = build_homepage_data()

    vwo_pages = []
    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            for root, dirs, files in os.walk(year_path):
                vwo_pages.append((root, dirs, files))

    template = template_env.get_template("home.html")
    rendered = template.render(
        homepage_data=homepage_data,
        vwo_pages=vwo_pages,
        site={
            "title": "Leermiddelenoverzicht",
            "data": {"homepage_data": homepage_data},
        },
    )

    with open(os.path.join(build_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(rendered)

    for year_dir in [d for d in os.listdir("site") if re.match(r"[0-9]VWO", d)]:
        year_path = os.path.join("site", year_dir)
        if os.path.isdir(year_path):
            build_year_dir = os.path.join(build_dir, year_dir)
            os.makedirs(build_year_dir, exist_ok=True)

            for root, dirs, files in os.walk(year_path):
                for file in files:
                    if file.endswith(".md"):
                        md_file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(md_file_path, year_path)
                        build_path = os.path.join(
                            build_year_dir, os.path.splitext(relative_path)[0] + ".html"
                        )

                        os.makedirs(os.path.dirname(build_path), exist_ok=True)

                        with open(md_file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        if content.startswith("---"):
                            _, front_matter_str, markdown_content = content.split(
                                "---", 2
                            )
                            front_matter = yaml.safe_load(front_matter_str)
                        else:
                            front_matter = {}
                            markdown_content = content

                        html_content = md_processor.convert(markdown_content.strip())
                        html_content = remove_base64_images(html_content)

                        if front_matter.get("layout") == "summary":
                            template = template_env.get_template("summary.html")
                            page_path = os.path.relpath(md_file_path, "site").replace(
                                ".md", ""
                            )
                            rendered = template.render(
                                content=html_content,
                                page=front_matter,
                                page_path=page_path,
                                github_repo="gijs6/school.gijs6.nl",
                                site={"title": "Leermiddelenoverzicht"},
                            )
                        else:
                            rendered = f"<html><body>{html_content}</body></html>"

                        with open(build_path, "w", encoding="utf-8") as f:
                            f.write(rendered)


def main():
    print("Building with Binder...")

    build_dir = setup_build_directory()
    print(f"Build directory created: {build_dir}")

    template_env = Environment(loader=FileSystemLoader("site/templates"))
    print("Template environment set up")

    md_processor = setup_markdown_processor()
    print("Markdown processor ready")

    copy_static_assets(build_dir)
    print("Static assets copied")

    homepage_data = build_homepage_data()

    process_markdown_files(build_dir, template_env, md_processor)
    print("Markdown files processed")

    generate_feeds(build_dir, homepage_data, md_processor)
    print("RSS and Atom feeds generated")

    print(f"Build complete! Output in {build_dir}/")


if __name__ == "__main__":
    main()
