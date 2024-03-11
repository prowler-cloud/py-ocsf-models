from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class TypeID(IntEnum):
    Unknown: int = 0
    Other: int = 99
    Windows: int = 100
    Windows_Mobile: int = 101
    Linux: int = 200
    Android: int = 201
    MacOS: int = 300
    IOS: int = 301
    IPadOS: int = 302
    Solaris: int = 400
    AIX: int = 401
    HP_UX: int = 402


class OperatingSystem(BaseModel):
    """
    Represents the operating system, detailing its architecture, country, language, name, build, and specific editions or service packs.
    It encompasses both broad categorization and specific identifiers like CPE names.

    Attributes:
    - CPU Bits (cpu_bits) [Optional]: The cpu architecture, the number of bits used for addressing in memory. For example: 32 or 64.
    - Country (country) [Optional]: The operating system country code, as defined by the ISO 3166-1 standard (Alpha-2 code). For the complete list of country codes, see ISO 3166-1 alpha-2 codes.
    - Language (lang) [Optional]: The two letter lower case language codes, as defined by ISO 639-1. For example: en (English), de (German), or fr (French).
    - Name (name) [Optional]: The operating system name.
    - OS Build (build) [Optional]: The operating system build number.
    - OS Edition (edition) [Optional]: The operating system edition. For example: Professional.
    - OS Service Pack Name (sp_name) [Optional]: The name of the latest Service Pack.
    - OS Service Pack Version (sp_ver) [Optional]: The version number of the latest Service Pack.
    - The product CPE identifier (cpe_name) [Optional]: The Common Platform Enumeration (CPE) name as described by (NIST) For example: cpe:/a:apple:safari:16.2.
    - Type (type) [Optional]: The type of the operating system.
    - Type ID (type_id) [Optional]: The type identifier of the operating system.
    - Version (version) [Optional]: The version of the OS running on the device that originated the event. For example: "Windows 10", "OS X 10.7", or "iOS 9".
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
    type_id: TypeID
    version: Optional[str]
