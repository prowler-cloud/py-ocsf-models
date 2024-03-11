from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class NetworkType(IntEnum):
    """
    Enum representing different types of network interfaces.

    Attributes:
    - Unknown (0): The type is unknown.
    - Wired (1): A wired network interface.
    - Wireless (2): A wireless network interface.
    - Mobile (3): A mobile network interface.
    - Tunnel (4): A tunnel network interface.
    - Other (99): The type is not mapped. See the type attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    Wired: int = 1
    Wireless: int = 2
    Mobile: int = 3
    Tunnel: int = 4
    Other: int = 99


class NetworkInterface(BaseModel):
    """
    The Network Interface object describes the type and associated attributes of a network interface.

    Attributes:
    - Hostname (hostname) [Recommended]: The hostname associated with the network interface.
    - IP Address (ip) [Recommended]: The IP address associated with the network interface.
    - MAC Address (mac) [Recommended]: The MAC address of the network interface.
    - Name (name) [Recommended]: The name of the network interface.
    - Namespace (namespace) [Optional]: The namespace useful in merger or acquisition situations.
    - Subnet Prefix Length (subnet_prefix) [Optional]: The subnet prefix length determines the number of bits used to represent the network part of the IP address.
    - Type (type) [Optional]: The type of network interface.
    - Type ID (type_id) [Required]: The network interface type identifier.
    - Unique ID (uid) [Optional]: The unique identifier for the network interface.
    """

    hostname: str
    ip: str
    mac: str
    name: str
    namespace: Optional[str]
    subnet_prefix: Optional[int]
    type: Optional[str]
    type_id: NetworkType
    uid: Optional[str]
