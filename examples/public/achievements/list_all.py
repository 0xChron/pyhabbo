"""GET /api/public/achievements — list all achievements in the catalog."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    achievements = client.achievements.list_all()

    print(f"Catalog has {len(achievements)} achievements")
    for entry in achievements[:5]:
        name = entry.achievement.name
        levels = len(entry.level_requirements)
        print(f"  - {name} ({levels} levels)")


if __name__ == "__main__":
    main()
