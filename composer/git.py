import subprocess
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor


def _parse_first_commits():
    try:
        output = subprocess.check_output(
            ["git", "log", "--format=%ct", "--name-only", "--diff-filter=A"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}

    result = {}
    current_ts = None
    for line in output.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.isdigit():
            current_ts = int(line)
        elif current_ts:
            result[line] = current_ts
    return result


def _parse_last_commits():
    try:
        output = subprocess.check_output(
            ["git", "log", "--format=%ct", "--name-only"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}

    result = {}
    current_ts = None
    for line in output.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.isdigit():
            current_ts = int(line)
        elif current_ts and line not in result:
            result[line] = current_ts
    return result


def get_all_git_dates():
    try:
        with ThreadPoolExecutor(max_workers=2) as ex:
            f_first = ex.submit(_parse_first_commits)
            f_last = ex.submit(_parse_last_commits)
            first_commits = f_first.result()
            last_commits = f_last.result()

        git_dates = {}
        for filepath in set(first_commits) | set(last_commits):
            first_ts = first_commits.get(filepath)
            last_ts = last_commits.get(filepath)
            git_dates[filepath] = (
                datetime.fromtimestamp(first_ts, tz=timezone.utc) if first_ts else None,
                datetime.fromtimestamp(last_ts, tz=timezone.utc) if last_ts else None,
            )
        return git_dates

    except ValueError:
        return {}
