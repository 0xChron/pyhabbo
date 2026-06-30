from pyhabbo.client import HabboClient
from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError
from pyhabbo.hotels import Hotel
from pyhabbo.models.achievement import AchievementCatalogEntry, UserAchievement
from pyhabbo.models.badge import BadgeOwners
from pyhabbo.models.group import Group, GroupMember
from pyhabbo.models.room import Room
from pyhabbo.models.user import Friend, User, UserProfile

__version__ = "0.1.0"

__all__ = [
    "AchievementCatalogEntry",
    "BadgeOwners",
    "BadRequestError",
    "Friend",
    "Group",
    "GroupMember",
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
