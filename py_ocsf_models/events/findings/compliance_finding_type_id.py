from enum import IntEnum


class ComplianceFindingTypeID(IntEnum):
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.

    """

    Unknown = 200300
    Create = 200301
    Update = 200302
    Close = 200303
    Other = 200399
