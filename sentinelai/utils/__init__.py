"""
NOVA: The Prompt Pattern Matching
Author: Thomas Roccia
twitter: @fr0gger_
License: MIT License
Version: see sentinelai._version
Description: Utility functions for SentinelAI framework
"""

from sentinelai.utils.config import SentinelConfig, get_config
from sentinelai.utils.logger import LOG_FORMATS, get_logger, set_log_format, set_log_level
from sentinelai.utils.helpers import normalize_unicode, remove_zero_width_chars
from sentinelai.utils.log_buffer import (
    LogRingBuffer,
    clear_log_buffer,
    get_log_buffer,
    install_buffer_handler,
    uninstall_buffer_handler,
)

__all__ = [
    'SentinelConfig',
    'get_config',
    'LOG_FORMATS',
    'get_logger',
    'set_log_format',
    'set_log_level',
    'normalize_unicode',
    'remove_zero_width_chars',
    'LogRingBuffer',
    'clear_log_buffer',
    'get_log_buffer',
    'install_buffer_handler',
    'uninstall_buffer_handler',
]
