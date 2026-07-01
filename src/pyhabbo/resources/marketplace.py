from pyhabbo.models.marketplace import MarketplaceBatchStats
from pyhabbo.resources.base import BaseResource


class MarketplaceResource(BaseResource):
    def batch_stats(
        self,
        *,
        room_items: list[str] | None = None,
        wall_items: list[str] | None = None,
    ) -> MarketplaceBatchStats:
        return self._post(
            path="/marketplace/stats/batch",
            model=MarketplaceBatchStats,
            json={
                "roomItems": [{"item": item} for item in room_items or []],
                "wallItems": [{"item": item} for item in wall_items or []],
            },
        )
