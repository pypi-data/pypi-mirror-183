#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Helps installing Ginggar. See documentation.
"""

import os
import sys
import subprocess
import typing as t
import uuid


def find_install_dirs() -> t.Tuple[str, str]:
    _install_dir = os.path.abspath(__file__)
    install_dir = None
    while not install_dir:
        for cnd in [_install_dir, f"{_install_dir}/ginggar"]:
            if os.path.isfile(f"{cnd}/main/views.py"):
                install_dir = _install_dir
                break
        if install_dir:
            break
        _ninstalldir = os.path.dirname(_install_dir)
        if _install_dir == _ninstalldir:
            raise RuntimeError("installation directory not found")
        _install_dir = _ninstalldir
    inner_install_dir = install_dir = os.path.realpath(install_dir)
    if os.path.isdir(f"{install_dir}/ginggar"):
        inner_install_dir = os.path.realpath(f"{install_dir}/ginggar")
    return install_dir, inner_install_dir


def find_managecmd(install_dir: str) -> str:
    if os.path.exists(f"{install_dir}/manage.py"):
        return f"{install_dir}/manage.py"
    else:
        return f"{install_dir}/_meta/manage.py"


def generate_settingslocalpy(runtime_dir: str) -> str:
    return f"""
    DEBUG = True  # required also for static files delivery in dev server (for any reason)
    SECRET_KEY = "{uuid.uuid4()}-{uuid.uuid4()}-{uuid.uuid4()}"
    STATIC_ROOT = "{runtime_dir}/static"

    import os
    if "GINGGAR_DB_ENGINE" in os.environ:  # mostly for container images
        _db = {{}}
        for k in os.environ:
            if k.startswith("GINGGAR_DB_"):
                _db[k[10:]] = os.environ[k]
        DATABASES = {{ "default": _db }}
    else:
        DATABASES = {{
            "default": {{
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "{runtime_dir}/ginggar-db-v1",
            }}
        }}
    """


def main() -> None:
    if len(sys.argv) == 1:
        raise Exception(f"""Usage:

        $ {os.path.basename(sys.argv[0])} [command] ... ...

    For more information, please read the Ginggar documentation.
        """)
    command = sys.argv[1]
    install_dir, inner_install_dir = find_install_dirs()
    managecmd = find_managecmd(install_dir)
    if command in ["setup", "init", "update"]:
        if command == "setup":
            runtime_dir = os.path.abspath(os.path.expandvars(sys.argv[2])).replace("\\", "/")
            os.makedirs(runtime_dir, exist_ok=True)
            os.chdir(inner_install_dir)
            with open(f"{inner_install_dir}/settings_local.py", "w") as f:
                f.write(generate_settingslocalpy(runtime_dir))
        if command in ["setup", "init"]:
            subprocess.call([sys.executable, managecmd, "makemigrations", "main"])
        subprocess.call([sys.executable, managecmd, "collectstatic", "--noinput"])
        subprocess.call([sys.executable, managecmd, "makemigrations"])
        subprocess.call([sys.executable, managecmd, "migrate"])
    elif command == "runserver":
        subprocess.call([sys.executable, managecmd, "runserver"])
    else:
        raise Exception(f"unknown command: {command}")


if __name__ == "__main__":
    main()
