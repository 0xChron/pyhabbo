import json
from pathlib import Path

import pytest
import respx

from pyhabbo import HabboClient
from pyhabbo.exceptions import NotFoundError

FIXTURES_DIR = Path(__file__).parent / "fixtures"
GROUP_ID = "g-hhus-85e78fbbdf68e5cb4073de2b20f44ff6"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@pytest.fixture
def group_id() -> str:
    return GROUP_ID


@respx.mock
def test_get(base_url: str, client: HabboClient, group_id: str) -> None:
    respx.get(f"{base_url}/api/public/groups/{group_id}").respond(json=load_fixture("group.json"))

    group = client.groups.get(group_id)

    assert group.name == "1v1 Memory Game"
    assert group.type == "NORMAL"
    assert group.primary_colour == "b4278e"


@respx.mock
def test_list_members(base_url: str, client: HabboClient, group_id: str) -> None:
    respx.get(f"{base_url}/api/public/groups/{group_id}/members").respond(
        json=load_fixture("group_members.json")
    )

    members = client.groups.list_members(group_id)

    assert len(members) == 99
    assert members[0].name == "AX"
    assert members[0].gender == "f"


@respx.mock
def test_get_not_found(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/groups/invalid").respond(
        status_code=404,
        json={"errors": [{"param": "id", "msg": "group.invalid_id", "value": "invalid"}]},
    )

    with pytest.raises(NotFoundError):
        client.groups.get("invalid")
