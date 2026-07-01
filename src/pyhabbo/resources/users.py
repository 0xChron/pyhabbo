from pyhabbo.models.group import Group
from pyhabbo.models.room import Room
from pyhabbo.models.user import Badge, Friend, User, UserProfile
from pyhabbo.resources.base import BaseResource


class UsersResource(BaseResource):
    def get_by_name(self, name: str, *, etag: str | None = None) -> User:
        return self._get(
            path="/users",
            model=User,
            params={"name": name},
            headers={"If-None-Match": etag} if etag else None,
        )

    def get(self, user_id: str, *, etag: str | None = None) -> User:
        return self._get(
            path=f"/users/{user_id}",
            model=User,
            headers={"If-None-Match": etag} if etag else None,
        )

    def get_profile(self, user_id: str) -> UserProfile:
        return self._get(path=f"/users/{user_id}/profile", model=UserProfile)

    def list_friends(self, user_id: str) -> list[Friend]:
        return self._get_list(path=f"/users/{user_id}/friends", model=Friend)

    def list_groups(self, user_id: str) -> list[Group]:
        return self._get_list(path=f"/users/{user_id}/groups", model=Group)

    def list_rooms(self, user_id: str) -> list[Room]:
        return self._get_list(path=f"/users/{user_id}/rooms", model=Room)

    def list_badges(self, user_id: str) -> list[Badge]:
        return self._get_list(path=f"/users/{user_id}/badges", model=Badge)
