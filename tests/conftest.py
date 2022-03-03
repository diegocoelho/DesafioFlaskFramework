import pytest
from desafio import create_app


@pytest.fixture(scope='module')
def app():
    return create_app(test_config=True)