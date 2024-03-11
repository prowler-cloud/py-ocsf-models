from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class DNSOpcodeID(IntEnum):
    """
    Enum representing different DNS opcode identifiers.

    Attributes:
    - Query (0): Standard query.
    - Inverse Query (1): Inverse query, obsolete.
    - Status (2): Server status request.
    - Reserved (3): Reserved, not used.
    - Notify (4): Zone change notification.
    - Update (5): Dynamic DNS update.
    - DSO Message (6): DNS Stateful Operations (DSO).
    """

    Query: int = 0
    Inverse_Query: int = 1
    Status: int = 2
    Reserved: int = 3
    Notify: int = 4
    Update: int = 5
    DSO_Message: int = 6


class DNSQuery(BaseModel):
    """
    The DNS query object represents a specific request made to the Domain Name System (DNS) to retrieve information about a domain or perform a DNS operation.
    This object encapsulates the necessary attributes and methods to construct and send DNS queries, specify the query type (e.g., A, AAAA, MX).

    Attributes:
    - DNS Opcode (opcode) [Optional]: The DNS opcode specifies the type of the query message.
    - DNS Opcode ID (opcode_id) [Recommended]: The DNS opcode ID specifies the normalized query message type.
    - Hostname (hostname) [Required]: The hostname or domain being queried. For example: www.example.com.
    - Packet UID (packet_uid) [Recommended]: The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response.
    - Resource Record Class (class) [Recommended]: The class of resource records being queried. See RFC1035. For example: IN.
    - Resource Record Type (type) [Recommended]: The type of resource records being queried. See RFC1035. For example: A, AAAA, CNAME, MX, and NS.
    """

    opcode: Optional[str]
    opcode_id: Optional[DNSOpcodeID]
    hostname: str
    packet_uid: Optional[int]
    # TODO: Update to Pydantic v2 to use Field
    # class_: Optional[str] = Field(
    #     alias="class"
    # )  # Renaming class to avoid conflict with Python keyword
    type: Optional[str]
