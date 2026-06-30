"""POST /api/public/marketplace/stats/batch — room items only."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    stats = client.marketplace.batch_stats(room_items=["throne", "rare_dragonlamp"])

    for item in stats.room_item_data:
        latest = item.history[-1]
        print(
            f"{item.item}: avg {item.average_price} credits, "
            f"sold yesterday: {latest.total_sold_items}"
        )


if __name__ == "__main__":
    main()
