import shutil
import sys
import time

from colorama import Fore, Style


def _paint(color, text):
    return f"{color}{text}{Style.RESET_ALL}"


def title(text):
    print(_paint(Fore.CYAN, text))
    print()


def step(text):
    print(_paint(Fore.BLUE, text))


def detail(text):
    print(f"  {text}")


def success(text):
    print(_paint(Fore.GREEN, text))


def notice(text):
    print(_paint(Fore.YELLOW, text))


def error(text):
    print(_paint(Fore.RED, text))


def bold(text):
    return f"{Style.BRIGHT}{text}{Style.NORMAL}"


def elapsed_ms(started):
    return f"{(time.perf_counter() - started) * 1000:.0f}ms"


class ProgressBar:
    def __init__(self, total, label, width=25):
        self.total = max(total, 1)
        self.count = 0
        self.label = label[:10]
        self.width = width
        self.started = time.perf_counter()
        self.interactive = sys.stdout.isatty()

    def advance(self):
        self.count += 1
        if self.interactive:
            self._write(self._bar())

    def finish(self):
        done = _paint(Fore.GREEN, "done")
        line = (
            f"  {self.label:10} {done} ({self.count} items, {elapsed_ms(self.started)})"
        )
        self._write(line + "\n")

    def _bar(self):
        columns = shutil.get_terminal_size((80, 24)).columns
        width = max(5, min(self.width, columns - 31))
        filled = int(width * min(self.count / self.total, 1.0))
        bar = ("=" * filled + ">").ljust(width)[:width]
        seconds = time.perf_counter() - self.started
        return f"  {self.label:10} [{bar}] {self.count:>3}/{self.total:<3} ({seconds:.1f}s)"

    def _write(self, line):
        if self.interactive:
            line = "\r\x1b[K" + line
        sys.stdout.write(line)
        sys.stdout.flush()
