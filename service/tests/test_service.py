from service import __version__
from service.run import app


def test_version():
    assert __version__ == '0.1.0'

def test_run():
    assert app != None

def test_app(app):
    assert app.name == 'service'
