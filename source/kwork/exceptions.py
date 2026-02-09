from __future__ import annotations

from typing import Any


class KworkException(Exception):
    """Base exception for this library."""


class KworkHTTPException(KworkException):
    """HTTP-level error (non-2xx or invalid/undecodable response)."""

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        method: str | None = None,
        endpoint: str | None = None,
        response_text: str | None = None,
        response_json: dict[str, Any] | None = None,
        request_params: dict[str, Any] | None = None,
        request_body: Any | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.method = method
        self.endpoint = endpoint
        self.response_text = response_text
        self.response_json = response_json
        self.request_params = request_params
        self.request_body = request_body


class KworkRetryExceeded(KworkException):
    """Raised when retry attempts are exhausted."""

    def __init__(
        self,
        message: str,
        *,
        attempts: int,
        last_error: BaseException | None = None,
    ) -> None:
        super().__init__(message)
        self.attempts = attempts
        self.last_error = last_error


class KworkBotException(Exception):
    pass
