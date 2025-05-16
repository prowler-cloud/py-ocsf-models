from enum import IntEnum


class SeverityID(IntEnum):
    """
    The normalized identifier of the event/finding severity.

    The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.

    0 Unknown: The event/finding severity is unknown.
    1 Informational: Informational message. No action required.
    2 Low: The user decides if action is needed.
    3 Medium: Action is required but the situation is not serious at this time.
    4 High: Action is required immediately.
    5 Critical: Action is required immediately and the scope is broad.
    6 Fatal: An error occurred but it is too late to take remedial action.
    99 Other: The event/finding severity is not mapped. See the severity attribute, which contains a data source specific value.
    """

    Unknown = 0
    Informational = 1
    Low = 2
    Medium = 3
    High = 4
    Critical = 5
    Fatal = 6
    Other = 99
