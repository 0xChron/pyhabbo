import json
from pathlib import Path

import pytest
import respx

from pyhabbo import HabboClient
from pyhabbo.exceptions import NotFoundError

FIXTURES_DIR = Path(__file__).parent / "fixtures"
USER_ID = "hhus-44517b21477063301c17d08817bf8479"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@pytest.fixture
def user_id() -> str:
    return USER_ID


@respx.mock
def test_list_all(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/achievements").respond(
        json=load_fixture("achievements_all.json")
    )

    achievements = client.achievements.list_all()

    assert len(achievements) == 174
    assert achievements[0].achievement.name == "EmailVerification"
    assert achievements[0].level_requirements[0].required_score == 1


@respx.mock
def test_list_for_user(base_url: str, client: HabboClient, user_id: str) -> None:
    respx.get(f"{base_url}/api/public/achievements/{user_id}").respond(
        json=load_fixture("achievements_user.json")
    )

    achievements = client.achievements.list_for_user(user_id)

    assert len(achievements) == 35
    assert achievements[0].achievement.name == "EmailVerification"
    assert achievements[0].level == 1
    assert achievements[0].score == 1


@respx.mock
def test_list_for_user_not_found(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/achievements/invalid").respond(
        status_code=404,
        json={"errors": [{"param": "id", "msg": "user.invalid_id", "value": "invalid"}]},
    )

    with pytest.raises(NotFoundError):
        client.achievements.list_for_user("invalid")
