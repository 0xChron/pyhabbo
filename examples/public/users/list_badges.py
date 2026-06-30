"""GET /api/public/users/{id}/badges — list badges a user has earned."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    badges = client.users.list_badges(user.unique_id)

    print(f"{user.name} has {len(badges)} badges:")
    for badge in badges[:5]:
        print(f"  - [{badge.code}] {badge.name}")


if __name__ == "__main__":
    main()
