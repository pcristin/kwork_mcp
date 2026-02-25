import json

import pytest

from kwork.agent.tool_docs import render_tools_markdown


def test_render_tools_markdown_contains_known_tools() -> None:
    out = render_tools_markdown(include_write=True)

    assert out.startswith("# Agent Tools")
    assert "## Read Tools" in out
    assert "## Write Tools" in out
    assert "### `get_me`" in out
    assert "### `accept_extras`" in out
    assert "### `web_submit_exchange_offer`" in out


def test_render_tools_markdown_can_exclude_write_tools() -> None:
    out = render_tools_markdown(include_write=False)
    assert "## Write Tools" in out
    # Empty write section is allowed, but write tool entries should be absent.
    assert "### `accept_extras`" not in out


def test_cli_tools_export_markdown_output_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from kwork.agent import cli

    output_path = tmp_path / "agent-tools.md"
    exit_code = cli.run_cli(["tools", "export-markdown", "--output", str(output_path)])
    out = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert out["ok"] is True
    assert out["tool"] == "tools_export_markdown"
    assert output_path.exists()
    content = output_path.read_text(encoding="utf-8")
    assert content.startswith("# Agent Tools")
