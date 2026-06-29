from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class APIErrorDetail:
    param: str | None
    msg: str
    value: str | None = None


class HabboAPIError(Exception):
    def __init__(
        self,
        status_code: int,
        errors: list[APIErrorDetail],
        message: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.errors = errors
        if message is not None:
            super().__init__(message)
        elif errors:
            super().__init__(errors[0].msg)
        else:
            super().__init__(f"Habbo API error (HTTP {status_code})")


class NotFoundError(HabboAPIError):
    pass


class BadRequestError(HabboAPIError):
    pass


def parse_api_errors(payload: object) -> list[APIErrorDetail]:
    if not isinstance(payload, dict):
        return []

    raw_errors = payload.get("errors", [])
    if not isinstance(raw_errors, list):
        return []

    errors: list[APIErrorDetail] = []
    for item in raw_errors:
        if not isinstance(item, dict):
            continue
        errors.append(
            APIErrorDetail(
                param=item.get("param"),
                msg=item.get("msg", "unknown_error"),
                value=item.get("value"),
            )
        )
    return errors
