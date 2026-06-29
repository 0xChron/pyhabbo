from pyhabbo._http import HTTPTransport
from pyhabbo.hotels import Hotel


class HabboClient:
    """Client for the Habbo public Web API."""

    def __init__(
        self,
        *,
        hotel: Hotel = Hotel.COM,
        base_url: str | None = None,
        timeout: float = 10.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        url = base_url or hotel.base_url
        self._transport = HTTPTransport(url, timeout=timeout, headers=headers)

    def ping(self) -> None:
        """Health check — GET /api/public/ping."""
        self._transport.request("GET", "/ping")

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "HabboClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
