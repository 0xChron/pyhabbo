"""GET /api/public/achievements/{id} — list a user's achievement progress."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    achievements = client.achievements.list_for_user(user.unique_id)

    print(f"{user.name} has progress on {len(achievements)} achievements:")
    for entry in achievements[:5]:
        name = entry.achievement.name
        print(f"  - {name}: level {entry.level}, score {entry.score}")


if __name__ == "__main__":
    main()
