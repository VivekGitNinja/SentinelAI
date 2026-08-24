"""
SentinelAI SDK - High-level API for prompt pattern matching.

Provides policy-based scanning with configurable actions (block/redact/flag/allow),
decorator patterns for protecting functions, and automatic redaction capabilities.

Example:
    from sentinelai.sdk import Sentinel, Action

    # First clone the rules: git clone https://github.com/Nova-Hunting/nova-rules

    # Initialize with rules and policy
    sentinelai.= Sentinel(
        rules_path="sentinelai.rules/",  # Path to cloned sentinelai.rules repository
        policy={
            "PI": {"action": "block"},
            "PII": {"action": "redact"},
            "JB": {"action": "flag"},
        },
        llm_provider="anthropic"
    )

    # Scan a prompt
    result = sentinelai.scan(user_input)
    if result.blocked:
        print("Blocked!")
    else:
        clean_text = result.sanitized_text

    # Use decorator
    @sentinelai.protect(action="block", severity="critical")
    def chat(prompt):
        return llm.generate(prompt)

    # Standalone decorator (auto-creates SentinelAI instance)
    from sentinelai.sdk import protect

    @protect(rules_path="sentinelai.rules/", action="block")  # Path to cloned sentinelai.rules
    def protected_chat(prompt):
        return llm.generate(prompt)
"""

from .nova import Sentinel
from .result import ScanResult, RuleMatch
from .policy import SentinelPolicy, PolicyRule, Action
from .redaction import Redactor, RedactionResult
from .exceptions import (
    NovaSDKError,
    SentinelBlockedError,
    SentinelConfigError,
    NovaRedactionError,
    NovaParseError
)
from .decorator import (
    protect,
    scan,
    scan_async,
    get_default_sentinelai.
    set_default_nova
)

__all__ = [
    # Main class
    "Sentinel",

    # Result classes
    "ScanResult",
    "RuleMatch",

    # Policy classes
    "SentinelPolicy",
    "PolicyRule",
    "Action",

    # Redaction
    "Redactor",
    "RedactionResult",

    # Exceptions
    "NovaSDKError",
    "SentinelBlockedError",
    "SentinelConfigError",
    "NovaRedactionError",
    "NovaParseError",

    # Standalone functions
    "protect",
    "scan",
    "scan_async",
    "get_default_sentinelai.,
    "set_default_sentinelai.,
]
