from enum import IntEnum


class PriorityID(IntEnum):
    """
    The normalized priority identifies the relative importance of the incident or finding.

    0 Unknown: The priority is unknown.
    1 Low: Low priority.
    2 Medium: Medium priority.
    3 High: High priority.
    4 Critical: Critical priority.
    99 Other: The priority is not mapped. See the priority attribute, which contains a data source specific value.
    """

    Unknown = 0
    Low = 1
    Medium = 2
    High = 3
    Critical = 4
    Other = 99
