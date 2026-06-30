import json
from pathlib import Path

import pytest
import respx

from pyhabbo import HabboClient
from pyhabbo.exceptions import NotFoundError

FIXTURES_DIR = Path(__file__).parent / "fixtures"
ROOM_ID = 72631843


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@pytest.fixture
def room_id() -> int:
    return ROOM_ID


@respx.mock
def test_get(base_url: str, client: HabboClient, room_id: int) -> None:
    respx.get(f"{base_url}/api/public/rooms/{room_id}").respond(json=load_fixture("room.json"))

    room = client.rooms.get(room_id)

    assert room.name == "simba, cedie, queenie, moana & goldie"
    assert room.owner_name == "AaronChristian"
    assert room.door_mode == "closed"
    assert room.habbo_group_id == "g-hhus-fede0165b511d8ed7d956a749f1001e3"


@respx.mock
def test_get_with_string_id(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/rooms/{ROOM_ID}").respond(json=load_fixture("room.json"))

    room = client.rooms.get(str(ROOM_ID))

    assert room.id == ROOM_ID


@respx.mock
def test_get_not_found(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/rooms/99999999").respond(
        status_code=404,
        json={"error": "not-found"},
    )

    with pytest.raises(NotFoundError):
        client.rooms.get(99999999)
