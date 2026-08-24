"""
SentinelAI SDK Exceptions

Custom exceptions for the SentinelAI SDK.
"""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .result import ScanResult


class SentinelSDKError(Exception):
    """Base exception for SentinelAI SDK."""
    pass


class SentinelBlockedError(NovaSDKError):
    """
    Raised when a request is blocked by policy.

    Attributes:
        result: The ScanResult that triggered the block
        message: Human-readable error message
    """

    def __init__(self, result: "ScanResult", message: Optional[str] = None):
        self.result = result
        self.message = message or self._build_message()
        super().__init__(self.message)

    def _build_message(self) -> str:
        """Build default error message from result."""
        blocked_rules = [m.rule_name for m in self.result.matches]
        if blocked_rules:
            return f"Request blocked by SentinelAI: {', '.join(blocked_rules)}"
        return "Request blocked by SentinelAI policy"


class SentinelConfigError(NovaSDKError):
    """Raised for configuration errors."""
    pass


class SentinelRedactionError(NovaSDKError):
    """Raised when redaction fails."""
    pass


class SentinelParseError(NovaSDKError):
    """Raised when rule parsing fails."""
    pass
