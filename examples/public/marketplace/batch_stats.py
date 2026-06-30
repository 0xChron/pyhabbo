"""POST /api/public/marketplace/stats/batch — marketplace stats for room and wall items."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    stats = client.marketplace.batch_stats(
        room_items=["throne"],
        wall_items=["poster"],
    )

    print(f"Status: {stats.status}")

    throne = stats.room_item_data[0]
    print(f"Room item '{throne.item}': avg price {throne.average_price}")

    poster = stats.wall_item_data[0]
    print(f"Wall item '{poster.item}': avg price {poster.average_price}")


if __name__ == "__main__":
    main()
