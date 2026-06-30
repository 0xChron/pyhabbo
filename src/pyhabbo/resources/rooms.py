from pyhabbo.models.room import Room
from pyhabbo.resources.base import BaseResource


class RoomsResource(BaseResource):
    def get(self, room_id: str | int) -> Room:
        return self._get(f"/rooms/{room_id}", Room)
