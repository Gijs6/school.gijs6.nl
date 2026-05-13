import os
import sys
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from colorama import Fore, Style
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .config import SITE_DIR, BUILD_DIR, BUILD_DEV_DIR
from .build import build, rebuild_single_markdown


class BuildHandler(FileSystemEventHandler):
    def __init__(self, build_func, build_dir):
        self.build_func = build_func
        self.build_dir = build_dir
        self.last_build = 0

    def on_modified(self, event):
        if event.is_directory or "build" in event.src_path:
            return
        now = time.time()
        if now - self.last_build < 0.5:
            return
        self.last_build = now

        src_path = event.src_path

        if src_path.endswith(".py"):
            print(
                f"\n{Fore.YELLOW}Composer changed! Restarting process...{Style.RESET_ALL}\n"
            )
            os.execv(sys.executable, [sys.executable] + sys.argv)

        filename = os.path.basename(src_path)
        print(f"\n{Fore.YELLOW}Changed: {Style.BRIGHT}{filename}{Style.RESET_ALL}")

        if src_path.endswith(".md") and SITE_DIR in src_path:
            if rebuild_single_markdown(src_path, self.build_dir):
                return

        print(f"{Fore.CYAN}Full rebuild...{Style.RESET_ALL}")
        self.build_func()


class BuildHTTPServer(SimpleHTTPRequestHandler):
    directory = BUILD_DIR

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=self.directory, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)

        if self.path.endswith("/") or self.path == "":
            index_path = os.path.join(path, "index.html")
            if os.path.isfile(index_path):
                self.path = (
                    self.path.rstrip("/") + "/index.html"
                    if not self.path.endswith("index.html")
                    else self.path
                )
                return super().do_GET()

        if os.path.isfile(path):
            return super().do_GET()

        if not self.path.endswith("/") and "." not in os.path.basename(self.path):
            html_path = path + ".html"
            if os.path.isfile(html_path):
                self.path += ".html"
                return super().do_GET()

        not_found_path = os.path.join(self.directory, "404.html")
        if os.path.isfile(not_found_path):
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(not_found_path, "rb") as f:
                self.wfile.write(f.read())
            return

        self.send_error(404, "File not found")


def serve(port=8000, dev=False):
    print(f"{Fore.BLUE}Server{Style.RESET_ALL}\n")

    build(dev, output_dir=BUILD_DEV_DIR)

    observer = Observer()
    handler = BuildHandler(lambda: build(dev, output_dir=BUILD_DEV_DIR), BUILD_DEV_DIR)
    observer.schedule(handler, SITE_DIR, recursive=True)
    observer.schedule(handler, ".", recursive=False)
    observer.start()

    class DevHTTPServer(BuildHTTPServer):
        directory = BUILD_DEV_DIR

    server = HTTPServer(("0.0.0.0", port), DevHTTPServer)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    print(
        f"{Fore.GREEN}Serving on {Style.BRIGHT}http://localhost:{port}{Style.RESET_ALL}"
    )
    print(f"{Fore.MAGENTA}Watching for changes...{Style.RESET_ALL}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Stopping server...{Style.RESET_ALL}")
        observer.stop()
        server.shutdown()
        observer.join()
