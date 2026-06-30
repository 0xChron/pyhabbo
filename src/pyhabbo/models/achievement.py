from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class Achievement(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: int
    name: str
    creation_time: date = Field(alias="creationTime")
    state: str
    category: str


class LevelRequirement(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    level: int
    required_score: int = Field(alias="requiredScore")


class AchievementCatalogEntry(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    achievement: Achievement
    level_requirements: list[LevelRequirement] = Field(alias="levelRequirements")


class UserAchievement(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    achievement: Achievement
    level: int
    score: int
