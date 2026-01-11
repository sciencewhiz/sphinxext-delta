import pytest
from sphinx.application import Sphinx
import os


pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "roots"))


@pytest.fixture()
def content(app):
    app.build()
    yield app


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
