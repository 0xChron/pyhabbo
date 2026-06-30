"""GET /api/public/rooms/{roomId} — fetch a room by numeric ID."""

from pyhabbo import HabboClient

# Use the numeric room ID, not the r-hhus-... unique ID.
ROOM_ID = 72631843


def main() -> None:
    client = HabboClient()
    room = client.rooms.get(ROOM_ID)

    print(f"{room.name} — {room.description}")
    print(f"Owner: {room.owner_name}")
    print(f"Rating: {room.rating}, door: {room.door_mode}")


if __name__ == "__main__":
    main()
