from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Any, Literal, get_args, get_origin

from kwork.client import KworkClient
from kwork.web_client import KworkWebClient

JsonType = Literal["string", "integer", "number", "boolean", "array"]
ParamType = Literal["str", "int", "float", "bool", "int_or_str_list", "object", "array", "json"]
ToolHandler = Callable[[KworkClient, dict[str, Any]], Awaitable[Any]]


class ToolValidationError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class ParamSpec:
    name: str
    kind: ParamType
    description: str
    required: bool = False
    default: Any = None

    def to_json_schema(self) -> dict[str, Any]:
        if self.kind == "str":
            schema: dict[str, Any] = {"type": "string"}
        elif self.kind == "int":
            schema = {"type": "integer"}
        elif self.kind == "float":
            schema = {"type": "number"}
        elif self.kind == "bool":
            schema = {"type": "boolean"}
        elif self.kind == "int_or_str_list":
            schema = {
                "type": "array",
                "items": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
            }
        elif self.kind == "object":
            schema = {"type": "object"}
        elif self.kind == "array":
            schema = {"type": "array", "items": {}}
        elif self.kind == "json":
            schema = {
                "anyOf": [
                    {"type": "string"},
                    {"type": "integer"},
                    {"type": "number"},
                    {"type": "boolean"},
                    {"type": "object"},
                    {"type": "array"},
                    {"type": "null"},
                ]
            }
        else:
            raise AssertionError(f"Unsupported param kind: {self.kind}")
        schema["description"] = self.description
        return schema

    def coerce(self, value: Any) -> Any:
        if value is None:
            if self.required:
                raise ToolValidationError(f"Missing required parameter: {self.name}")
            if isinstance(self.default, list):
                return list(self.default)
            if isinstance(self.default, dict):
                return dict(self.default)
            return self.default

        if self.kind == "str":
            if not isinstance(value, str):
                raise ToolValidationError(f"Parameter {self.name} must be a string")
            return value

        if self.kind == "int":
            if isinstance(value, bool):
                raise ToolValidationError(f"Parameter {self.name} must be an integer")
            if isinstance(value, int):
                return value
            if isinstance(value, str):
                try:
                    return int(value)
                except ValueError as err:
                    raise ToolValidationError(f"Parameter {self.name} must be an integer") from err
            raise ToolValidationError(f"Parameter {self.name} must be an integer")

        if self.kind == "float":
            if isinstance(value, bool):
                raise ToolValidationError(f"Parameter {self.name} must be a number")
            if isinstance(value, (int, float)):
                return float(value)
            if isinstance(value, str):
                try:
                    return float(value)
                except ValueError as err:
                    raise ToolValidationError(f"Parameter {self.name} must be a number") from err
            raise ToolValidationError(f"Parameter {self.name} must be a number")

        if self.kind == "bool":
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                lowered = value.strip().lower()
                if lowered in {"1", "true", "yes", "on"}:
                    return True
                if lowered in {"0", "false", "no", "off"}:
                    return False
            raise ToolValidationError(f"Parameter {self.name} must be a boolean")

        if self.kind == "int_or_str_list":
            if not isinstance(value, list):
                raise ToolValidationError(f"Parameter {self.name} must be an array")
            out: list[int | str] = []
            for item in value:
                if isinstance(item, bool):
                    raise ToolValidationError(
                        f"Parameter {self.name} items must be integers or strings"
                    )
                if isinstance(item, (int, str)):
                    out.append(item)
                    continue
                raise ToolValidationError(
                    f"Parameter {self.name} items must be integers or strings"
                )
            return out

        if self.kind == "object":
            if not isinstance(value, dict):
                raise ToolValidationError(f"Parameter {self.name} must be an object")
            return value

        if self.kind == "array":
            if not isinstance(value, list):
                raise ToolValidationError(f"Parameter {self.name} must be an array")
            return value

        if self.kind == "json":
            return value

        raise AssertionError(f"Unsupported param kind: {self.kind}")


@dataclass(frozen=True, slots=True)
class ToolSpec:
    name: str
    description: str
    is_write: bool
    params: tuple[ParamSpec, ...]
    handler: ToolHandler
    extra_kwargs_param: str | None = None

    @property
    def mcp_input_schema(self) -> dict[str, Any]:
        properties = {param.name: param.to_json_schema() for param in self.params}
        required = [param.name for param in self.params if param.required]
        schema: dict[str, Any] = {
            "type": "object",
            "properties": properties,
            "additionalProperties": False,
        }
        if required:
            schema["required"] = required
        return schema

    def validate_args(self, raw_args: Mapping[str, Any] | None) -> dict[str, Any]:
        data = dict(raw_args or {})
        unknown = sorted(set(data) - {p.name for p in self.params})
        if unknown:
            joined = ", ".join(unknown)
            raise ToolValidationError(f"Unknown parameter(s) for {self.name}: {joined}")

        out: dict[str, Any] = {}
        for param in self.params:
            value = data.get(param.name)
            coerced = param.coerce(value)
            if coerced is None and not param.required and param.default is None:
                continue
            out[param.name] = coerced
        return out


