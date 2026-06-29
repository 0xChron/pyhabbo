from typing import Any

import httpx

from pyhabbo.exceptions import (
    APIErrorDetail,
    BadRequestError,
    HabboAPIError,
    NotFoundError,
    parse_api_errors,
)


class HTTPTransport:
    """Low-level sync HTTP client for /api/public endpoints."""

    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        headers: dict[str, str] | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._owns_client = client is None
        self._client = client or httpx.Client(
            base_url=self._base_url,
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
        """
        Send a request to /api/public{path}.

        path should be like "/users" or "/users/{id}/profile" — not the full URL.
        Returns parsed JSON (dict or list), or None for empty bodies.
        """
        response = self._client.request(
            method,
            f"/api/public{path}",
            params=params,
            json=json,
            headers=headers,
        )

        if response.is_success:
            if not response.content:
                return None
            return response.json()

        self._raise_for_status(response)

    def _raise_for_status(self, response: httpx.Response) -> None:
        errors = self._parse_errors(response)
        status = response.status_code

        if status == 404:
            raise NotFoundError(status, errors)
        if status == 400:
            raise BadRequestError(status, errors)
        raise HabboAPIError(status, errors)

    @staticmethod
    def _parse_errors(response: httpx.Response) -> list[APIErrorDetail]:
        try:
            payload = response.json()
        except ValueError:
            return []

        return parse_api_errors(payload)
