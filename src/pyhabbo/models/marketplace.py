from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class MarketplaceHistoryEntry(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    day_offset: str = Field(alias="dayOffset")
    average_price: int = Field(alias="averagePrice")
    total_sold_items: int = Field(alias="totalSoldItems")
    total_credit_sum: int = Field(alias="totalCreditSum")
    total_open_offers: int = Field(alias="totalOpenOffers")


class MarketplaceItemStats(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    item: str
    extra_data: str | None = Field(default=None, alias="extraData")
    stats_date: date = Field(alias="statsDate")
    history: list[MarketplaceHistoryEntry]
    sold_item_count: int = Field(alias="soldItemCount")
    credit_sum: int = Field(alias="creditSum")
    average_price: int = Field(alias="averagePrice")
    total_open_offers: int = Field(alias="totalOpenOffers")
    current_open_offers: int = Field(alias="currentOpenOffers")
    current_price: int = Field(alias="currentPrice")
    history_limit_in_days: int = Field(alias="historyLimitInDays")


class MarketplaceBatchStats(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    status: str
    room_item_data: list[MarketplaceItemStats] = Field(alias="roomItemData")
    wall_item_data: list[MarketplaceItemStats] = Field(alias="wallItemData")
