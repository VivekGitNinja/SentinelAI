"""
SentinelAI: The Prompt Pattern Matching
Author: Vivek Kumar Verma 
twitter: @VivekGitNinja
License: MIT License
Version: see sentinelai._version
Description: Main SentinelAI framework package initialization
"""

from sentinelai._version import __version__

# NOTE: Transformers configuration for clean_up_tokenization_spaces is done lazily
# in sentinelai.evaluators/semantics.py when the semantic model is first loaded.
# This avoids loading torch/transformers (~1 second) for keyword-only matching.

from sentinelai.core.rules import (
    KeywordPattern,
    SemanticPattern,
    LLMPattern,
    SentinelRule
)
from sentinelai.core.matcher import SentinelMatcher
from sentinelai.core.parser import SentinelParser
from sentinelai.core.scanner import SentinelScanner
from sentinelai.utils.config import SentinelConfig
from sentinelai.utils.logger import LOG_FORMATS, get_logger, set_log_format, set_log_level
from sentinelai.utils.log_buffer import get_log_buffer, install_buffer_handler

# SDK imports
from sentinelai.sdk import (
    Sentinel,
    ScanResult,
    RuleMatch,
    SentinelPolicy,
    PolicyRule,
    Action,
    Redactor,
    SentinelBlockedError,
    protect,
    scan,
)

__all__ = [
    '__version__',

    # Core classes
    'KeywordPattern',
    'SemanticPattern',
    'LLMPattern',
    'SentinelRule',
    'SentinelMatcher',
    'SentinelParser',
    'SentinelScanner',
    'SentinelConfig',
    'LOG_FORMATS',
    'get_logger',
    'set_log_format',
    'set_log_level',
    'get_log_buffer',
    'install_buffer_handler',

    # SDK classes
    'Sentinel',
    'ScanResult',
    'RuleMatch',
    'SentinelPolicy',
    'PolicyRule',
    'Action',
    'Redactor',
    'SentinelBlockedError',
    'protect',
    'scan',
]
