import asyncio

from kwork.agent.config import ClientConfig
from kwork.agent.runner import _map_exception, execute_operation
from kwork.exceptions import KworkHTTPException


def test_map_http_exception_redacts_sensitive_request_data() -> None:
    err = KworkHTTPException(
        "boom",
        status=401,
        endpoint="signIn",
        request_params={"token": "secret", "ok": 1},
        request_body={"password": "secret2"},
    )

    result = _map_exception(err)
    error = result.payload["error"]

    assert result.exit_code == 10
    assert error["status"] == 401
    assert error["endpoint"] == "signIn"
    assert error["details"]["request_params"]["token"] == "<redacted>"
    assert error["details"]["request_params"]["ok"] == 1
    assert error["details"]["request_body"]["password"] == "<redacted>"


def test_execute_operation_unknown_tool_returns_validation_error() -> None:
    config = ClientConfig(login="login", password="password")
    result = asyncio.run(execute_operation("missing_tool", {}, config))

    assert result.exit_code == 2
    assert result.payload["ok"] is False
    assert result.payload["error"]["type"] == "ToolValidationError"
