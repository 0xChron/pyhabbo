from pyhabbo._http import HTTPTransport
from pyhabbo.hotels import Hotel
from pyhabbo.resources.achievements import AchievementsResource
from pyhabbo.resources.users import UsersResource


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
        self._achievements = AchievementsResource(self._transport)
        self._users = UsersResource(self._transport)

    @property
    def achievements(self) -> AchievementsResource:
        return self._achievements

    @property
    def users(self) -> UsersResource:
        return self._users

    def ping(self) -> None:
        self._transport.request("GET", "/ping")

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "HabboClient":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
