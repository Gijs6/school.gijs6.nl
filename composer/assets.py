import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import SITE_DIR
from .utils import get_year_dirs


def copy_if_exists(src, dest):
    if not os.path.exists(src):
        return 0
    if os.path.isdir(src):
        shutil.copytree(src, dest)
        return sum(len(files) for _, _, files in os.walk(dest))
    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(src, dest)
    return 1


def collect_static_assets(build_dir):
    tasks = [
        ("site/assets", os.path.join(build_dir, "assets")),
        ("site/.well-known", os.path.join(build_dir, ".well-known")),
        ("site/robots.txt", os.path.join(build_dir, "robots.txt")),
        ("CNAME", os.path.join(build_dir, "CNAME")),
    ]

    for year_dir in get_year_dirs():
        year_path = os.path.join(SITE_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue
        build_year_dir = os.path.join(build_dir, year_dir)
        for root, _, files in os.walk(year_path):
            for file in (f for f in files if not f.endswith(".md")):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(
                    build_year_dir, os.path.relpath(src_file, year_path)
                )
                tasks.append((src_file, dest_file))

    return tasks


def copy_static_assets(build_dir, progress=None):
    tasks = collect_static_assets(build_dir)
    with ThreadPoolExecutor(max_workers=min(16, (os.cpu_count() or 4) * 2)) as ex:
        futures = [ex.submit(copy_if_exists, src, dest) for src, dest in tasks]
        for _ in as_completed(futures):
            if progress:
                progress.update()
    return len(tasks)
