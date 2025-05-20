from enum import IntEnum


class StatusID(IntEnum):
    """
    The normalized status identifier of the Finding, set by the consumer.

    0 Unknown: The status is unknown.
    1 New: The Finding is new and yet to be reviewed.
    2 InProgress: The Finding is under review.
    3 Suppressed: The Finding was reviewed, determined to be benign or a false positive and is now suppressed.
    4 Resolved: The Finding was reviewed, remediated and is now considered resolved.
    5 Archived: The Finding was archived.
    99 Other: The event status is not mapped. See the status attribute, which contains a data source specific value.
    """

    Unknown = 0
    New = 1
    InProgress = 2
    Suppressed = 3
    Resolved = 4
    Archived = 5
    Other = 99
