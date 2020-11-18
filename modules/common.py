import os
import subprocess
from subprocess import check_call
import platform

import modules.config as c
import modules.functions as f


def run_task_build():
    f.remove_dir("build")
    f.create_dir("build")

    build_dir = os.path.join("build")

    # generate cmake data
    cwd = build_dir
    command = " ".join(
        [
            "cmake",
            "../",
        ]
    )
    check_call(command, cwd=cwd, shell=True)

    # build
    cwd = build_dir
    command = " ".join(
        [
            "cmake",
            "--build",
            ".",
        ]
    )
    check_call(command, cwd=cwd, shell=True)


def run_task_test():
    is_windows = any(platform.win32_ver())
    extension = ".exe" if is_windows else ""

    build_dir = os.path.join("src", "python")

    # run
    cwd = build_dir
    command = " ".join(["./../../build/pybind11_test{0}".format(extension)])
    check_call(command, cwd=cwd, shell=True)


def run_task_format():
    # check
    try:
        subprocess.check_output(["black", "--version"])
    except OSError:
        f.error("Black is not installed, check: https://github.com/psf/black")

    # start
    f.debug("Formating...")

    # make.py
    command = " ".join(
        [
            "black",
            "make.py",
        ]
    )
    check_call(command, shell=True)

    # modules
    command = " ".join(
        [
            "black",
            "modules/",
        ]
    )
    check_call(command, shell=True)

    # src / python
    command = " ".join(
        [
            "black",
            "src/python/",
        ]
    )
    check_call(command, shell=True)

    f.debug("Finished")
