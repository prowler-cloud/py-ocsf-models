from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class ReputationScoreID(IntEnum):
    """
    Enum representing different reputation score identifiers.

    Attributes:
    - Unknown (0): The reputation score is unknown.
    - Very Safe (1): Long history of good behavior.
    - Safe (2): Consistently good behavior.
    - Probably Safe (3): Reasonable history of good behavior.
    - Leans Safe (4): Starting to establish a history of normal behavior.
    - May not be Safe (5): No established history of normal behavior.
    - Exercise Caution (6): Starting to establish a history of suspicious or risky behavior.
    - Suspicious/Risky (7): A site with a history of suspicious or risky behavior (spam, scam, potentially unwanted software, potentially malicious).
    - Possibly Malicious (8): Strong possibility of maliciousness.
    - Probably Malicious (9): Indicators of maliciousness.
    - Malicious (10): Proven evidence of maliciousness.
    - Other (99): The reputation score is not mapped. See the rep_score attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    Very_Safe: int = 1
    Safe: int = 2
    Probably_Safe: int = 3
    Leans_Safe: int = 4
    May_not_be_Safe: int = 5
    Exercise_Caution: int = 6
    Suspicious_or_Risky: int = 7
    Possibly_Malicious: int = 8
    Probably_Malicious: int = 9
    Malicious: int = 10
    Other: int = 99


class Reputation(BaseModel):
    """
    BaseModel class for representing reputation information.

    Attributes:
    - Provider (provider) [Recommended]: The provider of the reputation information.
    - Reputation Score (base_score) [Required]: The reputation score as reported by the event source.
    - Reputation Score (score) [Optional]: The reputation score, normalized to the caption of the score_id value. In the case of 'Other', it is defined by the event source.
    - Reputation Score ID (score_id) [Required]: The normalized reputation score identifier.
    """

    provider: str
    base_score: float
    score: Optional[str]
    score_id: ReputationScoreID


class TypeID(IntEnum):
    """
    Enum representing different types of observable value identifiers.

    Attributes:
    - Unknown (0): Unknown observable data type.
    - Hostname (1): Unique name assigned to a device connected to a computer network. A domain name in general is an Internet address that can be resolved through the Domain Name System (DNS).
    - IP_Address (2): Internet Protocol address (IP address), in either IPv4 or IPv6 format.
    - MAC_Address (3): Media Access Control (MAC) address.
    - User_Name (4): User name.
    - Email_Address (5): Email address.
    - URL_String (6): Uniform Resource Locator (URL) string.
    - File_Name (7): File name.
    - Hash (8): Hash. A unique value that corresponds to the content of the file, image, ja3_hash or hassh found in the schema.
    - Process_Name (9): Process name.
    - Resource_UID (10): Resource unique identifier. For example, S3 Bucket name or EC2 Instance ID.
    - Endpoint (20): The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network. Some examples of endpoints are mobile devices, desktop computers, virtual machines, embedded devices, and servers. Internet-of-Things devices—like cameras, lighting, refrigerators, security systems, smart speakers, and thermostats—are also endpoints.
    - User (21): The User object describes the characteristics of a user/person or a security principal. Defined by D3FEND d3f:UserAccount.
    - Email (22): The Email object describes the email metadata such as sender, recipients, and direction. Defined by D3FEND d3f:Email.
    - Uniform_Resource_Locator (23): The Uniform Resource Locator (URL) object describes the characteristics of a URL. Defined in RFC 1738 and by D3FEND d3f:URL.
    - File (24): The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details. Defined by D3FEND d3f:File.
    - Process (25): The Process object describes a running instance of a launched program. Defined by D3FEND d3f:Process.
    - Geo_Location (26): The Geo Location object describes a geographical location, usually associated with an IP address. Defined by D3FEND d3f:PhysicalLocation.
    - Container (27): The Container object describes an instance of a specific container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    - Registry_Key (28): The registry key object describes a Windows registry key. Defined by D3FEND d3f:WindowsRegistryKey.
    - Registry_Value (29): The registry value object describes a Windows registry value.
    - Fingerprint (30): The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content. It contains the algorithm and value of the fingerprint, enabling efficient and reliable identification of the associated data.
    - Other (99): The observable data type is not mapped. See the type attribute, which may contain data source specific value.
    """

    Unknown: int = 0
    Hostname: int = 1
    IP_Address: int = 2
    MAC_Address: int = 3
    User_Name: int = 4
    Email_Address: int = 5
    URL_String: int = 6
    File_Name: int = 7
    Hash: int = 8
    Process_Name: int = 9
    Resource_UID: int = 10
    Endpoint: int = 20
    User: int = 21
    Email: int = 22
    Uniform_Resource_Locator: int = 23
    File: int = 24
    Process: int = 25
    Geo_Location: int = 26
    Container: int = 27
    Registry_Key: int = 28
    Registry_Value: int = 29
    Fingerprint: int = 30
    Other: int = 99


class Observable(BaseModel):
    """
    The observable object is a pivot element that contains related information found in many places in the event.

    Attributes:
    - Name (name): The full name of the observable attribute. The name is a pointer/reference to an attribute within the event data. For example: file.name.
    - Reputation Scores (reputation) [Optional]: Contains the original and normalized reputation scores.
    - Type (type) [Optional]: The observable value type name.
    - Type ID (type_id): The observable value type identifier.
    - Value (value) [Optional]: The value associated with the observable attribute. The meaning of the value depends on the observable type. If the name refers to a scalar attribute, then the value is the value of the attribute. If the name refers to an object attribute, then the value is not populated.
    """

    name: str
    reputation: Optional[Reputation]
    type: Optional[str]
    type_id: TypeID
    value: Optional[str]
