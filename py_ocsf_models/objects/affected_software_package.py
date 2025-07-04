from enum import IntEnum
from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.fingerprint import FingerPrint
from py_ocsf_models.objects.remediation import Remediation


class SoftwarePackageTypeID(IntEnum):
    Unknown = 0
    Application = 1
    Operating_System = 2
    Other = 99


class AffectedSoftwarePackage(BaseModel):
    """
    The Affected Package object describes details about a software package identified as affected by a vulnerability/vulnerabilities.

    Attributes:
    - Architecture (architecture) [Recommended]: Architecture is a shorthand name describing the type of computer hardware the packaged software is meant to run on.
    - The product CPE identifier (cpe_name) [Optional]: The Common Platform Enumeration (CPE) name as described by (NIST) For example: cpe:/a:apple:safari:16.2.
    - Epoch (epoch) [Optional]: Integer The software package epoch. Epoch is a way to define weighted dependencies based on version numbers.
    - Fixed In Version (fixed_in_version) [Optional]: The software package version in which a reported vulnerability was patched/fixed.
    - Hash (hash) [Optional]: Fingerprint Cryptographic hash to identify the binary instance of a software component. This can include any component such file, package, or library.
    - Software License (license) [Optional]: The software license applied to this package.
    - Software License URL (license_url) [Optional]: The URL pointing to the license applied on package or software. This is typically a LICENSE.md file within a repository.
    - Name (name) [Required]: The software package name.
    - Package Manager (package_manager) [Optional]: The software packager manager utilized to manage a package on a system, e.g. npm, yum, dpkg etc.
    - Package Manager URL (package_manager_url) [Optional]: The URL of the package or library at the package manager, or the specific URL or URI of an internal package manager link such as AWS CodeArtifact or Artifactory.
    - Path (path) [Optional]: The installation path of the affected package.
    - Package URL (purl) [Optional]: A purl is a URL string used to identify and locate a software package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.
    - Software Release Details (release) [Optional]: Release is the number of times a version of the software has been packaged.
    - Remediation Guidance (remediation) [Optional]: Remediation Describes the recommended remediation steps to address identified issue(s).
    - Source URL (src_url) [Optional]: The link to the specific library or package such as within GitHub, this is different from the link to the package manager where the library or package is hosted.
    - Type (type) [Optional]: The type of software package, normalized to the caption of the type_id value. In the case of 'Other', it is defined by the source. This is the string sibling of enum attribute type_id.
    - Type ID (type_id) [Recommended]: Integer The type of software package.
    - Package UID (uid) [Optional]: A unique identifier for the package or library reported by the source tool. E.g., the libId within the sbom field of an OX Security Issue or the SPDX components.*.bom-ref.
    - Vendor Name (vendor_name) [Optional]: The name of the vendor who published the software package.
    - Version (version) [Required]: The software package version.

    """

    architecture: Optional[str]
    cpe_name: Optional[str]
    epoch: Optional[int]
    fixed_in_version: Optional[str]
    hash: Optional[FingerPrint]
    license: Optional[str]
    license_url: Optional[str]
    name: Optional[str]
    package_manager: Optional[str]
    package_manager_url: Optional[str]
    path: Optional[str]
    purl: Optional[str]
    release: Optional[str]
    remediation: Optional[Remediation]
    src_url: Optional[str]
    type: Optional[str]
    type_id: Optional[SoftwarePackageTypeID]
    uid: Optional[str]
    vendor_name: Optional[str]
    version: str
