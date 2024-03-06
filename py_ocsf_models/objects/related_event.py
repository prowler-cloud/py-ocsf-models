from typing import List, Optional

from pydantic import BaseModel

from py_ocsf_models.objects.mitre_attack import MITREAttack
from py_ocsf_models.objects.observable import Observable


class RelatedEvent(BaseModel):
    """
    Model representing a related event.

    The RelatedEvent class encapsulates information about an event related to a security incident,
    including details such as the Cyber Kill Chain phase, MITRE ATT&CK® details, observables,
    product identifier, event type, event type identifier, and unique identifier.

    Attributes:
    - Kill Chain (kill_chain) [Optional]: The Cyber Kill Chain® provides a detailed description of each phase and its associated activities within the broader context of a cyber attack.
    - MITRE ATT&CK® Details (attacks) [Optional]: An array of MITRE ATT&CK® objects describing the tactics, techniques & sub-techniques identified by a security control or finding.
    - Observables (observables) [Optional]: The observables associated with the event or a finding.
    - Product Identifier (product_uid) [Optional]: The unique identifier of the product that reported the related event.
    - Type (type) [Optional]: The type of the related event. For example: Process Activity: Launch.
    - Type ID (type_uid) [Recommended]: The unique identifier of the related event type. For example: 100701.
    - Unique ID (uid) [Required]: The unique identifier of the related event.
    """

    # TODO
    # kill_chain: Optional[List[KillChainPhase]]
    attacks: Optional[List[MITREAttack]]
    observables: Optional[List[Observable]]
    product_uid: Optional[str]
    type: Optional[str]
    type_uid: Optional[int]
    uid: str
