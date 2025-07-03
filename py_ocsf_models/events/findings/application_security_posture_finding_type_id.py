from enum import IntEnum


class ApplicationSecurityPostureFindingTypeID(IntEnum):
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.

    """

    Unknown = 200700
    Create = 200701
    Update = 200702
    Close = 200703
    Other = 200799
