from pyhabbo.models.group import Group, GroupMember
from pyhabbo.resources.base import BaseResource


class GroupsResource(BaseResource):
    def get(self, group_id: str) -> Group:
        return self._get(f"/groups/{group_id}", Group)

    def list_members(self, group_id: str) -> list[GroupMember]:
        return self._get_list(f"/groups/{group_id}/members", GroupMember)
