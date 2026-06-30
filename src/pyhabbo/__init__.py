from pyhabbo.client import HabboClient
from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError
from pyhabbo.hotels import Hotel
from pyhabbo.models.user import Friend, Room, User, UserProfile

__version__ = "0.1.0"

__all__ = [
    "BadRequestError",
    "Friend",
    "HabboAPIError",
    "HabboClient",
    "Hotel",
    "NotFoundError",
    "Room",
    "User",
    "UserProfile",
    "__version__",
]
