import pytest

from pyhabbo._http import HTTPTransport
from pyhabbo.client import HabboClient
from pyhabbo.hotels import Hotel


@pytest.fixture
def base_url() -> str:
    return Hotel.COM


@pytest.fixture
def transport(base_url: str):
    t = HTTPTransport(base_url)
    yield t
    t.close()


@pytest.fixture
def client() -> HabboClient:
    return HabboClient(hotel=Hotel.COM)
