from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Sequence

from kwork.agent.config import AgentConfigError, ClientConfig
from kwork.agent.mcp_server import MCPServerUnavailableError, run_mcp_server
from kwork.agent.registry import get_tools
from kwork.agent.runner import ExecutionPolicy, execute_operation
from kwork.agent.tool_docs import render_tools_markdown


class CLIParseError(ValueError):
    pass


class JSONArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise CLIParseError(message)


def _print_json(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")


def _error_payload(err_type: str, message: str) -> dict[str, Any]:
    return {
        "ok": False,
        "error": {
            "type": err_type,
            "message": message,
            "status": None,
            "endpoint": None,
            "details": {},
        },
    }


def _emit_cli_error(err: BaseException, *, exit_code: int = 2) -> int:
    _print_json(_error_payload(type(err).__name__, str(err)))
    return exit_code


def _add_auth_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--login", default=argparse.SUPPRESS)
    parser.add_argument("--password", default=argparse.SUPPRESS)
    parser.add_argument("--phone-last", default=argparse.SUPPRESS)
    parser.add_argument("--proxy", default=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=float, default=argparse.SUPPRESS)
    parser.add_argument("--retry-max-attempts", type=int, default=argparse.SUPPRESS)
    parser.add_argument("--relogin-on-auth-error", action="store_true", default=argparse.SUPPRESS)


def _comma_separated_categories(value: str) -> list[int | str]:
    if value.strip() == "":
        return []
    out: list[int | str] = []
    for item in value.split(","):
        token = item.strip()
        if token == "":
            continue
        try:
            out.append(int(token))
        except ValueError:
            out.append(token)
    return out


def _json_object_arg(value: str) -> dict[str, Any]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as err:
        raise CLIParseError(f"--args-json must be valid JSON: {err.msg}") from err
    if not isinstance(parsed, dict):
        raise CLIParseError("--args-json must decode to a JSON object")
    return parsed


def _build_parser() -> JSONArgumentParser:
    parser = JSONArgumentParser(prog="kwork-agent")
    _add_auth_args(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    me = sub.add_parser("me")
    _add_auth_args(me)
    me.set_defaults(_tool="get_me", _tool_args=lambda ns: {})

    user = sub.add_parser("user")
    _add_auth_args(user)
    user_sub = user.add_subparsers(dest="user_cmd", required=True)
    user_get = user_sub.add_parser("get")
    _add_auth_args(user_get)
    user_get.add_argument("--user-id", type=int, required=True)
    user_get.set_defaults(_tool="get_user", _tool_args=lambda ns: {"user_id": ns.user_id})

    categories = sub.add_parser("categories")
    _add_auth_args(categories)
    categories_sub = categories.add_subparsers(dest="categories_cmd", required=True)
    categories_list = categories_sub.add_parser("list")
    _add_auth_args(categories_list)
    categories_list.set_defaults(_tool="get_categories", _tool_args=lambda ns: {})

    connects = sub.add_parser("connects")
    _add_auth_args(connects)
    connects_sub = connects.add_subparsers(dest="connects_cmd", required=True)
    connects_get = connects_sub.add_parser("get")
    _add_auth_args(connects_get)
    connects_get.set_defaults(_tool="get_connects", _tool_args=lambda ns: {})

    notifications = sub.add_parser("notifications")
    _add_auth_args(notifications)
    notifications_sub = notifications.add_subparsers(dest="notifications_cmd", required=True)
    notifications_get = notifications_sub.add_parser("get")
    _add_auth_args(notifications_get)
    notifications_get.set_defaults(_tool="get_notifications", _tool_args=lambda ns: {})

    orders = sub.add_parser("orders")
    _add_auth_args(orders)
    orders_sub = orders.add_subparsers(dest="orders_cmd", required=True)
    orders_worker = orders_sub.add_parser("worker")
    _add_auth_args(orders_worker)
    orders_worker.set_defaults(_tool="get_worker_orders", _tool_args=lambda ns: {})
    orders_payer = orders_sub.add_parser("payer")
    _add_auth_args(orders_payer)
    orders_payer.set_defaults(_tool="get_payer_orders", _tool_args=lambda ns: {})

    dialogs = sub.add_parser("dialogs")
    _add_auth_args(dialogs)
    dialogs_sub = dialogs.add_subparsers(dest="dialogs_cmd", required=True)
    dialogs_list = dialogs_sub.add_parser("list")
    _add_auth_args(dialogs_list)
    group = dialogs_list.add_mutually_exclusive_group()
    group.add_argument("--page", type=int)
    group.add_argument("--all", action="store_true")
    dialogs_list.add_argument("--excluded-ids")
    dialogs_list.set_defaults(_dispatch="dialogs_list")

    messages = sub.add_parser("messages")
    _add_auth_args(messages)
    messages_sub = messages.add_subparsers(dest="messages_cmd", required=True)
    messages_list = messages_sub.add_parser("list")
    _add_auth_args(messages_list)
    messages_list.add_argument("--username", required=True)
    msg_group = messages_list.add_mutually_exclusive_group()
    msg_group.add_argument("--page", type=int)
    msg_group.add_argument("--all", action="store_true")
    messages_list.set_defaults(_dispatch="messages_list")

    messages_send = messages_sub.add_parser("send")
    _add_auth_args(messages_send)
    messages_send.add_argument("--user-id", type=int, required=True)
    messages_send.add_argument("--text", required=True)
    messages_send.set_defaults(
        _tool="send_message",
        _tool_args=lambda ns: {"user_id": ns.user_id, "text": ns.text},
    )

    projects = sub.add_parser("projects")
    _add_auth_args(projects)
    projects_sub = projects.add_subparsers(dest="projects_cmd", required=True)
    projects_list = projects_sub.add_parser("list")
    _add_auth_args(projects_list)
    projects_list.add_argument("--categories-ids", type=_comma_separated_categories)
    projects_list.add_argument("--price-from", type=int)
    projects_list.add_argument("--price-to", type=int)
    projects_list.add_argument("--hiring-from", type=int)
    projects_list.add_argument("--kworks-filter-from", type=int)
    projects_list.add_argument("--kworks-filter-to", type=int)
    projects_list.add_argument("--page", type=int)
    projects_list.add_argument("--query")
    projects_list.set_defaults(
        _tool="get_projects",
        _tool_args=lambda ns: {
            "categories_ids": ns.categories_ids if ns.categories_ids is not None else [],
            "price_from": ns.price_from,
            "price_to": ns.price_to,
            "hiring_from": ns.hiring_from,
            "kworks_filter_from": ns.kworks_filter_from,
            "kworks_filter_to": ns.kworks_filter_to,
            "page": ns.page,
            "query": ns.query,
        },
    )

    tools = sub.add_parser("tools")
    tools_sub = tools.add_subparsers(dest="tools_cmd", required=True)
    tools_list = tools_sub.add_parser("list")
    tools_list.add_argument("--include-write", action="store_true")
    tools_list.set_defaults(_dispatch="tools_list")
    tools_export = tools_sub.add_parser("export-markdown")
    tools_export.add_argument("--include-write", action="store_true")
    tools_export.add_argument("--output")
    tools_export.set_defaults(_dispatch="tools_export_markdown")

    call = sub.add_parser("call")
    _add_auth_args(call)
    call.add_argument("--tool", required=True)
    call.add_argument("--args-json", type=_json_object_arg, default={})
    call.set_defaults(_dispatch="generic_call")

    mcp = sub.add_parser("mcp")
    _add_auth_args(mcp)
    mcp_sub = mcp.add_subparsers(dest="mcp_cmd", required=True)
    mcp_serve = mcp_sub.add_parser("serve")
    _add_auth_args(mcp_serve)
    mcp_serve.add_argument("--enable-write-tools", action="store_true")
    mcp_serve.add_argument("--allow-tools")
    mcp_serve.set_defaults(_dispatch="mcp_serve")

    return parser


def _resolve_client_config(ns: argparse.Namespace) -> ClientConfig:
    return ClientConfig.from_sources(
        login=getattr(ns, "login", None),
        password=getattr(ns, "password", None),
        phone_last=getattr(ns, "phone_last", None),
        proxy=getattr(ns, "proxy", None),
        timeout=getattr(ns, "timeout", None),
        retry_max_attempts=getattr(ns, "retry_max_attempts", None),
        relogin_on_auth_error=(
            getattr(ns, "relogin_on_auth_error", False)
            if getattr(ns, "relogin_on_auth_error", False)
            else None
        ),
    )


def _dispatch_tool(ns: argparse.Namespace) -> tuple[str, dict[str, Any]]:
    dispatch = getattr(ns, "_dispatch", None)
    if dispatch == "generic_call":
        return ns.tool, dict(ns.args_json)
    if dispatch == "dialogs_list":
        if ns.all:
            return "get_all_dialogs", {}
        return "get_dialogs_page", {"page": ns.page or 1, "excluded_ids": ns.excluded_ids}
    if dispatch == "messages_list":
        if ns.all:
            return "get_dialog_with_user", {"username": ns.username}
        return "get_dialog_with_user_page", {"username": ns.username, "page": ns.page or 1}

    tool = getattr(ns, "_tool", None)
    tool_args_builder = getattr(ns, "_tool_args", None)
    if tool is None or tool_args_builder is None:
        raise CLIParseError("Unknown command")
    return tool, tool_args_builder(ns)


def _parse_allow_tools(raw: str | None) -> frozenset[str] | None:
    if raw is None:
        return None
    tools = [item.strip() for item in raw.split(",") if item.strip()]
    return frozenset(tools)


def _mcp_write_enabled(ns: argparse.Namespace) -> bool:
    if ns.enable_write_tools:
        return True
    env_value = os.environ.get("KWORK_MCP_ENABLE_WRITE_TOOLS")
    return str(env_value).strip().lower() in {"1", "true", "yes", "on"}


def run_cli(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    try:
        ns = parser.parse_args(list(argv) if argv is not None else None)
    except CLIParseError as err:
        return _emit_cli_error(err, exit_code=2)

    try:
        if getattr(ns, "_dispatch", None) == "tools_list":
            tools_payload = [
                {"name": t.name, "is_write": t.is_write, "description": t.description}
                for t in get_tools()
                if ns.include_write or not t.is_write
            ]
            _print_json({"ok": True, "tool": "tools_list", "data": tools_payload})
            return 0

        if getattr(ns, "_dispatch", None) == "tools_export_markdown":
            markdown = render_tools_markdown(include_write=ns.include_write)
            if ns.output:
                output_path = Path(ns.output)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(markdown + "\n", encoding="utf-8")
                _print_json(
                    {
                        "ok": True,
                        "tool": "tools_export_markdown",
                        "data": {"path": str(output_path), "bytes": len(markdown.encode("utf-8"))},
                    }
                )
                return 0
            sys.stdout.write(markdown + "\n")
            return 0

        if getattr(ns, "_dispatch", None) == "mcp_serve":
            config = _resolve_client_config(ns)
            policy = ExecutionPolicy(
                allow_write_tools=_mcp_write_enabled(ns),
                allow_tools=_parse_allow_tools(ns.allow_tools),
            )
            return run_mcp_server(config=config, policy=policy)

        config = _resolve_client_config(ns)
        tool_name, tool_args = _dispatch_tool(ns)
        result = asyncio.run(execute_operation(tool_name, tool_args, config))
        _print_json(result.payload)
        return result.exit_code
    except MCPServerUnavailableError as err:
        return _emit_cli_error(err, exit_code=2)
    except AgentConfigError as err:
        return _emit_cli_error(err, exit_code=2)
    except CLIParseError as err:
        return _emit_cli_error(err, exit_code=2)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(argv)


def main_mcp(argv: Sequence[str] | None = None) -> int:
    prefixed = ["mcp", "serve"]
    if argv is not None:
        prefixed.extend(argv)
    return run_cli(prefixed)
