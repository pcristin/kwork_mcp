import importlib.util

import pytest

from kwork.agent.config import ClientConfig
from kwork.agent.mcp_server import MCPServerUnavailableError, build_mcp_server
from kwork.agent.runner import ExecutionPolicy


def test_mcp_builder_raises_when_optional_dependency_missing() -> None:
    if importlib.util.find_spec("mcp") is not None:
        pytest.skip("mcp package is installed; missing-dependency path not applicable")

    with pytest.raises(MCPServerUnavailableError):
        build_mcp_server(
            config=ClientConfig(login="login", password="password"),
            policy=ExecutionPolicy(),
        )


@pytest.mark.skipif(importlib.util.find_spec("mcp") is None, reason="mcp extra not installed")
def test_mcp_builder_smoke_when_dependency_is_available() -> None:
    server = build_mcp_server(
        config=ClientConfig(login="login", password="password"),
        policy=ExecutionPolicy(),
    )
    assert server is not None
