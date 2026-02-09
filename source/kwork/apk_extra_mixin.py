from __future__ import annotations

from typing import Any, Protocol


class _APIProto(Protocol):
    async def request(
        self,
        method: str,
        endpoint: str,
        use_token: bool = False,
        **params: Any,
    ) -> dict[str, Any]: ...


class APKExtraMethodsMixin(_APIProto):
    """
    Endpoints found in the decompiled app but missing from docs/openapi.json.

    These are thin wrappers around `request(...)`.
    """

    async def get_public_features(
        self, *, use_token: bool = False, **params: Any
    ) -> dict[str, Any]:
        """POST /getPublicFeatures - auth: basic (per APK)"""
        return await self.request("post", "getPublicFeatures", use_token=use_token, **params)

    async def tos(self, *, use_token: bool = False, **params: Any) -> dict[str, Any]:
        """POST /tos - auth: basic (per APK)"""
        return await self.request("post", "tos", use_token=use_token, **params)

    async def validate_event(self, *, use_token: bool = True, **params: Any) -> dict[str, Any]:
        """POST /validateEvent - auth: token+basic (per APK)"""
        return await self.request("post", "validateEvent", use_token=use_token, **params)
