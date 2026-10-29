import contextlib
import multiprocessing
import os
import shutil
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

from . import console
from .config import BUILD_DIR, ONDERBOUW_DIR, SITE_DIR, TEMPLATES_DIR
from .content import (
    ONDERBOUW,
    SUMMARY,
    load_page,
    load_pages,
    load_resources,
    output_path,
    static_sources,
    year_dirs,
)
from .feeds import write_feeds
from .git import file_history
from .listing import onderbouw_listing, summary_listing
from .render import Renderer, site_context
from .sitemap import write_sitemap

_worker_renderer = None


def _start_worker(context, history):
    global _worker_renderer
    _worker_renderer = Renderer(context, history)


def _render_in_worker(page, output_dir):
    content, rendered = _worker_renderer.page(page)
    write_text(output_dir, page.output, rendered)
    return page.url, content


def _process_pool(context, history):
    methods = multiprocessing.get_all_start_methods()
    method = "forkserver" if "forkserver" in methods else "spawn"
    return ProcessPoolExecutor(
        max_workers=min(8, os.cpu_count() or 4),
        mp_context=multiprocessing.get_context(method),
        initializer=_start_worker,
        initargs=(context, history),
    )


def write_text(output_dir, relative_path, text):
    path = os.path.join(output_dir, relative_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    temp_path = f"{path}.{os.getpid()}-{threading.get_ident()}.tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(temp_path, path)


def copy_file(source, output_dir):
    destination = os.path.join(output_dir, output_path(source))
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy2(source, destination)


def _count(pages, kind):
    return sum(page.kind == kind for page in pages)


class Site:
    def __init__(self, output_dir=BUILD_DIR, dev=False):
        self.output_dir = output_dir
        self.dev = dev
        self.complete = False
        self.context = None
        self.history = {}
        self.renderer = None

    def refresh(self):
        self.context = site_context()
        self.history = file_history()
        self.renderer = Renderer(self.context, self.history)

    def build(self):
        started = time.perf_counter()
        self.complete = False
        console.title("Composer")

        console.step("[1/6] Setup")
        self.refresh()
        commit = self.context["commit"]
        console.detail(
            f"Loaded {self.renderer.template_count()} templates from {TEMPLATES_DIR}/"
        )
        console.detail(f"Read git history for {len(self.history)} files")
        console.detail(
            f"Deploy stamp: {self.context['built_at']}"
            f" ({commit['short'] if commit else 'no commit'})"
        )
        print()

        staging_dir = self._scratch_dir("staging")
        os.makedirs(staging_dir)
        try:
            self._build_into(staging_dir)
        except BaseException:
            shutil.rmtree(staging_dir, ignore_errors=True)
            raise

        console.step("Finalizing")
        self._publish(staging_dir)
        console.detail(f"Moved build to {self.output_dir}/")
        print()

        self.complete = True
        console.success(f"Build complete in {console.elapsed_ms(started)}")
        print()

    def _build_into(self, output_dir):
        console.step("[2/6] Copying static assets")
        self._copy_static(output_dir)
        print()

        console.step("[3/6] Rendering pages")
        pages = load_pages()
        console.detail(
            f"Found {_count(pages, SUMMARY)} summaries in"
            f" {', '.join(year_dirs(SITE_DIR))}"
        )
        console.detail(
            f"Found {_count(pages, ONDERBOUW)} onderbouw pages in"
            f" {', '.join(year_dirs(ONDERBOUW_DIR))}"
        )
        contents = self._render_pages(pages, output_dir)
        print()

        console.step("[4/6] Rendering indexes")
        self.write_indexes(pages, output_dir)
        console.detail("Wrote index.html, onderbouw/index.html and 404.html")
        print()

        console.step("[5/6] Generating feeds")
        public_listing = summary_listing(pages, load_resources())
        entries = write_feeds(output_dir, public_listing, contents, self.history)
        console.detail(f"Wrote rss.xml and atom.xml with {entries} entries")
        print()

        console.step("[6/6] Generating sitemap")
        urls = write_sitemap(output_dir, pages, self.history)
        console.detail(f"Wrote sitemap.xml with {urls} urls")
        print()

    def _copy_static(self, output_dir):
        sources = list(static_sources())
        progress = console.ProgressBar(len(sources), "Copying")
        with ThreadPoolExecutor(max_workers=min(16, (os.cpu_count() or 4) * 2)) as ex:
            futures = [ex.submit(copy_file, source, output_dir) for source in sources]
            for future in as_completed(futures):
                future.result()
                progress.advance()
        progress.finish()

    def _render_pages(self, pages, output_dir):
        contents = {}
        progress = console.ProgressBar(len(pages), "Pages")
        with _process_pool(self.context, self.history) as pool:
            futures = [
                pool.submit(_render_in_worker, page, output_dir) for page in pages
            ]
            for future in as_completed(futures):
                url, content = future.result()
                contents[url] = content
                progress.advance()
        progress.finish()
        return contents

    def _scratch_dir(self, purpose):
        parent = os.path.dirname(os.path.abspath(self.output_dir))
        path = os.path.join(parent, f".{os.path.basename(self.output_dir)}.{purpose}")
        shutil.rmtree(path, ignore_errors=True)
        return path

    def _publish(self, staging_dir):
        old_dir = self._scratch_dir("old")
        if os.path.exists(self.output_dir):
            os.rename(self.output_dir, old_dir)
        os.rename(staging_dir, self.output_dir)
        shutil.rmtree(old_dir, ignore_errors=True)

    def write_indexes(self, pages=None, output_dir=None):
        pages = load_pages() if pages is None else pages
        output_dir = output_dir or self.output_dir
        listing = summary_listing(pages, load_resources(), include_hidden=self.dev)
        write_text(output_dir, "index.html", self.renderer.home(listing))
        write_text(
            output_dir,
            os.path.join("onderbouw", "index.html"),
            self.renderer.onderbouw(onderbouw_listing(pages, include_hidden=self.dev)),
        )
        write_text(output_dir, "404.html", self.renderer.not_found())

    def write_page(self, source):
        page = load_page(source)
        _, rendered = self.renderer.page(page)
        write_text(self.output_dir, page.output, rendered)

    def write_all_pages(self):
        pages = load_pages()
        self._render_pages(pages, self.output_dir)
        self.write_indexes(pages)

    def copy_static(self, source):
        copy_file(source, self.output_dir)

    def remove(self, source):
        with contextlib.suppress(FileNotFoundError):
            os.remove(os.path.join(self.output_dir, output_path(source)))
