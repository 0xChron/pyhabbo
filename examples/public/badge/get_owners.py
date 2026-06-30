"""GET /api/public/badge/owners/{badgeCode} — badge info and owner count."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    badge = client.badges.get_owners("ITF82")

    print(f"[{badge.name}]")
    print(f"Owners: {badge.owner_count}")
    print(badge.description)


if __name__ == "__main__":
    main()