async def _call_no_args(client: KworkClient, _: dict[str, Any], method_name: str) -> Any:
    method = getattr(client, method_name)
    return await method()


def _simple_tool(
    *,
    name: str,
    description: str,
    method_name: str,
    is_write: bool = False,
    params: tuple[ParamSpec, ...] = (),
) -> ToolSpec:
    async def handler(client: KworkClient, args: dict[str, Any]) -> Any:
        method = getattr(client, method_name)
        return await method(**args)

    return ToolSpec(
        name=name,
        description=description,
        is_write=is_write,
        params=params,
        handler=handler,
    )


def _dynamic_tool(
    *,
    name: str,
    description: str,
    method_name: str,
    params: tuple[ParamSpec, ...],
    is_write: bool,
    web_method: bool = False,
    extra_kwargs_param: str | None = None,
) -> ToolSpec:
    async def handler(client: KworkClient, args: dict[str, Any]) -> Any:
        call_args = dict(args)
        if extra_kwargs_param is not None:
            extra = call_args.pop(extra_kwargs_param, None)
            if extra:
                if not isinstance(extra, dict):
                    raise ToolValidationError(f"Parameter {extra_kwargs_param} must be an object")
                call_args.update(extra)
        target: Any = client.web if web_method else client
        method = getattr(target, method_name)
        return await method(**call_args)

    return ToolSpec(
        name=name,
        description=description,
        is_write=is_write,
        params=params,
        handler=handler,
        extra_kwargs_param=extra_kwargs_param,
    )


_CURATED_TOOLS: tuple[ToolSpec, ...] = (
    _simple_tool(name="get_me", description="Get current user profile.", method_name="get_me"),
    _simple_tool(
        name="get_user",
        description="Get user profile by user ID.",
        method_name="get_user",
        params=(
            ParamSpec(name="user_id", kind="int", description="Kwork user ID.", required=True),
        ),
    ),
    _simple_tool(
        name="get_categories",
        description="List Kwork categories.",
        method_name="get_categories",
    ),
    _simple_tool(
        name="get_connects",
        description="Get remaining connects info.",
        method_name="get_connects",
    ),
    _simple_tool(
        name="get_notifications",
        description="Get notifications payload.",
        method_name="get_notifications",
    ),
    _simple_tool(
        name="get_worker_orders",
        description="Get worker orders.",
        method_name="get_worker_orders",
    ),
    _simple_tool(
        name="get_payer_orders",
        description="Get payer orders.",
        method_name="get_payer_orders",
    ),
    _simple_tool(
        name="get_dialogs_page",
        description="Get a page of dialogs.",
        method_name="get_dialogs_page",
        params=(
            ParamSpec(
                name="page",
                kind="int",
                description="Dialogs page number (1-based).",
                required=False,
                default=1,
            ),
            ParamSpec(
                name="excluded_ids",
                kind="str",
                description="Comma-separated excluded dialog IDs.",
                required=False,
                default=None,
            ),
        ),
    ),
    _simple_tool(
        name="get_all_dialogs",
        description="Get all dialogs by paginating until empty page.",
        method_name="get_all_dialogs",
    ),
    _simple_tool(
        name="get_dialog_with_user_page",
        description="Get a page of dialog messages by username.",
        method_name="get_dialog_with_user_page",
        params=(
            ParamSpec(
                name="username",
                kind="str",
                description="Kwork username.",
                required=True,
            ),
            ParamSpec(
                name="page",
                kind="int",
                description="Messages page number (1-based).",
                required=False,
                default=1,
            ),
        ),
    ),
    _simple_tool(
        name="get_dialog_with_user",
        description="Get full dialog with user by username.",
        method_name="get_dialog_with_user",
        params=(
            ParamSpec(
                name="username",
                kind="str",
                description="Kwork username.",
                required=True,
            ),
        ),
    ),
    _simple_tool(
        name="get_projects",
        description="List exchange projects with filters.",
        method_name="get_projects",
        params=(
            ParamSpec(
                name="categories_ids",
                kind="int_or_str_list",
                description="Array of category IDs or strings; empty means favorites.",
                required=False,
                default=[],
            ),
            ParamSpec(name="price_from", kind="int", description="Minimum price.", default=None),
            ParamSpec(name="price_to", kind="int", description="Maximum price.", default=None),
            ParamSpec(
                name="hiring_from",
                kind="int",
                description="Minimum hiring percent.",
                default=None,
            ),
            ParamSpec(
                name="kworks_filter_from",
                kind="int",
                description="Minimum offers count (exclusive).",
                default=None,
            ),
            ParamSpec(
                name="kworks_filter_to",
                kind="int",
                description="Maximum offers count (inclusive).",
                default=None,
            ),
            ParamSpec(name="page", kind="int", description="Projects page number.", default=None),
            ParamSpec(name="query", kind="str", description="Search query.", default=None),
        ),
    ),
    _simple_tool(
        name="send_message",
        description="Send a message to a user.",
        method_name="send_message",
        is_write=True,
        params=(
            ParamSpec(name="user_id", kind="int", description="Recipient user ID.", required=True),
            ParamSpec(name="text", kind="str", description="Message text.", required=True),
        ),
    ),
)

