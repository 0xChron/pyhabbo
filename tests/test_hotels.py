import pytest

from pyhabbo.hotels import Hotel


@pytest.mark.parametrize(
    ("hotel", "expected_url"),
    [
        (Hotel.COM, "https://www.habbo.com"),
        (Hotel.DE, "https://www.habbo.de"),
        (Hotel.FI, "https://www.habbo.fi"),
        (Hotel.BR, "https://www.habbo.com.br"),
    ],
)
def test_hotel_url(hotel: Hotel, expected_url: str) -> None:
    assert hotel == expected_url


def test_hotel_is_str() -> None:
    assert Hotel.COM == "https://www.habbo.com"
    assert isinstance(Hotel.COM, str)


def test_all_hotels_use_https() -> None:
    for hotel in Hotel:
        assert hotel.startswith("https://")
