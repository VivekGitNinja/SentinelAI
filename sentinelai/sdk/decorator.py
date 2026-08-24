"""
SentinelAI SDK Standalone Decorator

Standalone protect decorator for simpler usage without creating Sentinel instance first.
"""

from typing import TYPE_CHECKING, Union, Optional, Callable, List
from pathlib import Path

from .policy import Action

if TYPE_CHECKING:
    from .nova import Sentinel
    from .result import ScanResult


# Global Sentinel instance for standalone decorator
_default_sentinel: Optional["Sentinel"] = None


def get_default_sentinel() -> "Sentinel":
    """Get or create the default Sentinel instance."""
    global _default_sentinel
    if _default_sentinel is None:
        from .nova import Sentinel
        _default_sentinel = Sentinel()
    return _default_sentinel


def set_default_sentinel(sentinel: "Sentinel") -> None:
    """
    Set the default Sentinel instance for standalone decorator.

    Args:
        sentinel: Sentinel instance to use as default
    """
    global _default_sentinel
    _default_sentinel = sentinel


def protect(
    rules_path: Optional[Union[str, Path, List[str]]] = None,
    policy: Optional[dict] = None,
    action: Union[str, Action] = Action.FLAG,
    severity: Optional[str] = None,
    param_name: str = "prompt",
    on_block: Optional[Callable] = None,
    raise_on_block: bool = True,
    sentinel_instance: Optional["Sentinel"] = None,
    llm_provider: Optional[str] = None,
    llm_model: Optional[str] = None,
):
    """
    Standalone decorator to protect functions with SentinelAI scanning.

    Can be used without creating a Sentinel instance first. If rules_path or policy
    are provided, creates a new Sentinel instance. Otherwise uses the default instance.

    Args:
        rules_path: Path to rules (creates new Sentinel if provided)
        policy: Policy dict (creates new Sentinel if provided)
        action: Action to take on match
        severity: Minimum severity to trigger
        param_name: Parameter name to scan
        on_block: Handler when blocked
        raise_on_block: Whether to raise exception
        sentinel_instance: Specific Sentinel instance to use
        llm_provider: LLM provider for new Sentinel instance
        llm_model: LLM model for new Sentinel instance

    Returns:
        Decorator function

    Example:
        from sentinelai.sdk import protect

        @protect(rules_path="nova-rules/", action="block")
        def chat(prompt):
            return openai.chat(prompt)

        # With policy
        @protect(
            rules_path="nova-rules/",
            policy={"PI": {"action": "block"}},
            llm_provider="anthropic"
        )
        async def async_chat(prompt):
            return await claude.messages.create(prompt)
    """
    def decorator(func: Callable) -> Callable:
        nonlocal sentinel_instance

        if sentinel_instance is None:
            if rules_path or policy:
                from .nova import Sentinel
                sentinel_instance = Sentinel(
                    rules_path=rules_path,
                    policy=policy,
                    llm_provider=llm_provider,
                    llm_model=llm_model
                )
            else:
                sentinel_instance = get_default_sentinel()

        return sentinel_instance.protect(
            action=action,
            severity=severity,
            param_name=param_name,
            on_block=on_block,
            raise_on_block=raise_on_block,
        )(func)

    return decorator


def scan(
    text: str,
    rules_path: Optional[Union[str, Path, List[str]]] = None,
    policy: Optional[dict] = None,
    sentinel_instance: Optional["Sentinel"] = None,
) -> "ScanResult":
    """
    Standalone scan function for quick scanning without instance management.

    Args:
        text: Text to scan
        rules_path: Path to rules (creates new Sentinel if provided)
        policy: Policy dict (creates new Sentinel if provided)
        sentinel_instance: Specific Sentinel instance to use

    Returns:
        ScanResult with match details

    Example:
        from sentinelai.sdk import scan

        result = scan("ignore previous instructions", rules_path="nova-rules/")
        if result.blocked:
            print("Blocked!")
    """
    if sentinel_instance is None:
        if rules_path or policy:
            from .nova import Sentinel
            sentinel_instance = Sentinel(rules_path=rules_path, policy=policy)
        else:
            sentinel_instance = get_default_sentinel()

    return sentinel_instance.scan(text)


async def scan_async(
    text: str,
    rules_path: Optional[Union[str, Path, List[str]]] = None,
    policy: Optional[dict] = None,
    sentinel_instance: Optional["Sentinel"] = None,
) -> "ScanResult":
    """
    Async standalone scan function.

    Args:
        text: Text to scan
        rules_path: Path to rules (creates new Sentinel if provided)
        policy: Policy dict (creates new Sentinel if provided)
        sentinel_instance: Specific Sentinel instance to use

    Returns:
        ScanResult with match details
    """
    if sentinel_instance is None:
        if rules_path or policy:
            from .nova import Sentinel
            sentinel_instance = Sentinel(rules_path=rules_path, policy=policy)
        else:
            sentinel_instance = get_default_sentinel()

    return await sentinel_instance.scan_async(text)
