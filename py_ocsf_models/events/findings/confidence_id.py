from enum import IntEnum


class ConfidenceID(IntEnum):
    """
    The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

    0 Unknown: The normalized confidence is unknown.
    1 Low
    2 Medium
    3 High
    99 Other: The confidence is not mapped to the defined enum values. See the confidence attribute, which contains a data source specific value.

    """

    Unknown = 0
    Low = 1
    Medium = 2
    High = 3
    Other = 99
