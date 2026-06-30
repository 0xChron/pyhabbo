import json
from pathlib import Path

import respx

from pyhabbo import HabboClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"
BADGE_CODE = "ITF82"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@respx.mock
def test_get_owners(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/badge/owners/{BADGE_CODE}").respond(
        json=load_fixture("badge_owners.json")
    )

    badge = client.badges.get_owners(BADGE_CODE)

    assert badge.name == "Amb 12 Days of Safety - 2021"
    assert badge.owner_count == 1520
    assert badge.description.startswith("On the 12th day of Safety")


@respx.mock
def test_get_owners_unknown_badge(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/badge/owners/INVALIDBADGE").respond(
        json={"ownerCount": 0, "name": "INVALIDBADGE", "description": ""}
    )

    badge = client.badges.get_owners("INVALIDBADGE")

    assert badge.owner_count == 0
    assert badge.name == "INVALIDBADGE"
