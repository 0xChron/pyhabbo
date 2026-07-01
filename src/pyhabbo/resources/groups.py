from pyhabbo.models.group import Group, GroupMember
from pyhabbo.resources.base import BaseResource


class GroupsResource(BaseResource):
    def get(self, group_id: str) -> Group:
        return self._get(path=f"/groups/{group_id}", model=Group)

    def list_members(self, group_id: str) -> list[GroupMember]:
        return self._get_list(path=f"/groups/{group_id}/members", model=GroupMember)
