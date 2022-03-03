import pytest
from desafio import create_app


@pytest.fixture()
def app():
    return create_app(test_config=True)
