from pathlib import Path

import respx

from pyhabbo import HabboClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@respx.mock
def test_list_hotlooks(base_url: str, client: HabboClient) -> None:
    respx.get(f"{base_url}/api/public/lists/hotlooks").respond(
        content=(FIXTURES_DIR / "hotlooks.xml").read_bytes(),
        headers={"Content-Type": "application/xml"},
    )

    hotlooks = client.lists.list_hotlooks()

    assert hotlooks.avatar_url == "/habbo-imaging/avatar/"
    assert len(hotlooks.looks) == 10
    assert hotlooks.looks[0].gender == "f"
    assert hotlooks.looks[0].figure.startswith("hr-")
    assert len(hotlooks.looks[0].figure_hash) == 32
