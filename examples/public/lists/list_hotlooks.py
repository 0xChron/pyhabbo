"""GET /api/public/lists/hotlooks — trending avatar looks (XML response)."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    hotlooks = client.lists.list_hotlooks()

    print(f"Avatar base URL: {hotlooks.avatar_url}")
    print(f"{len(hotlooks.looks)} hot looks:")
    for look in hotlooks.looks[:5]:
        print(f"  - {look.gender}: {look.figure}")


if __name__ == "__main__":
    main()
