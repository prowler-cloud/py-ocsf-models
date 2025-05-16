from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.policy import Policy


class Assessment(BaseModel):
    """
    The Assessment object describes a point-in-time assessment, check, or evaluation of a specific configuration or signal against an asset, entity, person, or otherwise. For example, this can encapsulate os_signals from CrowdStrike Falcon Zero Trust Assessments, or account for Datastore configurations from Cyera, or capture details of Microsoft Intune configuration policies.

    Attributes:
    - Category (category) [Optional]: The Assessment object describes a point-in-time assessment, check, or evaluation of a specific configuration or signal against an asset, entity, person, or otherwise. For example, this can encapsulate os_signals from CrowdStrike Falcon Zero Trust Assessments, or account for Datastore configurations from Cyera, or capture details of Microsoft Intune configuration policies.
    - Description (desc) [Optional]: The description of the assessment criteria, or a description of the specific configuration or signal the assessment is targeting.
    - Meets Criteria (meets_criteria) [Optional]: Determines whether the assessment against the specific configuration or signal meets the assessments criteria. For example, if the assessment checks if a Datastore is encrypted or not, having encryption would be evaluated as true.
    - Name (name) [Optional]: The name of the configuration or signal being assessed. For example: Kernel Mode Code Integrity (KMCI) or publicAccessibilityState.
    - Policy (policy) [Optional]: The details of any policy associated with an assessment.
    - UID (uid) [Optional]: The unique identifier of the configuration or signal being assessed. For example: the signal_id.
    """

    category: Optional[str]
    desc: Optional[str]
    meets_criteria: Optional[bool]
    name: Optional[str]
    policy: Optional[Policy]
    uid: Optional[str]
