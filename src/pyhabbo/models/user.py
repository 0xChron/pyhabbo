from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Badge(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    code: str
    name: str
    description: str


class SelectedBadge(Badge):
    badge_index: int = Field(alias="badgeIndex")


class Friend(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    unique_id: str = Field(alias="uniqueId")
    name: str
    motto: str
    online: bool
    figure_string: str = Field(alias="figureString")


class User(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    unique_id: str = Field(alias="uniqueId")
    name: str
    figure_string: str = Field(alias="figureString")
    motto: str
    online: bool
    last_access_time: datetime = Field(alias="lastAccessTime")
    member_since: datetime = Field(alias="memberSince")
    profile_visible: bool = Field(alias="profileVisible")
    current_level: int = Field(alias="currentLevel")
    current_level_complete_percent: int = Field(alias="currentLevelCompletePercent")
    total_experience: int = Field(alias="totalExperience")
    star_gem_count: int = Field(alias="starGemCount")
    selected_badges: list[SelectedBadge] = Field(alias="selectedBadges")


class Group(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: str | None = None
    name: str | None = None
    description: str | None = None
    type: str | None = None
    room_id: int | None = Field(default=None, alias="roomId")
    badge_code: str | None = Field(default=None, alias="badgeCode")


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


class UserProfile(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    user: User
    groups: list[Group]
    badges: list[Badge]
    friends: list[Friend]
    rooms: list[Room]
