"""GET /api/public/users/{id}/profile — full profile with badges, friends, rooms."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    profile = client.users.get_profile(user.unique_id)

    print(f"Profile: {profile.user.name}")
    print(f"Badges: {len(profile.badges)}")
    print(f"Friends: {len(profile.friends)}")
    print(f"Rooms: {len(profile.rooms)}")
    print(f"Groups: {len(profile.groups)}")


if __name__ == "__main__":
    main()
