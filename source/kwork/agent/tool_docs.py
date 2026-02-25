from __future__ import annotations

import json
from typing import Iterable

from kwork.agent.registry import ToolSpec, get_tools


def _schema_json(schema: dict) -> str:
    return json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True)


def render_tools_markdown(*, include_write: bool = True, tools: Iterable[ToolSpec] | None = None) -> str:
    all_tools = list(get_tools() if tools is None else tools)
    if not include_write:
        all_tools = [tool for tool in all_tools if not tool.is_write]

    read_tools = [tool for tool in all_tools if not tool.is_write]
    write_tools = [tool for tool in all_tools if tool.is_write]
    lines: list[str] = []
    lines.append("# Agent Tools")
    lines.append("")
    lines.append("Auto-generated tool reference for `kwork-agent` / MCP server.")
    lines.append("")
    lines.append(f"- Total tools: `{len(all_tools)}`")
    lines.append(f"- Read tools: `{len(read_tools)}`")
    lines.append(f"- Write tools: `{len(write_tools)}`")
    lines.append("")
    lines.append("Regenerate:")
    lines.append("")
    lines.append("```bash")
    if include_write:
        lines.append("kwork-agent tools export-markdown --include-write")
    else:
        lines.append("kwork-agent tools export-markdown")
    lines.append("```")
    lines.append("")

    def add_tool_section(title: str, section_tools: list[ToolSpec]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not section_tools:
            lines.append("_None_")
            lines.append("")
            return

        for tool in section_tools:
            lines.append(f"### `{tool.name}`")
            lines.append("")
            lines.append(f"- Description: {tool.description}")
            lines.append(f"- Access: {'write' if tool.is_write else 'read'}")
            lines.append(f"- Parameter count: {len(tool.params)}")
            lines.append("")

            if tool.params:
                lines.append("| Parameter | Type | Required | Default |")
                lines.append("|---|---|---:|---|")
                for param in tool.params:
                    default_repr = "`-`"
                    if not param.required:
                        if param.default is None:
                            default_repr = "`null`"
                        else:
                            default_repr = f"`{param.default!r}`"
                    lines.append(
                        f"| `{param.name}` | `{param.kind}` | {'yes' if param.required else 'no'} | {default_repr} |"
                    )
                lines.append("")
            else:
                lines.append("Parameters: none")
                lines.append("")

            lines.append("MCP input schema:")
            lines.append("")
            lines.append("```json")
            lines.append(_schema_json(tool.mcp_input_schema))
            lines.append("```")
            lines.append("")

    add_tool_section("Read Tools", read_tools)
    add_tool_section("Write Tools", write_tools)
    return "\n".join(lines)
