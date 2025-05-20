from enum import IntEnum


class VerdictID(IntEnum):
    """
    The normalized verdict (or status) ID of the evidence associated with the security detection. For example, Microsoft Graph Security Alerts contain a verdict enumeration for each type of evidence associated with the Alert. This is typically set by an automated investigation process or an analyst/investigator assigned to the finding.
        0	Unknown: The type is unknown.
        1	False Positive: The verdict for the evidence has been identified as a False Positive.
        2	True Positive: The verdict for the evidence has been identified as a True Positive.
        3	Disregard: The verdict for the evidence is that is should be Disregarded.
        4	Suspicious: The verdict for the evidence is that the behavior has been identified as Suspicious.
        5	Benign: The verdict for the evidence is that the behavior has been identified as Benign.
        6	Test: The evidence is part of a Test, or other sanctioned behavior(s).
        7	Insufficient Data: There is insufficient data to render a verdict on the evidence.
        8	Security Risk: The verdict for the evidence is that the behavior has been identified as a Security Risk.
        9	Managed Externally: The verdict for the evidence is Managed Externally, such as in a case management tool.
        10	Duplicate: This evidence duplicates existing evidence related to this finding.
        99	Other: The type is not mapped. See the type attribute, which contains a data source specific value.
    """

    Unknown = 0
    FalsePositive = 1
    TruePositive = 2
    Disregard = 3
    Suspicious = 4
    Benign = 5
    Test = 6
    InsufficientData = 7
    SecurityRisk = 8
    ManagedExternally = 9
    Duplicate = 10
    Other = 99
