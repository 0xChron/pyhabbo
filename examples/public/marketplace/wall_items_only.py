"""POST /api/public/marketplace/stats/batch — wall items only."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    stats = client.marketplace.batch_stats(wall_items=["poster"])

    item = stats.wall_item_data[0]
    print(f"{item.item}: {item.history_limit_in_days} days of history")
    print(f"Current open offers: {item.current_open_offers}")


if __name__ == "__main__":
    main()
