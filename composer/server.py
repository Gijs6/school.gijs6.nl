import errno
import os
import sys
import threading
import time
import traceback
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, urlunsplit

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from . import console
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
        paths = {os.path.relpath(os.fsdecode(event.src_path))}
        if event.event_type == "moved":
            paths.add(os.path.relpath(os.fsdecode(event.dest_path)))

        with self.lock:
            if event.is_directory:
                if event.event_type == "created" or event.event_type == "modified":
                    return
                self.structural = True
            else:
                paths = {path for path in paths if not is_ignored(path)}
                if not paths:
                    return
            self.paths |= paths
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
    console.notice("\nComposer changed! Restarting process...\n")
    sys.stdout.flush()
    os.execv(sys.executable, [sys.executable, *sys.argv])


def _describe(paths):
    names = ", ".join(os.path.basename(path) for path in paths[:3])
    if len(paths) > 3:
        names += f" and {len(paths) - 3} more"
    return names


def _apply_changes(site, paths, structural):
    if any(is_under(path, COMPOSER_DIR) and path.endswith(".py") for path in paths):
        _restart()

    console.notice(f"\nChanged: {console.bold(_describe(paths))}")
    if structural or not site.complete:
        console.notice("Full rebuild...")
        site.build()
        return

    started = time.perf_counter()
    kinds = {path: classify(path) for path in paths}
    if TEMPLATE in kinds.values():
        console.notice("Rebuilding all pages...")
        site.write_all_pages()
    else:
        for path, kind in kinds.items():
            if kind in (PAGE, STATIC):
                _apply_file_change(site, path, kind)
        if PAGE in kinds.values() or DATA in kinds.values():
            site.write_indexes()
    console.success(f"Rebuilt in {console.elapsed_ms(started)}\n")


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


def _watch(site, changes):
    while True:
        paths, structural = changes.wait()
        try:
            _apply_changes(site, paths, structural)
        except Exception:
            console.error("Rebuild failed")
            traceback.print_exc()
            print()


class DevRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):
        url = urlsplit(self.path)
        path = self.translate_path(url.path)
        if os.path.isdir(path):
            if os.path.isfile(os.path.join(path, "index.html")):
                return super().send_head()
        elif os.path.isfile(path):
            return super().send_head()
        elif os.path.isfile(path + ".html"):
            self.path = urlunsplit(url._replace(path=url.path + ".html"))
            return super().send_head()
        return self._send_not_found()

    def _send_not_found(self):
        not_found = os.path.join(self.directory, "404.html")
        if not os.path.isfile(not_found):
            self.send_error(404, "File not found")
            return None
        page = open(not_found, "rb")
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(os.fstat(page.fileno()).st_size))
        self.end_headers()
        return page


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

    site = Site(BUILD_DEV_DIR, dev=dev)
    try:
        site.build()
    except Exception:
        console.error("Initial build failed, fix the error and save to retry")
        traceback.print_exc()
        print()

    changes = ChangeCollector()
    observer = Observer()
    observer.schedule(changes, SITE_DIR, recursive=True)
    observer.schedule(changes, COMPOSER_DIR, recursive=True)
    observer.start()
    threading.Thread(target=_watch, args=(site, changes), daemon=True).start()

    server = _bind(port, partial(DevRequestHandler, directory=BUILD_DEV_DIR))
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
