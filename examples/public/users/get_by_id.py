"""GET /api/public/users/{id} — look up a user by unique ID."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")

    # get user info by ID
    same_user = client.users.get(user.unique_id)

    print(f"{same_user.name} — {same_user.motto!r}")
    print(f"Member since: {same_user.member_since.date()}")


if __name__ == "__main__":
    main()
