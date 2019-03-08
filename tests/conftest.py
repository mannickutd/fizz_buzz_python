import pytest
from fizz_buzz_python import create_app


@pytest.fixture
def async_app(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app)), app
