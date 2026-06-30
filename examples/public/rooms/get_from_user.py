"""GET /api/public/rooms/{roomId} — look up a room from a user's room list."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    user = client.users.get_by_name("AaronChristian")
    rooms = client.users.list_rooms(user.unique_id)

    if not rooms:
        print(f"{user.name} has no public rooms")
        return

    room = client.rooms.get(rooms[0].id)
    print(f"{room.name} (id {room.id})")
    print(f"Thumbnail: {room.thumbnail_url}")


if __name__ == "__main__":
    main()
