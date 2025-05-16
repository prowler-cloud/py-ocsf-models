from enum import IntEnum


class ImpactID(IntEnum):
    """
    The normalized impact of the finding.

    0 Unknown: The normalized impact is unknown.
    1 Low
    2 Medium
    3 High
    4 Critical
    99 Other: The impact is not mapped. See the impact attribute, which contains a data source specific value.
    """

    Unknown = 0
    Low = 1
    Medium = 2
    Hig = 3
    Critical = 4
    Other = 99
