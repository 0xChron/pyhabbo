from typing import TypeVar

from pydantic import BaseModel

from pyhabbo._http import HTTPTransport

T = TypeVar("T", bound=BaseModel)


class BaseResource:
    def __init__(self, transport: HTTPTransport) -> None:
        self._transport = transport

    def _get(
        self,
        *,
        path: str,
        model: type[T],
        params: dict[str, object] | None = None,
        headers: dict[str, str] | None = None,
    ) -> T:
        data = self._transport.request("GET", path, params=params, headers=headers)
        return model.model_validate(data)

    def _get_list(
        self,
        *,
        path: str,
        model: type[T],
        params: dict[str, object] | None = None,
        headers: dict[str, str] | None = None,
    ) -> list[T]:
        data = self._transport.request("GET", path, params=params, headers=headers)
        return [model.model_validate(item) for item in data]

    def _post(
        self,
        *,
        path: str,
        model: type[T],
        json: dict[str, object],
    ) -> T:
        data = self._transport.request("POST", path, json=json)
        return model.model_validate(data)
