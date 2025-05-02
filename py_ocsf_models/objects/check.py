from typing import List, Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.objects.compliance_status import StatusID


class Check(BaseModel):
    """
    The check object defines a specific, testable compliance verification point that evaluates a target device against a standard, framework, or custom requirement. While checks are typically associated with formal standards (like CIS, NIST, or ISO), they can also represent custom or organizational requirements. When mapped to controls, checks can evaluate specific control_parameters to determine compliance status, but neither the control mapping nor control_parameters are required for a valid check.

    Attributes:
    - Description (desc) [Optional]: The detailed description of the compliance check, explaining the security requirement, vulnerability, or configuration being assessed. For example, CIS: The cramfs filesystem type is a compressed read-only Linux filesystem. Removing support for unneeded filesystem types reduces the local attack surface. or DISA STIG: Unauthorized access to the information system by foreign entities may result in loss or compromise of data.
    - Name (name) [Optional]: The name or title of the compliance check. For example, CIS: Ensure mounting of cramfs filesystems is disabled or DISA STIG: The Ubuntu operating system must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

    - Severity (severity) [Optional]: The severity level as defined in the source document. For example CIS Benchmarks, valid values are: Level 1 (security-forward, essential settings), Level 2 (security-focused environment, more restrictive), or Scored/Not Scored (whether compliance can be automatically checked). For DISA STIG, valid values are: CAT I (maps to severity_id 5/Critical), CAT II (maps to severity_id 4/High), or CAT III (maps to severity_id 3/Medium).
    - Severity ID (severity_id) [Optional]: The normalized severity identifier that maps severity levels to standard severity levels. For example CIS Benchmark: Level 2 maps to 4 (High), Level 1 maps to 3 (Medium). For DISA STIG: CAT I maps to 5 (Critical), CAT II maps to 4 (High), and CAT III maps to 3 (Medium).
    - Standards (standards) [Optional]: The regulatory or industry standard this check is associated with. E.g., PCI DSS 3.2.1, HIPAA Security Rule, NIST SP 800-53 Rev. 5, or ISO/IEC 27001:2013.
    - Status (status) [Optional]: The resultant status of the compliance check normalized to the caption of the status_id value. For example, CIS Benchmark: Pass when all requirements are met, Fail when requirements are not met, or DISA STIG: NotAFinding (maps to status_id 1/Pass), Open (maps to status_id 3/Fail).
    - Status ID (status_id) [Optional]: The normalized status identifier of the compliance check.
    - UID (uid) [Optional]: The unique identifier of the compliance check within its standard or framework. For example, CIS Benchmark identifier 1.1.1.1, DISA STIG identifier V-230234, or NIST control identifier AC-17(2).
    - Version (version) [Optional]: The check version. For example, CIS Benchmark: 1.1.0 for Amazon Linux 2 or DISA STIG: V2R1 for Windows 10.
    """

    desc: Optional[str]
    name: Optional[str]
    severity: Optional[str]
    severity_id: Optional[SeverityID]
    standards: Optional[List[str]]
    status: Optional[str]
    status_id: Optional[StatusID]
    uid: Optional[str]
    version: Optional[str]
