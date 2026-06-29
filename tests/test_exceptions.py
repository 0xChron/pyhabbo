import pytest

from pyhabbo.exceptions import (
    APIErrorDetail,
    BadRequestError,
    HabboAPIError,
    NotFoundError,
    parse_api_errors,
)


def test_api_error_detail_is_frozen() -> None:
    detail = APIErrorDetail(param="id", msg="user.invalid_id", value="abc")
    with pytest.raises(AttributeError):
        detail.msg = "other"  # type: ignore[misc]


def test_habbo_api_error_uses_first_error_message() -> None:
    errors = [APIErrorDetail(param="id", msg="user.invalid_id", value="abc")]
    exc = HabboAPIError(404, errors)

    assert str(exc) == "user.invalid_id"
    assert exc.status_code == 404
    assert exc.errors == errors


def test_habbo_api_error_fallback_message_without_errors() -> None:
    exc = HabboAPIError(500, [])

    assert str(exc) == "Habbo API error (HTTP 500)"


def test_habbo_api_error_custom_message() -> None:
    exc = HabboAPIError(500, [], message="custom")

    assert str(exc) == "custom"


def test_not_found_and_bad_request_inherit_from_habbo_api_error() -> None:
    assert issubclass(NotFoundError, HabboAPIError)
    assert issubclass(BadRequestError, HabboAPIError)


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        (
            {"errors": [{"param": "id", "msg": "user.invalid_id", "value": "x"}]},
            [APIErrorDetail(param="id", msg="user.invalid_id", value="x")],
        ),
        ({"errors": "not-a-list"}, []),
        ({"other": []}, []),
        ("not-a-dict", []),
        ({}, []),
    ],
)
def test_parse_api_errors(payload: object, expected: list[APIErrorDetail]) -> None:
    assert parse_api_errors(payload) == expected


def test_parse_api_errors_defaults_missing_msg() -> None:
    result = parse_api_errors({"errors": [{"param": "name"}]})

    assert result == [APIErrorDetail(param="name", msg="unknown_error", value=None)]
