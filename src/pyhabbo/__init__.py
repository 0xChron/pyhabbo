"""Python SDK for the Habbo public Web API."""

from pyhabbo.client import HabboClient
from pyhabbo.exceptions import (
    APIErrorDetail,
    BadRequestError,
    HabboAPIError,
    NotFoundError,
    parse_api_errors,
)
from pyhabbo.hotels import Hotel

__version__ = "0.1.0"

__all__ = [
    "APIErrorDetail",
    "BadRequestError",
    "HabboAPIError",
    "HabboClient",
    "Hotel",
    "NotFoundError",
    "parse_api_errors",
    "__version__",
]
