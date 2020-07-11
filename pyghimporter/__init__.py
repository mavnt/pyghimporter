import inspect
import os
import os.path
import pathlib
import subprocess
import sys
import urllib.request


def import_failed(exec_cmd: str):
    try:
        exec(exec_cmd)
    except ModuleNotFoundError:
        return True
    return False


def github(
    user: str,
    module: str,
    commit_or_branch: str = "master",
    exec_cmd: str = None,
    force=False,
):
    if not exec_cmd:
        exec_cmd = f"import {module}"
    gh_path = f"github.com/{user}/{module}/archive/"
    dir_ = f"/tmp/{gh_path}"
    path = f"{dir_}{commit_or_branch}.zip"
    if force or import_failed(exec_cmd):
        pathlib.Path(dir_).mkdir(parents=True, exist_ok=True)
        if force or not os.path.isfile(path):
            urllib.request.urlretrieve(
                f"https://{gh_path}{commit_or_branch}.zip",
                f"/tmp/{gh_path}{commit_or_branch}.zip",
            )
        subprocess.check_call([sys.executable, "-m", "pip", "install", path])
    frame = inspect.currentframe()
    exec(exec_cmd, globals(), frame.f_back.f_locals)


__all__ = [github]
