import pytest
from desafio import create_app
from desafio.database import db


@pytest.fixture(scope='session')
def app():
    app = create_app(test_config=True)
    db.app = app
    db.init_app(app)
    db.create_all()
    return app