_EXCLUDED_CLIENT_METHODS: frozenset[str] = frozenset(
    {
        "close",
        "get_token",
        "request",
        "request_with_body",
        "request_multipart",
    }
)

_EXCLUDED_WEB_METHODS: frozenset[str] = frozenset({"request"})

_READ_NAME_PREFIXES: tuple[str, ...] = (
    "get_",
    "check_",
    "catalog_",
)

_READ_NAME_EXACT: frozenset[str] = frozenset(
    {
        "actor",
        "categories",
        "category",
        "cities",
        "countries",
        "dialogs",
        "exchange_info",
        "favorite_categories",
        "favorite_kworks",
        "inboxes",
        "kworks",
        "my_wants",
        "notifications",
        "offers",
        "order",
        "orders_between",
        "portfolio_list",
        "positive_reviews_count",
        "privacy",
        "project",
        "projects",
        "resolution",
        "quick_faq_init",
        "check_is_template",
    }
)

_WRITE_NAME_PREFIXES: tuple[str, ...] = (
    "accept_",
    "add_",
    "allow_",
    "apple_sign_in",
    "approve_",
    "archive_",
    "block_",
    "cancel_",
    "change_",
    "clear_",
    "confirm_",
    "create_",
    "del_",
    "delete_",
    "edit_",
    "fcm_",
    "file_",
    "hide_",
    "inbox_",
    "logout",
    "mark_",
    "open_",
    "order_",
    "pause_",
    "pay_",
    "payer_",
    "push_",
    "rate_",
    "recharge_",
    "register_",
    "reject_",
    "repeat_",
    "replace_",
    "report_",
    "request_",
    "reset_",
    "restart_",
    "save_",
    "send_",
    "set_",
    "submit_",
)


def _annotation_to_kind(annotation: Any, default: Any) -> ParamType:
    if annotation is inspect.Signature.empty:
        if isinstance(default, bool):
            return "bool"
        if isinstance(default, int) and not isinstance(default, bool):
            return "int"
        if isinstance(default, float):
            return "float"
        if isinstance(default, str):
            return "str"
        if isinstance(default, dict):
            return "object"
        if isinstance(default, list):
            return "array"
        return "json"

    if isinstance(annotation, str):
        ann = annotation.replace("typing.", "").replace(" ", "")
        if "list[int|str]" in ann or "list[str|int]" in ann:
            return "int_or_str_list"
        if "dict[" in ann or ann == "dict" or "mapping[" in ann.lower():
            return "object"
        if "list[" in ann or "tuple[" in ann or "sequence[" in ann.lower():
            return "array"
        if "bool" in ann:
            return "bool"
        # Prefer string over int for unions like "str | None".
        if "str" in ann:
            return "str"
        if "int" in ann and "ClientTimeout" not in ann:
            return "int"
        if "float" in ann:
            return "float"
        return "json"

    origin = get_origin(annotation)
    if origin is None:
        if annotation is bool:
            return "bool"
        if annotation is str:
            return "str"
        if annotation is int:
            return "int"
        if annotation is float:
            return "float"
        if annotation is dict:
            return "object"
        if annotation is list:
            return "array"
        return "json"

    if origin in (dict, Mapping):
        return "object"
    if origin in (list, tuple):
        args = get_args(annotation)
        if origin is list and args:
            item = args[0]
            item_origin = get_origin(item)
            item_args = get_args(item)
            if item_origin is None and item in (int, str):
                return "array"
            if item_args and set(item_args) == {int, str}:
                return "int_or_str_list"
        return "array"

    args = get_args(annotation)
    if args:
        filtered = [arg for arg in args if arg is not type(None)]
        if len(filtered) == 1:
            return _annotation_to_kind(filtered[0], default)
        if set(filtered) == {int, str}:
            return "json"
        for candidate in (str, bool, int, float):
            if candidate in filtered:
                return _annotation_to_kind(candidate, default)
        return "json"

    return "json"


