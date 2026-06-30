"""GET /api/public/users?name= — look up a user by Habbo name."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    print(f"{user.name} (level {user.current_level})")
    print(f"ID: {user.unique_id}")
    print(f"Online: {user.online}")


if __name__ == "__main__":
    main()
