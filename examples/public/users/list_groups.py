"""GET /api/public/users/{id}/groups — list groups a user belongs to."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    groups = client.users.list_groups(user.unique_id)

    print(f"{user.name} is in {len(groups)} groups:")
    for group in groups[:5]:
        print(f"  - {group.name} ({group.type})")


if __name__ == "__main__":
    main()
