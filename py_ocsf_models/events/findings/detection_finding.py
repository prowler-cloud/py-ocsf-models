from datetime import datetime
from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.events.findings.finding import Finding
from py_ocsf_models.objects.api import API
from py_ocsf_models.objects.cloud import Cloud
from py_ocsf_models.objects.container import Container
from py_ocsf_models.objects.evidence_artifacts import EvidenceArtifacts
from py_ocsf_models.objects.remediation import Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails


class CategoryUID(IntEnum):
    """
    The category unique identifier of the event.

    2 Findings: Findings events report findings, detections, and possible resolutions of malware, anomalies, or other actions performed by security products.
    """

    Findings: int = 2


class ClassUID(IntEnum):
    """
    The unique identifier of a class. A Class describes the attributes available in an event.

    2004 DetectionFinding: A Detection Finding describes detections or alerts generated by security products using correlation engines, detection engines or other methodologies. Note: if the product is a security control, the security_control profile should be applied and its attacks information should be duplicated into the finding_info object.
    """

    DetectionFinding: int = 2004


class ImpactID(IntEnum):
    """
    The normalized impact of the finding.

    0 Unknown: The normalized impact is unknown.
    1 Low
    2 Medium
    3 High
    4 Critical
    99 Other: The impact is not mapped. See the impact attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    Low: int = 1
    Medium: int = 2
    Hig: int = 3
    Critical: int = 4
    Other: int = 99


class RiskLevelID(IntEnum):
    """
    The normalized risk level id.

    0 Info
    1 Low
    2 Medium
    3 High
    4 Critical
    """

    Info: int = 0
    Low: int = 1
    Medium: int = 2
    High: int = 3
    Critical: int = 4


class TypeID(IntEnum):
    """
    The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.

    0 Info
    1 Low
    2 Medium
    3 High
    4 Critical
    """

    Unknown: int = 200400
    Create: int = 200401
    Update: int = 200402
    Close: int = 200403
    Other: int = 200404


class StatusID(IntEnum):
    """
    The normalized identifier of the event/finding severity.

    The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.

    0 Unknown: The status is unknown.
    1 New: The Finding is new and yet to be reviewed.
    2 InProgress: The Finding is under review.
    3 Suppressed: The Finding was reviewed, determined to be benign or a false positive and is now suppressed.
    4 Resolved: The Finding was reviewed, remediated and is now considered resolved.
    99 Other: The event status is not mapped. See the status attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    New: int = 1
    InProgress: int = 2
    Suppressed: int = 3
    Resolved: int = 4
    Other: int = 99


class DetectionFinding(Finding, BaseModel):
    """
    A Detection Finding describes detections or alerts generated by security products using correlation engines, detection engines or other methodologies. Note: if the product is a security control, the security_control profile should be applied and its attacks information should be duplicated into the finding_info object.

    Attributes:
    - Affected Resources (resources) [Recommended]: Describes details about resources that were the target of the activity that triggered the finding.
    - Category (category_name): The event category name, as defined by category_uid value: Findings.
    - Class (class_name) [Optional]: The event class name, as defined by class_uid value: Detection Finding.
    - Class ID (class_uid): The unique identifier of a class. A Class describes the attributes available in an event.
    - Cloud (cloud) [Optional]: Describes details about the Cloud environment where the event was originally created or logged.
    - Container (container) [Optional]: Describes the container details.
    - Count (count) [Optional]: Number of times similar events occurred within a specified timeframe.
    - Duration (duration) [Optional]: Time span of the event, from start to end, in milliseconds.
    - Event Time (time) [Required]: The standardized time when the event occurred or the finding was created.
    - Evidence Artifacts (evidences) [Optional]: Artifacts related to the security detection activities.
    - Impact (impact) [Optional]: The impact, normalized to the caption of the impact_id value. In the case of 'Other', it is defined by the event source.
    - Impact Score (impact_score) [Optional]: The impact of the finding, valid range 0-100.
    - Impact ID (impact_id) [Optional]: The normalized impact of the finding.
    - Remediation Guidance (remediation) [Optional]: Suggested steps to address the finding.
    - Risk Level (risk_level) [Optional]: The risk level, normalized to the caption of the risk_level_id value. In the case of 'Other', it is defined by the event source.
    - Risk Level ID (risk_level_id) [Optional]: The normalized risk level id.
    - Risk Score (risk_score) [Optional]: The risk score as reported by the event source.
    - Timezone Offset (timezone_offset) [Optional]: Difference in minutes from UTC.
    - Type ID (type_uid): The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: class_uid * 100 + activity_id.
    - Type Name (type_name) [Optional]: The event/finding type name, as defined by the type_uid.
    - Vulnerabilities (vulnerabilities) [Optional]: Vulnerabilities identified in the finding.

    If the Cloud profile is needed:
        - API Details (api) [Optional]: Describes details about a typical API (Application Programming Interface) call.
        - Cloud (cloud): Describes details about the Cloud environment where the event was originally created or logged.

    If the Container profile is needed:
        - Container (container) [Recommended]: The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
        - Namespace PID (namespace_pid) [Recommended]: If running under a process namespace (such as in a container), the process identifier within that process namespace.
    """

    resources: Optional[list[ResourceDetails]]
    category_name: str = CategoryUID.Findings.name
    category_uid: int = CategoryUID.Findings.value
    class_name: Optional[str] = ClassUID.DetectionFinding.name
    class_uid: int = ClassUID.DetectionFinding.value
    cloud: Optional[Cloud]
    api: Optional[API]
    container: Optional[Container]
    namespace_pid: Optional[int]
    count: Optional[int]
    duration: Optional[int]
    event_time: datetime
    evidences: Optional[list[EvidenceArtifacts]]
    impact: Optional[str]
    impact_score: Optional[int]
    impact_id: Optional[ImpactID]
    remediation: Optional[Remediation]
    risk_level: Optional[str]
    risk_level_id: Optional[RiskLevelID]
    risk_score: Optional[int]
    status_id: Optional[StatusID]  # type: ignore
    timezone_offset: Optional[int]
    type_id: TypeID
    type_name: Optional[str]
    vulnerabilities: Optional[list[VulnerabilityDetails]]
