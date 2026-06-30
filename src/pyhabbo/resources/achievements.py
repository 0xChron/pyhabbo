from pyhabbo.models.achievement import AchievementCatalogEntry, UserAchievement
from pyhabbo.resources.base import BaseResource


class AchievementsResource(BaseResource):
    def list_all(self) -> list[AchievementCatalogEntry]:
        return self._get_list("/achievements", AchievementCatalogEntry)

    def list_for_user(self, user_id: str) -> list[UserAchievement]:
        return self._get_list(f"/achievements/{user_id}", UserAchievement)
