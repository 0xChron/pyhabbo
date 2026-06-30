from typing import Any

import httpx

from pyhabbo.exceptions import BadRequestError, HabboAPIError, NotFoundError, parse_api_errors


class HTTPTransport:
    """Sync HTTP client for Habbo /api/public endpoints."""

    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        headers: dict[str, str] | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        self._owns_client = client is None
        self._client = client or httpx.Client(
            base_url=base_url.rstrip("/"),
            timeout=timeout,
            headers=headers,
        )

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Any:
        response = self._client.request(
            method,
            f"/api/public{path}",
            params=params,
            json=json,
            headers=headers,
        )

        if not response.is_success:
            self._raise_for_status(response)

        if not response.content:
            return None
        return response.json()

    def request_text(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> str:
        response = self._client.request(
            method,
            f"/api/public{path}",
            params=params,
            headers=headers,
        )

        if not response.is_success:
            self._raise_for_status(response)

        return response.text

    def _raise_for_status(self, response: httpx.Response) -> None:
        errors = []
        try:
            errors = parse_api_errors(response.json())
        except ValueError:
            pass

        status = response.status_code
        if status == 404:
            raise NotFoundError(status, errors)
        if status == 400:
            raise BadRequestError(status, errors)
        raise HabboAPIError(status, errors)
