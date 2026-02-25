from __future__ import annotations

import inspect
from typing import Any

from kwork.agent.config import ClientConfig
from kwork.agent.registry import ParamSpec, ToolSpec, get_tools
from kwork.agent.runner import ExecutionPolicy, execute_operation


class MCPServerUnavailableError(ImportError):
    """Raised when optional MCP dependency is not installed."""


def _load_fastmcp() -> Any:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as err:  # pragma: no cover - depends on optional extra
        raise MCPServerUnavailableError(
            'MCP server support requires optional dependency "mcp". Install with: pip install "kwork[mcp]"'
        ) from err
    return FastMCP


def _annotation_for_param(param: ParamSpec) -> Any:
    if param.kind == "str":
        return str
    if param.kind == "int":
        return int
    if param.kind == "float":
        return float
    if param.kind == "bool":
        return bool
    if param.kind == "int_or_str_list":
        return list[int | str]
    return Any


def _build_signature(spec: ToolSpec) -> inspect.Signature:
    params: list[inspect.Parameter] = []
    for param in spec.params:
        default = inspect.Parameter.empty if param.required else param.default
        params.append(
            inspect.Parameter(
                name=param.name,
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=default,
                annotation=_annotation_for_param(param),
            )
        )
    return inspect.Signature(parameters=params, return_annotation=dict[str, Any])


def _make_tool_callable(
    *,
    tool: ToolSpec,
    config: ClientConfig,
    policy: ExecutionPolicy,
) -> Any:
    async def _tool(**kwargs: Any) -> dict[str, Any]:
        result = await execute_operation(tool.name, kwargs, config, policy=policy)
        return result.payload

    _tool.__name__ = tool.name
    _tool.__qualname__ = tool.name
    _tool.__doc__ = tool.description
    _tool.__annotations__ = {param.name: _annotation_for_param(param) for param in tool.params}
    _tool.__annotations__["return"] = dict[str, Any]
    _tool.__signature__ = _build_signature(tool)  # type: ignore[attr-defined]
    return _tool


def build_mcp_server(
    *,
    config: ClientConfig,
    policy: ExecutionPolicy,
    server_name: str = "kwork-agent",
) -> Any:
    FastMCP = _load_fastmcp()
    server = FastMCP(server_name)

    for tool in get_tools():
        func = _make_tool_callable(tool=tool, config=config, policy=policy)
        try:
            decorator = server.tool(name=tool.name, description=tool.description)
        except TypeError:
            decorator = server.tool(name=tool.name)
        decorator(func)

    return server


def run_mcp_server(
    *,
    config: ClientConfig,
    policy: ExecutionPolicy,
    server_name: str = "kwork-agent",
) -> int:
    server = build_mcp_server(config=config, policy=policy, server_name=server_name)
    server.run()
    return 0
