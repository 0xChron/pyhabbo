"""GET /api/public/users/{id}/rooms — list a user's public rooms."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    rooms = client.users.list_rooms(user.unique_id)

    print(f"{user.name} has {len(rooms)} rooms:")
    for room in rooms[:5]:
        print(f"  - {room.name} (rating {room.rating}, id {room.id})")


if __name__ == "__main__":
    main()
