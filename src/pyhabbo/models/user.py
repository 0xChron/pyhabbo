from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyhabbo.models.group import Group
from pyhabbo.models.room import Room


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


class UserProfile(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    user: User
    groups: list[Group]
    badges: list[Badge]
    friends: list[Friend]
    rooms: list[Room]
