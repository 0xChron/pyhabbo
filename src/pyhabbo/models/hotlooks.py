from pydantic import BaseModel, ConfigDict


class HotLook(BaseModel):
    model_config = ConfigDict(extra="ignore")

    gender: str
    figure: str
    figure_hash: str


class HotLooks(BaseModel):
    model_config = ConfigDict(extra="ignore")

    avatar_url: str
    looks: list[HotLook]
