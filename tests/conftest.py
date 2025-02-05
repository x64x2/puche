"""Common test stuff.
"""

import os
from pathlib import Path

from pytest import fixture

from logicgrid import __version__


def pytest_report_header(config):
    return f"package: puche, version {__version__}"


@fixture(autouse=True)
def setup(monkeypatch):
    "Global test setup."

    # Run tests from this directory.
    path = os.path.dirname(__file__)
    monkeypatch.chdir(path)


@fixture(scope="session")
def demodir():
    "Return directory containing demo files."
    return Path("../demo")
