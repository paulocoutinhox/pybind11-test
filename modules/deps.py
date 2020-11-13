import os
import subprocess
from subprocess import check_call

import modules.config as c
import modules.functions as f


def run_task_pybind11():
    f.remove_dir("pybind11")
    f.create_dir("pybind11")

    # clone
    cwd = None
    command = " ".join(["git", "clone", "https://github.com/pybind/pybind11.git"])
    check_call(command, cwd=cwd, shell=True)

    # reset to commit
    cwd = os.path.join("pybind11")
    command = " ".join(
        [
            "git",
            "reset",
            "--hard",
            c.pybind11_git_commit,
        ]
    )
    check_call(command, cwd=cwd, shell=True)


def run_task_python():
    f.remove_dir("python")
    f.create_dir("python")

    # clone
    cwd = None
    command = " ".join(
        [
            "git",
            "clone",
            "--branch",
            c.python_version,
            "https://github.com/python/cpython.git",
            "python",
        ]
    )
    check_call(command, cwd=cwd, shell=True)

    # configure
    cwd = os.path.join("python")
    command = " ".join(
        [
            "./configure",
            "--enable-optimizations",
        ]
    )
    check_call(command, cwd=cwd, shell=True)

    # build
    cwd = os.path.join("python")
    command = " ".join(
        [
            "make",
            "-j",
            "8",
        ]
    )
    check_call(command, cwd=cwd, shell=True)
