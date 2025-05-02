from enum import IntEnum


class RiskLevelID(IntEnum):
    """
    The normalized risk level id.

    0 Info
    1 Low
    2 Medium
    3 High
    4 Critical
    """

    Info = 0
    Low = 1
    Medium = 2
    High = 3
    Critical = 4