def _param_spec_from_signature_param(param: inspect.Parameter) -> tuple[ParamSpec | None, str | None]:
    if param.kind == inspect.Parameter.VAR_POSITIONAL:
        return None, None

    required = param.default is inspect.Parameter.empty
    default = None if required else param.default

    if param.kind == inspect.Parameter.VAR_KEYWORD:
        # Expose catch-all kwargs as a single object field to keep MCP/CLI JSON-friendly.
        return (
            ParamSpec(
                name=param.name,
                kind="object",
                description="Additional keyword arguments passed through to the underlying method.",
                required=False,
                default={},
            ),
            param.name,
        )

    kind = _annotation_to_kind(param.annotation, default)
    return (
        ParamSpec(
            name=param.name,
            kind=kind,
            description=f"Parameter `{param.name}` for the underlying method.",
            required=required,
            default=default,
        ),
        None,
    )


def _is_read_method_name(name: str) -> bool:
    if name in _READ_NAME_EXACT:
        return True
    if any(name.startswith(prefix) for prefix in _READ_NAME_PREFIXES):
        return True
    if any(name.startswith(prefix) for prefix in _WRITE_NAME_PREFIXES):
        return False
    # Conservative default: unknown methods are treated as write-capable.
    return False


def _build_dynamic_tools() -> tuple[ToolSpec, ...]:
    curated_names = {tool.name for tool in _CURATED_TOOLS}
    tools: list[ToolSpec] = []

    for method_name, method in inspect.getmembers(KworkClient, predicate=inspect.iscoroutinefunction):
        if method_name.startswith("_") or method_name in _EXCLUDED_CLIENT_METHODS:
            continue
        if method_name in curated_names:
            continue

        sig = inspect.signature(method)
        params: list[ParamSpec] = []
        extra_kwargs_param: str | None = None
        for p in sig.parameters.values():
            if p.name == "self":
                continue
            spec, var_kw = _param_spec_from_signature_param(p)
            if spec is not None:
                params.append(spec)
            if var_kw is not None:
                extra_kwargs_param = var_kw

        tools.append(
            _dynamic_tool(
                name=method_name,
                description=f"Auto-exposed KworkClient.{method_name}()",
                method_name=method_name,
                params=tuple(params),
                is_write=not _is_read_method_name(method_name),
                extra_kwargs_param=extra_kwargs_param,
            )
        )

    for method_name, method in inspect.getmembers(KworkWebClient, predicate=inspect.iscoroutinefunction):
        if method_name.startswith("_") or method_name in _EXCLUDED_WEB_METHODS:
            continue
        tool_name = f"web_{method_name}"
        if tool_name in curated_names:
            continue

        sig = inspect.signature(method)
        params = []
        extra_kwargs_param: str | None = None
        for p in sig.parameters.values():
            if p.name == "self":
                continue
            spec, var_kw = _param_spec_from_signature_param(p)
            if spec is not None:
                params.append(spec)
            if var_kw is not None:
                extra_kwargs_param = var_kw

        tools.append(
            _dynamic_tool(
                name=tool_name,
                description=f"Auto-exposed KworkWebClient.{method_name}()",
                method_name=method_name,
                params=tuple(params),
                is_write=not _is_read_method_name(method_name),
                web_method=True,
                extra_kwargs_param=extra_kwargs_param,
            )
        )

    tools.sort(key=lambda t: t.name)
    return tuple(tools)


_TOOLS: tuple[ToolSpec, ...] = _CURATED_TOOLS + _build_dynamic_tools()
_TOOLS_BY_NAME: dict[str, ToolSpec] = {tool.name: tool for tool in _TOOLS}


def get_tools() -> tuple[ToolSpec, ...]:
    return _TOOLS


def get_tool(name: str) -> ToolSpec:
    try:
        return _TOOLS_BY_NAME[name]
    except KeyError as err:
        raise ToolValidationError(f"Unknown tool: {name}") from err
