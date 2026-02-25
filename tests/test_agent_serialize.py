from kwork.agent.serialize import serialize_result
from kwork.schema import DialogMessage


def test_serialize_result_handles_pydantic_and_nested_values() -> None:
    dialog = DialogMessage(user_id=123, username="alice")
    payload = {
        "dialog": dialog,
        "items": [dialog, ("x", 1)],
        "none": None,
    }

    out = serialize_result(payload)

    assert out["dialog"]["user_id"] == 123
    assert out["dialog"]["username"] == "alice"
    assert out["items"][0]["user_id"] == 123
    # Tuples are normalized to JSON-friendly arrays.
    assert out["items"][1] == ["x", 1]
    assert out["none"] is None
