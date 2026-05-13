import argparse
from .build import build
from .server import serve

parser = argparse.ArgumentParser(
    description="Composer - Static site generator for school summaries"
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
    help="Enable development mode (include hidden pages)",
)

args = parser.parse_args()

if args.command == "serve":
    serve(args.port, dev=args.dev)
else:
    build(dev=args.dev)
