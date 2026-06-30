import json
from pathlib import Path

import respx

from pyhabbo import HabboClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURES_DIR / name).read_text())


@respx.mock
def test_batch_stats(base_url: str, client: HabboClient) -> None:
    route = respx.post(f"{base_url}/api/public/marketplace/stats/batch").respond(
        json=load_fixture("marketplace_batch.json")
    )

    stats = client.marketplace.batch_stats(room_items=["throne"], wall_items=["poster"])

    assert stats.status == "OK"
    assert stats.room_item_data[0].item == "throne"
    assert stats.wall_item_data[0].item == "poster"
    assert len(stats.room_item_data[0].history) == 30
    assert stats.room_item_data[0].history[0].average_price == 1075

    request_body = json.loads(route.calls.last.request.content)
    assert request_body == {
        "roomItems": [{"item": "throne"}],
        "wallItems": [{"item": "poster"}],
    }


@respx.mock
def test_batch_stats_empty_items(base_url: str, client: HabboClient) -> None:
    route = respx.post(f"{base_url}/api/public/marketplace/stats/batch").respond(
        json={"status": "OK", "roomItemData": [], "wallItemData": []}
    )

    stats = client.marketplace.batch_stats()

    assert stats.room_item_data == []
    assert json.loads(route.calls.last.request.content) == {
        "roomItems": [],
        "wallItems": [],
    }
