from enum import Enum


class DebugTraceLevel(Enum):
    """Different trace level of debugging message"""
    NONE = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4
