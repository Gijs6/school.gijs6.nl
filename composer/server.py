import errno
import io
import os
import subprocess
import sys
import threading
import time
import traceback
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from . import console, livereload
from .build import Site
from .config import BUILD_DEV_DIR, COMPOSER_DIR, SITE_DIR
from .content import DATA, PAGE, STATIC, TEMPLATE, classify, is_ignored, is_under

DEBOUNCE_SECONDS = 0.15
WATCHED_EVENTS = {"created", "modified", "deleted", "moved"}


class ChangeCollector(FileSystemEventHandler):
    def __init__(self):
        self.lock = threading.Lock()
        self.changed = threading.Event()
        self.paths = set()
        self.structural = False

    def on_any_event(self, event):
        if event.event_type not in WATCHED_EVENTS:
            return
        if event.is_directory and event.event_type in ("created", "modified"):
            return

        paths = {event.src_path}
        if event.event_type == "moved":
            paths.add(event.dest_path)
        paths = {os.path.relpath(os.fsdecode(path)) for path in paths}
        paths = {path for path in paths if not is_ignored(path)}
        if not paths:
            return

        with self.lock:
            self.paths |= paths
            self.structural |= event.is_directory
        self.changed.set()

    def wait(self):
        while True:
            self.changed.wait()
            while True:
                self.changed.clear()
                if not self.changed.wait(DEBOUNCE_SECONDS):
                    break
            with self.lock:
                paths, self.paths = self.paths, set()
                structural, self.structural = self.structural, False
            if paths:
                return sorted(paths), structural


def _restart():
    check = subprocess.run(
        [sys.executable, "-c", "import composer.__main__"],
        capture_output=True,
        text=True,
    )
    if check.returncode != 0:
        console.error("\nComposer changed, but it does not import. Not restarting:")
        print(check.stderr.strip() + "\n")
        return
    console.notice("\nComposer changed! Restarting process...\n")
    sys.stdout.flush()
    os.execv(sys.executable, sys.orig_argv)


def _describe(paths):
    names = ", ".join(os.path.basename(path) for path in paths[:3])
    if len(paths) > 3:
        names += f" and {len(paths) - 3} more"
    return names


def _apply_changes(site, paths, structural):
    if any(is_under(path, COMPOSER_DIR) and path.endswith(".py") for path in paths):
        _restart()

    kinds = {path: kind for path in paths if (kind := classify(path))}
    if not kinds and not structural:
        return False

    console.notice(f"\nChanged: {console.bold(_describe(paths))}")
    if structural or not site.complete:
        console.notice("Full rebuild...")
        site.build()
        return True

    started = time.perf_counter()
    all_pages = TEMPLATE in kinds.values()
    for path, kind in kinds.items():
        if kind == PAGE and all_pages and os.path.isfile(path):
            continue
        if kind in (PAGE, STATIC):
            _apply_file_change(site, path, kind)
    if all_pages:
        console.notice("Rebuilding all pages...")
        site.write_all_pages()
    elif PAGE in kinds.values() or DATA in kinds.values():
        site.write_indexes()
    console.success(f"Rebuilt in {console.elapsed_ms(started)}\n")
    return True


def _apply_file_change(site, path, kind):
    try:
        if not os.path.isfile(path):
            site.remove(path)
        elif kind == PAGE:
            site.write_page(path)
        else:
            site.copy_static(path)
    except Exception:
        console.error(f"Failed to rebuild {path}")
        traceback.print_exc()


def _watch(site, changes, live_reload):
    while True:
        paths, structural = changes.wait()
        try:
            if _apply_changes(site, paths, structural):
                live_reload.reload()
        except Exception:
            console.error("Rebuild failed")
            traceback.print_exc()
            print()


class DevRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, live_reload, **kwargs):
        self.live_reload = live_reload
        super().__init__(*args, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if urlsplit(self.path).path == livereload.PATH:
            self.live_reload.serve(self)
        else:
            super().do_GET()

    def send_head(self):
        url = urlsplit(self.path)
        path = self.translate_path(url.path)
        if os.path.isdir(path):
            if not url.path.endswith("/"):
                return super().send_head()
            path = os.path.join(path, "index.html")
        elif not os.path.isfile(path):
            path += ".html"

        if not os.path.isfile(path):
            return self._send_not_found()
        if path.endswith(".html"):
            return self._send_html(path)
        return super().send_head()

    def _send_html(self, path, status=200):
        with open(path, "rb") as page:
            body = livereload.inject(page.read())
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return io.BytesIO(body)

    def _send_not_found(self):
        not_found = os.path.join(self.directory, "404.html")
        if os.path.isfile(not_found):
            return self._send_html(not_found, status=404)
        self.send_error(404, "File not found")
        return None


def _bind(port, handler):
    for candidate in range(port, port + 100):
        try:
            return ThreadingHTTPServer(("0.0.0.0", candidate), handler)
        except OSError as exc:
            if exc.errno != errno.EADDRINUSE:
                raise
    raise SystemExit(f"composer: no free port in {port}-{port + 99}")


def serve(port=8000, dev=False):
    console.title("Server")

    changes = ChangeCollector()
    observer = Observer()
    observer.schedule(changes, SITE_DIR, recursive=True)
    observer.schedule(changes, COMPOSER_DIR, recursive=True)
    observer.start()

    site = Site(BUILD_DEV_DIR, dev=dev)
    try:
        site.build()
    except Exception:
        console.error("Initial build failed, fix the error and save to retry")
        traceback.print_exc()
        print()

    live_reload = livereload.LiveReload()
    threading.Thread(
        target=_watch, args=(site, changes, live_reload), daemon=True
    ).start()

    handler = partial(
        DevRequestHandler, directory=BUILD_DEV_DIR, live_reload=live_reload
    )
    server = _bind(port, handler)
    console.success(
        f"Serving on {console.bold(f'http://localhost:{server.server_port}')}"
    )
    console.notice("Watching for changes...")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        console.error("\nStopping server...")
    finally:
        observer.stop()
        server.server_close()
        observer.join()
