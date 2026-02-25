import json
from typing import Any

import pytest

from kwork.agent.runner import ExecutionResult


def _set_auth_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KWORK_LOGIN", "login")
    monkeypatch.setenv("KWORK_PASSWORD", "password")


def test_cli_me_emits_json(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    from kwork.agent import cli

    _set_auth_env(monkeypatch)

    async def fake_execute_operation(tool: str, args: dict[str, Any], config: Any) -> ExecutionResult:
        assert tool == "get_me"
        assert args == {}
        assert config.login == "login"
        return ExecutionResult(payload={"ok": True, "tool": tool, "data": {"id": 1}}, exit_code=0)

    monkeypatch.setattr(cli, "execute_operation", fake_execute_operation)

    exit_code = cli.run_cli(["me"])
    out = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert out == {"ok": True, "tool": "get_me", "data": {"id": 1}}


def test_cli_dialogs_list_page_dispatches_correct_tool(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    _set_auth_env(monkeypatch)
    captured: dict[str, Any] = {}

    async def fake_execute_operation(tool: str, args: dict[str, Any], config: Any) -> ExecutionResult:
        captured["tool"] = tool
        captured["args"] = args
        return ExecutionResult(payload={"ok": True, "tool": tool, "data": []}, exit_code=0)

    monkeypatch.setattr(cli, "execute_operation", fake_execute_operation)

    exit_code = cli.run_cli(["dialogs", "list", "--page", "2", "--excluded-ids", "1,2"])
    _ = capsys.readouterr()

    assert exit_code == 0
    assert captured["tool"] == "get_dialogs_page"
    assert captured["args"] == {"page": 2, "excluded_ids": "1,2"}


def test_cli_dialogs_list_all_dispatches_to_get_all_dialogs(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    _set_auth_env(monkeypatch)
    captured: dict[str, Any] = {}

    async def fake_execute_operation(tool: str, args: dict[str, Any], config: Any) -> ExecutionResult:
        captured["tool"] = tool
        captured["args"] = args
        return ExecutionResult(payload={"ok": True, "tool": tool, "data": []}, exit_code=0)

    monkeypatch.setattr(cli, "execute_operation", fake_execute_operation)

    exit_code = cli.run_cli(["dialogs", "list", "--all"])
    _ = capsys.readouterr()

    assert exit_code == 0
    assert captured["tool"] == "get_all_dialogs"
    assert captured["args"] == {}


def test_cli_missing_credentials_returns_json_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    monkeypatch.delenv("KWORK_LOGIN", raising=False)
    monkeypatch.delenv("KWORK_PASSWORD", raising=False)

    exit_code = cli.run_cli(["me"])
    out = json.loads(capsys.readouterr().out)

    assert exit_code == 2
    assert out["ok"] is False
    assert out["error"]["type"] == "AgentConfigError"


def test_cli_parse_error_returns_json_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    _set_auth_env(monkeypatch)

    exit_code = cli.run_cli(["user", "get"])
    out = json.loads(capsys.readouterr().out)

    assert exit_code == 2
    assert out["ok"] is False
    assert out["error"]["type"] == "CLIParseError"


def test_cli_tools_list_includes_dynamic_tools(capsys: pytest.CaptureFixture[str]) -> None:
    from kwork.agent import cli

    exit_code = cli.run_cli(["tools", "list", "--include-write"])
    out = json.loads(capsys.readouterr().out)

    names = {item["name"] for item in out["data"]}
    assert exit_code == 0
    assert out["ok"] is True
    assert "get_me" in names
    assert "accept_extras" in names
    assert "web_submit_exchange_offer" in names


def test_cli_generic_call_dispatches_tool_and_args_json(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    _set_auth_env(monkeypatch)
    captured: dict[str, Any] = {}

    async def fake_execute_operation(tool: str, args: dict[str, Any], config: Any) -> ExecutionResult:
        captured["tool"] = tool
        captured["args"] = args
        return ExecutionResult(payload={"ok": True, "tool": tool, "data": {"ok": 1}}, exit_code=0)

    monkeypatch.setattr(cli, "execute_operation", fake_execute_operation)

    exit_code = cli.run_cli(["call", "--tool", "accept_extras", "--args-json", '{"params":{"id":1}}'])
    _ = capsys.readouterr()

    assert exit_code == 0
    assert captured["tool"] == "accept_extras"
    assert captured["args"] == {"params": {"id": 1}}
