import json
from pathlib import Path

import pytest
import respx

from pyhabbo import HabboClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"
USER_ID = "hhus-d58a49f5fd62a4e49c69d54200191e20"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@pytest.fixture
def user_id() -> str:
    return USER_ID


@respx.mock
def test_get_by_name(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/users").respond(json=load_fixture("user_by_name.json"))

    user = client.users.get_by_name("AaronChristian")

    assert user.name == "AaronChristian"
    assert user.unique_id == USER_ID
    assert user.current_level == 25


@respx.mock
def test_get_by_name_with_etag(base_url: str, client: HabboClient) -> None:
    route = respx.get(f"{base_url}/api/public/users").respond(
        json=load_fixture("user_by_name.json")
    )

    client.users.get_by_name("AaronChristian", etag='"abc123"')

    assert route.calls.last.request.headers["If-None-Match"] == '"abc123"'


@respx.mock
def test_get(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}").respond(json=load_fixture("user_by_id.json"))

    user = client.users.get(user_id)

    assert user.name == "AaronChristian"
    assert len(user.selected_badges) == 4


@respx.mock
def test_get_profile(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}/profile").respond(
        json=load_fixture("user_profile.json")
    )

    profile = client.users.get_profile(user_id)

    assert profile.user.name == "AaronChristian"
    assert len(profile.badges) > 0
    assert len(profile.friends) == 363
    assert len(profile.rooms) == 3


@respx.mock
def test_list_friends(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}/friends").respond(
        json=load_fixture("user_friends.json")
    )

    friends = client.users.list_friends(user_id)

    assert len(friends) == 363
    assert friends[0].name == "!Mythical!"


@respx.mock
def test_list_badges(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}/badges").respond(
        json=load_fixture("user_badges.json")
    )

    badges = client.users.list_badges(user_id)

    assert len(badges) > 0
    assert badges[0].code == "DE382"


@respx.mock
def test_list_groups(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}/groups").respond(
        json=load_fixture("user_groups.json")
    )

    groups = client.users.list_groups(user_id)

    assert len(groups) == 59


@respx.mock
def test_list_rooms(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/users/{user_id}/rooms").respond(
        json=load_fixture("user_rooms.json")
    )

    rooms = client.users.list_rooms(user_id)

    assert len(rooms) == 3
    assert rooms[0].owner_name == "AaronChristian"


@respx.mock
def test_get_user_not_found(base_url: str, client: HabboClient) -> None:
    from pyhabbo.exceptions import NotFoundError

    respx.get(f"{base_url}/api/public/users/invalid").respond(
        status_code=404,
        json={"errors": [{"param": "id", "msg": "user.invalid_id", "value": "invalid"}]},
    )

    with pytest.raises(NotFoundError):
        client.users.get("invalid")
