from __future__ import annotations

import asyncio
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

try:
    import aiohttp
except ImportError:  # pragma: no cover
    aiohttp = None  # type: ignore[assignment]

from kwork.api import _redact_sensitive
from kwork.client import KworkClient
from kwork.exceptions import KworkException, KworkHTTPException, KworkRetryExceeded

from kwork.agent.config import AgentConfigError, ClientConfig
from kwork.agent.registry import ToolValidationError, get_tool
from kwork.agent.serialize import serialize_result


@dataclass(slots=True, frozen=True)
class ExecutionPolicy:
    allow_write_tools: bool = True
    allow_tools: frozenset[str] | None = None

    def permits(self, tool_name: str, *, is_write: bool) -> bool:
        if self.allow_tools is not None and tool_name not in self.allow_tools:
            return False
        if is_write and not self.allow_write_tools:
            return False
        return True


@dataclass(slots=True)
class ExecutionResult:
    payload: dict[str, Any]
    exit_code: int

    @property
    def ok(self) -> bool:
        ok = self.payload.get("ok")
        return bool(ok)


def _error_payload(
    *,
    err_type: str,
    message: str,
    status: int | None = None,
    endpoint: str | None = None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "ok": False,
        "error": {
            "type": err_type,
            "message": message,
            "status": status,
            "endpoint": endpoint,
            "details": details or {},
        },
    }


def _normalize_detail(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(k): _normalize_detail(v) for k, v in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_normalize_detail(v) for v in value]
    return repr(value)


def _map_exception(err: BaseException) -> ExecutionResult:
    if isinstance(err, (AgentConfigError, ToolValidationError, ValueError)):
        return ExecutionResult(
            payload=_error_payload(err_type=type(err).__name__, message=str(err)),
            exit_code=2,
        )

    if isinstance(err, KworkHTTPException):
        details = {
            "method": err.method,
            "response_json": _normalize_detail(err.response_json),
            "request_params": _normalize_detail(_redact_sensitive(err.request_params or {})),
            "request_body": _normalize_detail(_redact_sensitive(err.request_body or {})),
        }
        return ExecutionResult(
            payload=_error_payload(
                err_type=type(err).__name__,
                message=str(err),
                status=err.status,
                endpoint=err.endpoint,
                details=details,
            ),
            exit_code=10,
        )

    if isinstance(err, KworkRetryExceeded):
        details = {
            "attempts": err.attempts,
            "last_error": repr(err.last_error) if err.last_error is not None else None,
        }
        return ExecutionResult(
            payload=_error_payload(
                err_type=type(err).__name__,
                message=str(err),
                details=details,
            ),
            exit_code=11,
        )

    if aiohttp is not None and isinstance(err, aiohttp.ClientError):
        return ExecutionResult(
            payload=_error_payload(err_type=type(err).__name__, message=str(err) or repr(err)),
            exit_code=11,
        )

    if isinstance(err, asyncio.TimeoutError):
        return ExecutionResult(
            payload=_error_payload(err_type=type(err).__name__, message=str(err) or repr(err)),
            exit_code=11,
        )

    if isinstance(err, KworkException):
        return ExecutionResult(
            payload=_error_payload(err_type=type(err).__name__, message=str(err)),
            exit_code=10,
        )

    return ExecutionResult(
        payload=_error_payload(err_type=type(err).__name__, message=str(err) or repr(err)),
        exit_code=1,
    )


async def _execute_operation_inner(
    tool_name: str,
    args: Mapping[str, Any] | None,
    config: ClientConfig,
    *,
    policy: ExecutionPolicy | None = None,
) -> dict[str, Any]:
    spec = get_tool(tool_name)
    effective_policy = policy or ExecutionPolicy()
    if not effective_policy.permits(spec.name, is_write=spec.is_write):
        raise ToolValidationError(f"Tool {spec.name} is not allowed by the current policy")

    validated = spec.validate_args(args)

    async with KworkClient(
        login=config.login,
        password=config.password,
        proxy=config.proxy,
        phone_last=config.phone_last,
        timeout=config.timeout,
        retry_max_attempts=config.retry_max_attempts,
        relogin_on_auth_error=config.relogin_on_auth_error,
    ) as client:
        result = await spec.handler(client, validated)

    return {"ok": True, "tool": spec.name, "data": serialize_result(result)}


async def execute_operation(
    tool_name: str,
    args: Mapping[str, Any] | None,
    config: ClientConfig,
    *,
    policy: ExecutionPolicy | None = None,
) -> ExecutionResult:
    try:
        payload = await _execute_operation_inner(tool_name, args, config, policy=policy)
    except Exception as err:  # noqa: BLE001 - normalized for machine-readable output
        return _map_exception(err)
    return ExecutionResult(payload=payload, exit_code=0)

