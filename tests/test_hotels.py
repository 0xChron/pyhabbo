import pytest

from pyhabbo.hotels import Hotel


@pytest.mark.parametrize(
    "hotel,expected_host",
    [
        (Hotel.COM, "https://www.habbo.com"),
        (Hotel.DE, "https://www.habbo.de"),
        (Hotel.FI, "https://www.habbo.fi"),
        (Hotel.BR, "https://www.habbo.com.br"),
    ],
)
def test_hotel_base_url(hotel: Hotel, expected_host: str) -> None:
    assert hotel.base_url == expected_host


def test_hotel_is_str_enum() -> None:
    assert Hotel.COM == "https://www.habbo.com"
    assert isinstance(Hotel.COM, str)


def test_all_hotels_use_https() -> None:
    for hotel in Hotel:
        assert hotel.base_url.startswith("https://")
