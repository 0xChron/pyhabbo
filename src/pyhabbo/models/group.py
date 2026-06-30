from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Group(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: str
    name: str
    description: str
    type: str
    room_id: str = Field(alias="roomId")
    badge_code: str = Field(alias="badgeCode")
    primary_colour: str = Field(alias="primaryColour")
    secondary_colour: str = Field(alias="secondaryColour")
    online: bool | None = None
    is_admin: bool | None = Field(default=None, alias="isAdmin")


class GroupMember(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    unique_id: str = Field(alias="uniqueId")
    name: str
    motto: str
    online: bool
    gender: str
    habbo_figure: str = Field(alias="habboFigure")
    member_since: datetime = Field(alias="memberSince")
    is_admin: bool = Field(alias="isAdmin")
