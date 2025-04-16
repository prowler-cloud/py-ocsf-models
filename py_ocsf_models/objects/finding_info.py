from datetime import datetime
from typing import List, Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.analytic import Analytic
from py_ocsf_models.objects.kill_chain_phase import KillChainPhase
from py_ocsf_models.objects.mitre_attack import MITREAttack
from py_ocsf_models.objects.related_event import RelatedEvent


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
    related_analytics: Optional[List[Analytic]]
    related_events: Optional[List[RelatedEvent]]
    src_url: Optional[str]
    title: str
    types: Optional[List[str]]
    uid: str
