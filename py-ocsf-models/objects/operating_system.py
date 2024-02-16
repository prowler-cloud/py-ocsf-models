from typing import Optional

from pydantic import BaseModel


class OperatingSystemType(int, Enum):
    Unknown = 0
    Other = 99
    Windows = 100
    Windows_Mobile = 101
    Linux = 200
    Android = 201
    MacOS = 300
    IOS = 301
    IPadOS = 302
    Solaris = 400
    AIX = 401
    HP_UX = 402


class OperatingSystem(BaseModel):
    """
    Represents the operating system, detailing its architecture, country, language, name, build, and specific editions or service packs.
    It encompasses both broad categorization and specific identifiers like CPE names.

    Attributes:
    - cpu_bits: Architecture in bits.
    - country: ISO 3166-1 alpha-2 country code.
    - lang: ISO 639-1 two-letter language code.
    - name: OS name.
    - build: OS build number.
    - edition: OS edition.
    - sp_name: Service Pack name.
    - sp_ver: Service Pack version.
    - cpe_name: Common Platform Enumeration name.
    - type: OS type.
    - type_id: OS type identifier.
    - version: OS version.
    """

    cpu_bits: Optional[int]
    country: Optional[str]
    lang: Optional[str]
    name: str
    build: Optional[str]
    edition: Optional[str]
    sp_name: Optional[str]
    sp_ver: Optional[int]
    cpe_name: Optional[str]
    type: Optional[str]
    type_id: OperatingSystemType
    version: Optional[str]
