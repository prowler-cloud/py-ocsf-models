from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class TicketStatusID(IntEnum):
    """
    The normalized status of the ticket.

    0 Unknown: The status is unknown.
    1 New: The ticket is new.
    2 In Progress: The ticket is being worked on.
    3 On Hold: The ticket is on hold.
    4 Resolved: The ticket is resolved.
    5 Closed: The ticket is closed.
    99 Other: The status is not mapped. See the status attribute.
    """

    Unknown = 0
    New = 1
    InProgress = 2
    OnHold = 3
    Resolved = 4
    Closed = 5
    Other = 99


class TicketTypeID(IntEnum):
    """
    The type of ticket.

    0 Unknown: The type is unknown.
    1 Internal: An internal ticket.
    2 External: An external ticket.
    99 Other: The type is not mapped. See the type attribute.
    """

    Unknown = 0
    Internal = 1
    External = 2
    Other = 99


class Ticket(BaseModel):
    """
    The Ticket object describes a ticket from an IT Service Management (ITSM) system
    such as ServiceNow, Jira, etc.

    Constraint: At least one of src_url, uid must be present.

    Attributes:
    - Source URL (src_url) [Recommended]: The URL to the ticket in the ITSM system.
    - Status (status) [Optional]: The ticket status.
    - Status Details (status_details) [Optional]: Additional status details.
    - Status ID (status_id) [Optional]: The normalized status identifier.
    - Title (title) [Optional]: The ticket title.
    - Type (type) [Optional]: The ticket type.
    - Type ID (type_id) [Optional]: The normalized type identifier.
    - UID (uid) [Recommended]: The unique identifier of the ticket.
    """

    src_url: Optional[str] = None
    status: Optional[str] = None
    status_details: Optional[list[str]] = None
    status_id: Optional[TicketStatusID] = None
    title: Optional[str] = None
    type: Optional[str] = None
    type_id: Optional[TicketTypeID] = None
    uid: Optional[str] = None
