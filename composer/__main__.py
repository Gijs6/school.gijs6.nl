import argparse

from colorama import just_fix_windows_console

from .build import Site
from .config import BUILD_DIR
from .server import serve


def main():
    parser = argparse.ArgumentParser(
        prog="composer",
        description="Composer - Static site generator for school summaries",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="build",
        choices=["build", "serve"],
        help="Command to run (default: build)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for server (default: 8000)",
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Development mode: list hidden pages on the index pages",
    )
    args = parser.parse_args()

    just_fix_windows_console()
    if args.command == "serve":
        serve(args.port, dev=args.dev)
    else:
        Site(BUILD_DIR, dev=args.dev).build()


if __name__ == "__main__":
    main()
