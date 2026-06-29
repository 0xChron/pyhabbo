from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class APIErrorDetail:
    """A single error entry from the Habbo API ``errors`` array."""

    param: str | None
    msg: str
    value: str | None = None


class HabboAPIError(Exception):
    """Base exception for Habbo API errors."""

    def __init__(
        self,
        status_code: int,
        errors: list[APIErrorDetail],
        message: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.errors = errors
        super().__init__(
            message or (errors[0].msg if errors else f"Habbo API error (HTTP {status_code})")
        )


class NotFoundError(HabboAPIError):
    """HTTP 404 — resource not found."""


class BadRequestError(HabboAPIError):
    """HTTP 400 — invalid request."""


def parse_api_errors(payload: object) -> list[APIErrorDetail]:
    """Parse the ``errors`` field from a Habbo API error response body."""
    if not isinstance(payload, dict):
        return []

    raw_errors = payload.get("errors", [])
    if not isinstance(raw_errors, list):
        return []

    return [
        APIErrorDetail(
            param=item.get("param"),
            msg=item.get("msg", "unknown_error"),
            value=item.get("value"),
        )
        for item in raw_errors
        if isinstance(item, dict)
    ]
