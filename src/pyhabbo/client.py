from pyhabbo._http import HTTPTransport
from pyhabbo.hotels import Hotel


class HabboClient:
    def __init__(
        self,
        *,
        hotel: Hotel = Hotel.COM,
        base_url: str | None = None,
        timeout: float = 10.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        self._transport = HTTPTransport(base_url or hotel, timeout=timeout, headers=headers)

    def ping(self) -> None:
        self._transport.request("GET", "/ping")

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "HabboClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
