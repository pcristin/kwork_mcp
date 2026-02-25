from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def _is_pydantic_model(value: Any) -> bool:
    return callable(getattr(value, "model_dump", None))


def serialize_result(value: Any) -> Any:
    if _is_pydantic_model(value):
        dumped = value.model_dump(by_alias=True, mode="json")
        return serialize_result(dumped)

    if isinstance(value, Mapping):
        return {str(k): serialize_result(v) for k, v in value.items()}

    if isinstance(value, (str, int, float, bool)) or value is None:
        return value

    if isinstance(value, tuple):
        return [serialize_result(v) for v in value]

    if isinstance(value, Sequence):
        return [serialize_result(v) for v in value]

    return repr(value)
