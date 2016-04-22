from enum import Enum


class DebugTraceLevel(Enum):
    """Different trace level of debugging message"""
    NONE = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4


class Const:
    PIN_MIN = 1
    PIN_MAX = 40

    TWO_WHEELED = 1
    FOUR_WHEELED = 2

    REAR_LEFT = 1
    REAR_RIGHT = 2
    FRONT_LEFT = 3
    FRONT_RIGHT = 4
