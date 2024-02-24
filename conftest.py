import pytest
import dotenv
import os
from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_endpoint import GetRequest
from data.operators import ru, ua, kz


@pytest.fixture()
def base_endpoint():
    return BaseEndpoint()


@pytest.fixture()
def get_endpoint():
    return GetRequest()


@pytest.fixture(scope='module')
def operators():
    return ru, ua, kz


@pytest.fixture()
def api_key():
    dotenv.load_dotenv()
    return os.getenv('BASE_API_KEY')
