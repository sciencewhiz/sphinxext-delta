import os
import pytest
from sphinx.application import Sphinx
from sphinx.testing.path import path


pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(autouse=True)
def set_rtd_env(monkeypatch):
    monkeypatch.setenv("READTHEDOCS_VERSION_NAME", "17")
    monkeypatch.setenv("READTHEDOCS", "True")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "pull_request")


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture()
def content(app):
    app.build()
    yield app


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
