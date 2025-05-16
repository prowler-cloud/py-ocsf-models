from typing import List, Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.assessment import Assessment
from py_ocsf_models.objects.check import Check
from py_ocsf_models.objects.compliance_status import StatusID


class Compliance(BaseModel):
    """
    The Compliance object contains information about Industry and Regulatory Framework standards, controls and requirements or details about custom assessments utilized in a compliance evaluation. Standards define broad security frameworks, controls represent specific security requirements within those frameworks, and checks are the testable verification points used to determine if controls are properly implemented.

    Attributes:
    - Assessments (assessments) [Optional]: A list of assessments associated with the compliance requirements evaluation.
    - Category (category) [Optional]: The category a control framework pertains to, as reported by the source tool, such as Asset Management or Risk Assessment.
    - Checks (checks) [Optional]: A list of compliance checks associated with specific industry standards or frameworks. Each check represents an individual rule or requirement that has been evaluated against a target device. Checks typically include details such as the check name (e.g., CIS: 'Ensure mounting of cramfs filesystems is disabled' or DISA STIG descriptive titles), unique identifiers (such as CIS identifier '1.1.1.1' or DISA STIG identifier 'V-230234'), descriptions (detailed explanations of security requirements or vulnerability discussions), and version information.
    - Control (control) [Optional]: A Control is a prescriptive, actionable set of specifications that strengthens device posture. The control specifies required security measures, while the specific implementation values are defined in control_parameters. E.g., CIS AWS Foundations Benchmark 1.2.0 - Control 2.1 - Ensure CloudTrail is enabled in all regions
    - Description (desc) [Optional]: The description or criteria of a control.
    - Requirements (requirements) [Optional]: The specific compliance requirements being evaluated. E.g., PCI DSS Requirement 8.2.3 - Passwords must meet minimum complexity requirements or HIPAA Security Rule 164.312(a)(2)(iv) - Implement encryption and decryption mechanisms
    - Standards (standards) [Optional]: The regulatory or industry standards being evaluated for compliance.
    """

    assessments: Optional[List[Assessment]]
    category: Optional[str]
    checks: Optional[List[Check]]
    control: Optional[str]
    desc: Optional[str]
    requirements: Optional[List[str]]
    standards: Optional[List[str]]
    status_id: Optional[StatusID]
