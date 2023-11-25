import pytest
from app import create_app, db
from flask_migrate import Migrate, upgrade, downgrade


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


@pytest.fixture(scope='session')
def test_app():
    app = create_app(TestConfig)
    Migrate(app, db)

    with app.app_context():
        upgrade()

        yield app

        downgrade()


@pytest.fixture(scope='session')
def test_client(test_app):
    return test_app.test_client()
