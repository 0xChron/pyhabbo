from pyhabbo.client import HabboClient
from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError
from pyhabbo.hotels import Hotel

__version__ = "0.1.0"

__all__ = [
    "BadRequestError",
    "HabboAPIError",
    "HabboClient",
    "Hotel",
    "NotFoundError",
    "__version__",
]
