"""GET /api/public/groups/{id} — fetch a group by ID."""

from pyhabbo import HabboClient

# Example group ID — replace with any g-hhus-... ID from a user's groups list.
GROUP_ID = "g-hhus-85e78fbbdf68e5cb4073de2b20f44ff6"


def main() -> None:
    client = HabboClient()
    group = client.groups.get(GROUP_ID)

    print(f"{group.name} ({group.type})")
    print(f"Description: {group.description}")
    print(f"Colours: #{group.primary_colour} / #{group.secondary_colour}")


if __name__ == "__main__":
    main()
