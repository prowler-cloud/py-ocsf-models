from enum import IntEnum


class ApplicationSecurityPostureFindingTypeID(IntEnum):
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.

    0 Info
    1 Low
    2 Medium
    3 High
    4 Critical
    """

    Unknown = 200700
    Create = 200701
    Update = 200702
    Close = 200703
    Other = 200799
