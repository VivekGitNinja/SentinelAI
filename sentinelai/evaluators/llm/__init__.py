"""
NOVA: The Prompt Pattern Matching
Author: Thomas Roccia
twitter: @fr0gger_
License: MIT License
Version: see sentinelai._version
Description: LLM-based evaluator implementations

This package preserves the historical public import path
``sentinelai.evaluators.llm``. Provider implementations live in internal
modules (``_openai``, ``_anthropic``, ``_groq``, ``_ollama``) with shared
caching/session infrastructure in ``_shared`` and the evaluator factory
in ``_factory``. Import everything from ``sentinelai.evaluators.llm`` directly;
the underscore-prefixed modules are implementation details.
"""

from sentinelai.evaluators.llm._shared import (
    PROVIDER_MODEL_ENV,
    PROVIDER_MODEL_ENV_ALIASES,
    TTLLRUCache,
    logger,
)
from sentinelai.evaluators.llm._shared import _get_env_model as _get_env_model
from sentinelai.evaluators.llm._shared import _select_model as _select_model
from sentinelai.evaluators.llm._shared import _LLM_RESPONSE_CACHE as _LLM_RESPONSE_CACHE
from sentinelai.evaluators.llm._shared import _LLM_CACHE_LOCK as _LLM_CACHE_LOCK
from sentinelai.evaluators.llm._shared import _SESSION_LOCK as _SESSION_LOCK
from sentinelai.evaluators.llm._shared import _normalize_cache_temperature as _normalize_cache_temperature
from sentinelai.evaluators.llm._shared import _get_llm_cache_key as _get_llm_cache_key
from sentinelai.evaluators.llm._shared import _get_cached_response as _get_cached_response
from sentinelai.evaluators.llm._shared import _cache_response as _cache_response
from sentinelai.evaluators.llm._shared import _get_shared_session as _get_shared_session
from sentinelai.evaluators.llm._openai import (
    OpenAIEvaluator,
    OpenRouterEvaluator,
    AzureOpenAIEvaluator,
)
from sentinelai.evaluators.llm._anthropic import AnthropicEvaluator
from sentinelai.evaluators.llm._groq import GroqEvaluator
from sentinelai.evaluators.llm._ollama import OllamaEvaluator
from sentinelai.evaluators.llm._factory import get_validated_evaluator
from sentinelai.evaluators.base import LLMEvaluator

__all__ = [
    'PROVIDER_MODEL_ENV',
    'PROVIDER_MODEL_ENV_ALIASES',
    'TTLLRUCache',
    'logger',
    'LLMEvaluator',
    'OpenAIEvaluator',
    'OpenRouterEvaluator',
    'AzureOpenAIEvaluator',
    'AnthropicEvaluator',
    'GroqEvaluator',
    'OllamaEvaluator',
    'get_validated_evaluator',
]
