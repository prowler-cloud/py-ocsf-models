from enum import IntEnum


class DetectionFindingTypeID(IntEnum):
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.

    0 Info
    1 Low
    2 Medium
    3 High
    4 Critical
    """

    Unknown = 200400
    Create = 200401
    Update = 200402
    Close = 200403
    Other = 200499
