from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel

from py_ocsf_models.events.base_event import BaseEvent
from py_ocsf_models.objects.mitre_attack import MITREAttack
from py_ocsf_models.objects.related_event import RelatedEvent


class PhaseID(IntEnum):
    """
    The Kill Chain Phase object represents a single phase of a cyber attack, including the initial reconnaissance and planning stages up to the final objective of the attacker. It provides a detailed description of each phase and its associated activities within the broader context of a cyber attack.

    Attributes:
    - Unknown (0): The kill chain phase is unknown.
    - Reconnaissance (1): The attackers pick a target and perform a detailed analysis, start collecting information (email addresses, conferences information, etc.) and evaluate the victim’s vulnerabilities to determine how to exploit them.
    - Weaponization (2): The attackers develop a malware weapon and aim to exploit the discovered vulnerabilities.
    - Delivery (3): The intruders will use various tactics, such as phishing, infected USB drives, etc.
    - Exploitation (4): The intruders start leveraging vulnerabilities to executed code on the victim’s system.
    - Installation (5): The intruders install malware on the victim’s system.
    - Command & Control (6): Malware opens a command channel to enable the intruders to remotely manipulate the victim's system.
    - Actions on Objectives (7): With hands-on keyboard access, intruders accomplish the mission’s goal.
    - Other (99): The kill chain phase is not mapped. See the phase attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    Reconnaissance: int = 1
    Weaponization: int = 2
    Delivery: int = 3
    Exploitation: int = 4
    Installation: int = 5
    Command_Control: int = 6
    Actions_on_Objectives: int = 7
    Other: int = 99


class KillChainPhase(BaseModel):
    """
    Base model representing a Cyber Kill Chain phase.

    Attributes:
    - Kill Chain Phase (phase) [Recommended]: The cyber kill chain phase.
    - Kill Chain Phase ID (phase_id) [Required]: The cyber kill chain phase identifier.
    """

    phase: str
    phase_id: PhaseID


class Analytic(BaseModel):
    """
    The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.

    Attributes:
    - Category (category) [Optional]: The analytic category.
    - Description (desc) [Optional]: The description of the analytic that generated the finding.
    - Name (name) [Recommended]: The name of the analytic that generated the finding.
    - Type (type) [Optional]: The analytic type.
    - Type ID (type_id) [Required]: The analytic type ID.
    - Unique ID (uid) [Recommended]: The unique identifier of the analytic that generated the finding.
    - Version (version) [Optional]: The analytic version. For example: 1.1.
    """

    category: Optional[str]
    desc: Optional[str]
    name: str
    type: Optional[str]
    type_id: int
    uid: str
    version: Optional[str]


class FindingInformation(BaseModel):
    """
    Base model representing information about a finding or conclusion.

    Attributes:
    - Analytic (analytic) [Recommended]: The analytic technique used to analyze and derive insights from the data or information that led to the finding or conclusion.
    - Created Time (created_time) [Optional]: The time when the finding was created.
    - Created Time DT (created_time_dt) [Optional]: The time when the finding was created in datetime format.
    - Data Sources (data_sources) [Optional]: A list of data sources utilized in generation of the finding.
    - Description (desc) [Optional]: The description of the reported finding.
    - First Seen (first_seen_time) [Optional]: The time when the finding was first observed.
    - First Seen DT (first_seen_time_dt) [Optional]: The time when the finding was first observed in datetime format.
    - Kill Chain (kill_chain) [Optional]: The Cyber Kill Chain® provides a detailed description of each phase and its associated activities within the broader context of a cyber attack.
    - Last Seen (last_seen_time) [Optional]: The time when the finding was last observed.
    - Last Seen DT (last_seen_time_dt) [Optional]: The time when the finding was last observed in datetime format.
    - MITRE ATT&CK® Details (attacks) [Optional]: The MITRE ATT&CK® technique and associated tactics related to the finding.
    - Modified Time (modified_time) [Optional]: The time when the finding was last modified.
    - Modified Time DT (modified_time_dt) [Optional]: The time when the finding was last modified in datetime format.
    - Product Identifier (product_uid) [Optional]: The unique identifier of the product that reported the finding.
    - Related Analytics (related_analytics) [Optional]: Other analytics related to this finding.
    - Related Events (related_events) [Optional]: Describes events and/or other findings related to the finding as identified by the security product.
    - Source URL (src_url) [Optional]: The URL pointing to the source of the finding.
    - Title (title) [Required]: A title or a brief phrase summarizing the reported finding.
    - Types (types) [Optional]: One or more types of the reported finding.
    - Unique ID (uid) [Required]: The unique identifier of the reported finding.
    """

    analytic: Optional[Analytic]
    created_time: Optional[int]
    created_time_dt: Optional[datetime]
    data_sources: Optional[List[str]]
    desc: Optional[str]
    first_seen_time: Optional[int]
    first_seen_time_dt: Optional[datetime]
    kill_chain: Optional[List[KillChainPhase]]
    last_seen_time: Optional[int]
    last_seen_time_dt: Optional[datetime]
    attacks: Optional[List[MITREAttack]]
    modified_time: Optional[int]
    modified_time_dt: Optional[datetime]
    product_uid: Optional[str]
    related_analytics: Optional[List[Analytic]]
    related_events: Optional[List[RelatedEvent]]
    src_url: Optional[str]
    title: str
    types: Optional[List[str]]
    uid: str


class ActivityID(IntEnum):
    """
    The normalized identifier of the finding activity.

    0 Unknown: The event activity is unknown.
    1 Create: A finding was created.
    2 Update: A finding was updated.
    3 Close: A finding was closed.
    99 Other: The event activity is not mapped. See the activity_name attribute, which contains a data source specific value.
    """

    Unknown: int = 0
    Create: int = 1
    Update: int = 2
    Close: int = 3
    Other: int = 99


class ConfidenceID(IntEnum):
    """
    The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

    0 Unknown: The normalized confidence is unknown.
    1 Low
    2 Medium
    3 High
    99 Other: The confidence is not mapped to the defined enum values. See the confidence attribute, which contains a data source specific value.

    """

    Unknown: int = 0
    Low: int = 1
    Medium: int = 2
    High: int = 3
    Other: int = 99


class Finding(BaseEvent, BaseModel):
    """
    The Finding event is a generic event that defines a set of attributes available in the Findings category.

    Attributes:
    - Activity (activity_name) [Optional]: The finding activity name, as defined by the activity_id.
    - Activity ID (activity_id): The normalized identifier of the finding activity.
    - Comment (comment) [Optional]: A user provided comment about the finding.
    - Confidence (confidence) [Optional]: The confidence, normalized to the caption of the confidence_id value. In the case of 'Other', it is defined by the event source.
    - Confidence ID (confidence_id) [Optional]: Represents the accuracy of the detection rule. A low confidence indicates a broad finding scope that may include benign events.
    - Confidence Score (confidence_score) [Optional]: The confidence score as reported by the event source.
    - End Time (end_time) [Optional]: Time of the latest event included in the finding.
    - End Time DT (end_time_dt) [Optional]: Time of the latest event included in the finding in datetime format.
    - Finding Information (finding_info) [Required]: Describes the supporting information about a generated finding.
    - Start Time (start_time) [Optional]: Time of the earliest event included in the finding.
    - Start Time DT (start_time_dt) [Optional]: Time of the earliest event included in the finding in datetime

    """

    activity_name: Optional[str]
    activity_id: ActivityID
    comment: Optional[str]
    confidence: Optional[str]
    confidence_id: Optional[ConfidenceID]
    confidence_score: Optional[int]
    end_time: Optional[int]
    end_time_dt: Optional[datetime]
    finding_info: FindingInformation
    start_time: Optional[int]
    start_time_dt: Optional[datetime]
