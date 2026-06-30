"""GET /api/public/groups/{id}/members — list members of a group."""

from pyhabbo import HabboClient

GROUP_ID = "g-hhus-85e78fbbdf68e5cb4073de2b20f44ff6"


def main() -> None:
    client = HabboClient()
    members = client.groups.list_members(GROUP_ID)

    print(f"Group has {len(members)} members:")
    for member in members[:5]:
        role = "admin" if member.is_admin else "member"
        print(f"  - {member.name} ({role})")


if __name__ == "__main__":
    main()
