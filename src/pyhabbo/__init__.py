from pyhabbo.client import HabboClient
from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError
from pyhabbo.hotels import Hotel
from pyhabbo.models.achievement import AchievementCatalogEntry, UserAchievement
from pyhabbo.models.user import Friend, Room, User, UserProfile

__version__ = "0.1.0"

__all__ = [
    "AchievementCatalogEntry",
    "BadRequestError",
    "Friend",
    "HabboAPIError",
    "HabboClient",
    "Hotel",
    "NotFoundError",
    "Room",
    "User",
    "UserAchievement",
    "UserProfile",
    "__version__",
]
