#!/usr/bin/env python3

import sys
import shutil
import subprocess

import setuptools


def __get_long_description():
    fallback = True
    if shutil.which("pandoc"):
        try:
            proc = subprocess.Popen(["pandoc", "-t", "rst", "README.org"],
                                    stdout=subprocess.PIPE)
            stdout, _ = proc.communicate()
            long_description = stdout.decode("utf8")
        except OSError:
            sys.stderr.write(
                "Warning: Error while converting with README.org with pandoc.\n"
                "         Falling back to literal blocks for the README.rst.\n")
        else:
            fallback = False
    else:
        sys.stderr.write(
            "Warning: pandoc not found.\n"
            "         In a debian system you can install pandoc with:\n"
            "             sudo apt install pandoc\n"
            "         Falling back to literal blocks for the README.rst.\n")

    if fallback:
        with open("README.org") as fp:
            readme_lines = fp.readlines()

        long_description = f"::\n\n  {'  '.join(readme_lines)}\n"

    return long_description


setuptools.setup(
    long_description=__get_long_description(),
    long_description_content_type="text/x-rst",
)
