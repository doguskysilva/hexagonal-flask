import pytest
from flask import Flask
from hexagonal_flask.server import create_app


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        pass

    yield app


@pytest.fixture
def client(app: Flask):
    return app.test_client()
