from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


class AgentConfigError(ValueError):
    """Raised when agent/CLI configuration is invalid."""


_TRUE_VALUES = {"1", "true", "yes", "on"}
_FALSE_VALUES = {"0", "false", "no", "off"}


def _parse_bool(value: str, *, field: str) -> bool:
    normalized = value.strip().lower()
    if normalized in _TRUE_VALUES:
        return True
    if normalized in _FALSE_VALUES:
        return False
    raise AgentConfigError(f"Invalid boolean for {field}: {value!r}")


def _parse_float(value: str, *, field: str) -> float:
    try:
        out = float(value)
    except ValueError as err:
        raise AgentConfigError(f"Invalid float for {field}: {value!r}") from err
    return out


def _parse_int(value: str, *, field: str) -> int:
    try:
        out = int(value)
    except ValueError as err:
        raise AgentConfigError(f"Invalid integer for {field}: {value!r}") from err
    return out


@dataclass(slots=True)
class ClientConfig:
    login: str
    password: str
    phone_last: str | None = None
    proxy: str | None = None
    timeout: float | None = 30.0
    retry_max_attempts: int = 1
    relogin_on_auth_error: bool = False

    @classmethod
    def from_sources(
        cls,
        *,
        env: Mapping[str, str] | None = None,
        login: str | None = None,
        password: str | None = None,
        phone_last: str | None = None,
        proxy: str | None = None,
        timeout: float | str | None = None,
        retry_max_attempts: int | str | None = None,
        relogin_on_auth_error: bool | str | None = None,
    ) -> ClientConfig:
        env_map = dict(os.environ if env is None else env)

        resolved_login = login if login is not None else env_map.get("KWORK_LOGIN")
        resolved_password = password if password is not None else env_map.get("KWORK_PASSWORD")
        resolved_phone_last = phone_last if phone_last is not None else env_map.get("KWORK_PHONE_LAST")
        resolved_proxy = proxy if proxy is not None else env_map.get("KWORK_PROXY")

        if timeout is None:
            timeout_env = env_map.get("KWORK_TIMEOUT")
            resolved_timeout: float | None = (
                _parse_float(timeout_env, field="KWORK_TIMEOUT") if timeout_env is not None else 30.0
            )
        elif isinstance(timeout, str):
            resolved_timeout = _parse_float(timeout, field="timeout")
        else:
            resolved_timeout = timeout

        if retry_max_attempts is None:
            retry_env = env_map.get("KWORK_RETRY_MAX_ATTEMPTS")
            resolved_retry = (
                _parse_int(retry_env, field="KWORK_RETRY_MAX_ATTEMPTS") if retry_env is not None else 1
            )
        elif isinstance(retry_max_attempts, str):
            resolved_retry = _parse_int(retry_max_attempts, field="retry_max_attempts")
        else:
            resolved_retry = retry_max_attempts

        if relogin_on_auth_error is None:
            relogin_env = env_map.get("KWORK_RELOGIN_ON_AUTH_ERROR")
            resolved_relogin = (
                _parse_bool(relogin_env, field="KWORK_RELOGIN_ON_AUTH_ERROR")
                if relogin_env is not None
                else False
            )
        elif isinstance(relogin_on_auth_error, str):
            resolved_relogin = _parse_bool(relogin_on_auth_error, field="relogin_on_auth_error")
        else:
            resolved_relogin = relogin_on_auth_error

        if not resolved_login:
            raise AgentConfigError("Missing credentials: KWORK_LOGIN (or --login) is required")
        if not resolved_password:
            raise AgentConfigError("Missing credentials: KWORK_PASSWORD (or --password) is required")
        if resolved_retry < 1:
            raise AgentConfigError("retry_max_attempts must be >= 1")
        if resolved_timeout is not None and resolved_timeout <= 0:
            raise AgentConfigError("timeout must be > 0 when provided")

        return cls(
            login=resolved_login,
            password=resolved_password,
            phone_last=resolved_phone_last,
            proxy=resolved_proxy,
            timeout=resolved_timeout,
            retry_max_attempts=resolved_retry,
            relogin_on_auth_error=resolved_relogin,
        )
