import pytest

from pyhabbo._http import HTTPTransport
from pyhabbo.client import HabboClient
from pyhabbo.hotels import Hotel


@pytest.fixture
def base_url() -> str:
    return Hotel.COM.base_url


@pytest.fixture
def transport(base_url: str) -> HTTPTransport:
    return HTTPTransport(base_url)


@pytest.fixture
def client() -> HabboClient:
    return HabboClient(hotel=Hotel.COM)
