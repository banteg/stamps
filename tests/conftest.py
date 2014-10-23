import pytest


@pytest.fixture(scope='session')
def db():
    from pymongo import MongoClient
    mongo = MongoClient()
    return mongo.stamps


@pytest.fixture(scope='session')
def app():
    from stamps.app import create_app
    app = create_app('testing')
    return app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def context(app):
    return app.test_request_context()
