from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Room(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: int
    unique_id: str = Field(alias="uniqueId")
    name: str
    description: str
    creation_time: datetime = Field(alias="creationTime")
    tags: list[str]
    maximum_visitors: int = Field(alias="maximumVisitors")
    show_owner_name: bool = Field(alias="showOwnerName")
    owner_name: str = Field(alias="ownerName")
    owner_unique_id: str = Field(alias="ownerUniqueId")
    categories: list[str]
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    image_url: str | None = Field(default=None, alias="imageUrl")
    rating: int
    habbo_group_id: str | None = Field(default=None, alias="habboGroupId")
    public_room: bool | None = Field(default=None, alias="publicRoom")
    door_mode: str | None = Field(default=None, alias="doorMode")
