"""GET /api/public/users/{id}/friends — list a user's friends."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    friends = client.users.list_friends(user.unique_id)

    print(f"{user.name} has {len(friends)} friends:")
    for friend in friends[:5]:
        status = "online" if friend.online else "offline"
        print(f"  - {friend.name} ({status})")


if __name__ == "__main__":
    main()
