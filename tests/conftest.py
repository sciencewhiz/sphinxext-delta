import os
import pytest
from sphinx.application import Sphinx
from sphinx.testing.path import path


pytest_plugins = "sphinx.testing.fixtures"

os.environ.setdefault("READTHEDOCS_VERSION_NAME", "15")



@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture()
def content(app):
    app.build()
    yield app


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
