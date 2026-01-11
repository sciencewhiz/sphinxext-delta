import pytest
from sphinx.application import Sphinx
from sphinx import version_info


@pytest.mark.sphinx("html", testroot="basic")
def test_simple_short(app: Sphinx):
    app.build()

    content = read_text(app)

    html = '<h1>test<a class="headerlink" href="#test" title="Link to this heading">Â¶</a></h1>'

    assert html in content

def read_text(app: Sphinx):
    if version_info[:2] < (3, 0):
        return (app.outdir / "index.html").text().replace("\n", "")
    else:
        return (app.outdir / "index.html").read_text()