from pyhabbo.models.badge import BadgeOwners
from pyhabbo.resources.base import BaseResource


class BadgesResource(BaseResource):
    def get_owners(self, badge_code: str) -> BadgeOwners:
        return self._get(path=f"/badge/owners/{badge_code}", model=BadgeOwners)
