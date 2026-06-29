import httpx
import pytest
import respx

from pyhabbo._http import HTTPTransport
from pyhabbo.client import HabboClient
from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError
from pyhabbo.hotels import Hotel


@respx.mock
def test_request_returns_json(base_url: str) -> None:
    respx.get(f"{base_url}/api/public/ping").respond(json={"ok": True})

    transport = HTTPTransport(base_url)
    try:
        assert transport.request("GET", "/ping") == {"ok": True}
    finally:
        transport.close()


@respx.mock
def test_request_returns_none_for_empty_body(base_url: str) -> None:
    respx.get(f"{base_url}/api/public/ping").respond(status_code=200, content=b"")

    transport = HTTPTransport(base_url)
    try:
        assert transport.request("GET", "/ping") is None
    finally:
        transport.close()


@respx.mock
def test_request_raises_not_found_with_parsed_errors(base_url: str) -> None:
    respx.get(f"{base_url}/api/public/users/invalid").respond(
        status_code=404,
        json={"errors": [{"param": "id", "msg": "user.invalid_id", "value": "invalid"}]},
    )

    transport = HTTPTransport(base_url)
    try:
        with pytest.raises(NotFoundError) as exc_info:
            transport.request("GET", "/users/invalid")
    finally:
        transport.close()

    assert exc_info.value.status_code == 404
    assert exc_info.value.errors[0].msg == "user.invalid_id"


@respx.mock
def test_request_raises_bad_request(base_url: str) -> None:
    respx.get(f"{base_url}/api/public/users").respond(
        status_code=400,
        json={"errors": [{"param": "name", "msg": "user.missing_name"}]},
    )

    transport = HTTPTransport(base_url)
    try:
        with pytest.raises(BadRequestError):
            transport.request("GET", "/users")
    finally:
        transport.close()


@respx.mock
def test_request_raises_habbo_api_error_for_other_status_codes(base_url: str) -> None:
    respx.get(f"{base_url}/api/public/ping").respond(status_code=503, json={"errors": []})

    transport = HTTPTransport(base_url)
    try:
        with pytest.raises(HabboAPIError) as exc_info:
            transport.request("GET", "/ping")
    finally:
        transport.close()

    assert exc_info.value.status_code == 503


def test_transport_closes_owned_client(base_url: str) -> None:
    transport = HTTPTransport(base_url)
    owned_client = transport._client

    transport.close()

    assert owned_client.is_closed


def test_transport_does_not_close_injected_client(base_url: str) -> None:
    http_client = httpx.Client(base_url=base_url)
    transport = HTTPTransport(base_url, client=http_client)

    transport.close()

    assert not http_client.is_closed
    http_client.close()


@respx.mock
def test_client_ping() -> None:
    respx.get(f"{Hotel.COM.base_url}/api/public/ping").respond(status_code=200, content=b"")

    with HabboClient(hotel=Hotel.COM) as client:
        client.ping()
