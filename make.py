#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Make tool

Usage:
  make.py run <task-name>
  make.py [options]
  make.py -h | --help  

Options:
  -h --help                         Show this screen.
  -d --debug                        Enable debug mode.
  
Examples:
  python make.py -h

Tasks:
  - build
  - test
  - format  
  - dep-pybind11
  - dep-python
"""

from docopt import docopt

import modules.common as common
import modules.deps as deps
import modules.functions as f
import modules.config as c


def main(options):
    # show all params for debug
    if ("--debug" in options and options["--debug"]) or (
        "-d" in options and options["-d"]
    ):
        c.make_debug = True

    if c.make_debug:
        f.debug("You have executed with options:")
        f.message(str(options))
        f.message("")

    # bind options
    if "<task-name>" in options:
        make_task = options["<task-name>"]

    # validate data
    f.debug("Validating data...")

    # validate task
    if not make_task:
        f.error("Task is invalid")

    # build
    if make_task == "build":
        common.run_task_build()

    # format code
    elif make_task == "format":
        common.run_task_format()

    # test
    elif make_task == "test":
        common.run_task_test()

    # download dep pybind11
    elif make_task == "dep-pybind11":
        deps.run_task_pybind11()

    # download dep python
    elif make_task == "dep-python":
        deps.run_task_python()

    #######################
    # Invalid
    #######################

    # invalid
    else:
        f.error("Task is invalid")

    f.message("")
    f.debug("FINISHED!")


if __name__ == "__main__":
    # main CLI entrypoint
    args = docopt(__doc__, version="1.0.0")
    main(args)
