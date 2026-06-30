from pydantic import BaseModel, ConfigDict, Field


class BadgeOwners(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    owner_count: int = Field(alias="ownerCount")
    name: str
    description: str
