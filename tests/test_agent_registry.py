import pytest

from kwork.agent.registry import ToolValidationError, get_tool, get_tools


def test_registry_contains_expected_v1_tools() -> None:
    names = {tool.name for tool in get_tools()}
    assert "get_me" in names
    assert "get_projects" in names
    assert "send_message" in names
    assert "accept_extras" in names
    assert "web_submit_exchange_offer" in names


def test_registry_excludes_low_level_transport_methods() -> None:
    names = {tool.name for tool in get_tools()}
    assert "request" not in names
    assert "request_with_body" not in names
    assert "request_multipart" not in names
    assert "web_request" not in names
    assert "close" not in names


def test_get_dialogs_page_validation_applies_defaults() -> None:
    tool = get_tool("get_dialogs_page")
    args = tool.validate_args({})

    assert args["page"] == 1
    assert "excluded_ids" not in args


def test_send_message_requires_fields() -> None:
    tool = get_tool("send_message")
    with pytest.raises(ToolValidationError):
        tool.validate_args({"user_id": 1})


def test_registry_rejects_unknown_parameters() -> None:
    tool = get_tool("get_me")
    with pytest.raises(ToolValidationError):
        tool.validate_args({"extra": 1})


def test_dynamic_tool_with_var_kwargs_accepts_params_object() -> None:
    tool = get_tool("accept_extras")
    args = tool.validate_args({"use_token": True, "params": {"order_id": 1}})
    assert args["use_token"] is True
    assert args["params"] == {"order_id": 1}
