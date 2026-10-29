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
    moment = None
    for line in _git("log", f"--format={COMMIT_MARKER}%ct", "--name-only").splitlines():
        if line.startswith(COMMIT_MARKER) and line[1:].isdigit():
            moment = datetime.fromtimestamp(int(line[1:]), tz=UTC)
        elif line and moment:
            updated.setdefault(line, moment)
            created[line] = moment
    return {path: (created[path], updated[path]) for path in updated}
