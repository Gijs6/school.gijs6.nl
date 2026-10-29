import subprocess
from datetime import UTC, datetime

COMMIT_MARKER = "@"


def _git(*args):
    try:
        return subprocess.check_output(
            ["git", "-c", "core.quotePath=false", *args],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def head_commit():
    sha = _git("rev-parse", "HEAD").strip()
    return {"sha": sha, "short": sha[:7]} if sha else None


def file_history():
    created = {}
    updated = {}
    renamed_to = {}
    moment = None
    log = _git("log", "-M", f"--format={COMMIT_MARKER}%ct", "--name-status")
    for line in log.splitlines():
        if line.startswith(COMMIT_MARKER) and line[1:].isdigit():
            moment = datetime.fromtimestamp(int(line[1:]), tz=UTC)
            continue
        if not line or moment is None:
            continue
        status, *paths = line.split("\t")
        path = renamed_to.get(paths[-1], paths[-1])
        if status.startswith("R"):
            renamed_to[paths[0]] = path
        updated.setdefault(path, moment)
        created[path] = moment
    return {path: (created[path], updated[path]) for path in updated}
