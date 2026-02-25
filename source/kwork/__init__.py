from kwork.api import KworkAPI
from kwork.client import KworkClient
from kwork.web_client import KworkWebClient, WebLoginResult

Kwork = KworkClient


def __getattr__(name: str):
    if name == "KworkBot":
        from kwork.bot import KworkBot

        return KworkBot
    raise AttributeError(f"module 'kwork' has no attribute {name!r}")

__all__ = (
    "Kwork",
    "KworkAPI",
    "KworkBot",
    "KworkClient",
    "KworkWebClient",
    "WebLoginResult",
)
