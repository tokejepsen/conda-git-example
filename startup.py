import subprocess

from conda_git_deployment import utils


if not utils.check_module("PySide"):
    subprocess.call(["pip", "install", "PySide"])

import PySide
