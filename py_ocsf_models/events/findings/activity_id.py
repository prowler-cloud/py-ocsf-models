from enum import IntEnum


class ActivityID(IntEnum):
    """
    The normalized identifier of the finding activity.

    0 Unknown: The event activity is unknown.
    1 Create: A finding was created.
    2 Update: A finding was updated.
    3 Close: A finding was closed.
    99 Other: The event activity is not mapped. See the activity_name attribute, which contains a data source specific value.
    """

    Unknown = 0
    Create = 1
    Update = 2
    Close = 3
    Other = 99
