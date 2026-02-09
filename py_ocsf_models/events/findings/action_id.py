from enum import IntEnum


class ActionID(IntEnum):
    """
    The action taken by a control or other policy-based system leading to an outcome or disposition.

    0 Unknown: The action is unknown.
    1 Allowed: The action was allowed.
    2 Denied: The action was denied.
    3 Observed: The action was observed but no action was taken.
    4 Modified: The action was modified.
    99 Other: The action is not mapped. See the action attribute, which contains a data source specific value.
    """

    Unknown = 0
    Allowed = 1
    Denied = 2
    Observed = 3
    Modified = 4
    Other = 99
