from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.events.findings.status_id import StatusID
from py_ocsf_models.objects.enrichment import Enrichment
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.observable import Observable


class BaseEvent(BaseModel):
    """
    The base event is a generic and concrete event. It also defines a set of attributes available in most event classes. As a generic event that does not belong to any event category, it could be used to log events that are not otherwise defined by the schema.

    Attributes:
    - Enrichments (enrichments) [Optional]: Additional information from external sources associated with the finding.
    - Message (message) [Optional]: Description of the event/finding as defined by the source.
    - Metadata (metadata) [Required]: Data providing context for the event/finding.
    - Observables (observables) [Optional]: Observable elements associated with the event/finding.
    - Raw Data (raw_data) [Optional]: Original data as received from the source.
    - Severity (severity) [Optional]: The event/finding severity, normalized to the caption of the severity_id value. In the case of 'Other', it is defined by the source.
    - Severity ID (severity_id) [Required]: The level of severity assigned to the event/finding.
    - Status (status) [Optional]: The normalized status of the Finding set by the consumer normalized to the caption of the status_id value. In the case of 'Other', it is defined by the source.
    - Status Code (status_code) [Optional]: The event status code, as reported by the event source. For example, in a Windows Failed Authentication event, this would be the value of 'Failure Code', e.g. 0x18.
    - Status Details (status_detail) [Optional]: The status details contains additional information about the event/finding outcome.
    - Status ID (status_id) [Optional]: The normalized status identifier of the Finding, set by the consumer.
    - Unmapped Data (unmapped) [Optional]: The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.
    """

    enrichments: Optional[list[Enrichment]]
    message: Optional[str]
    metadata: Metadata
    observables: Optional[list[Observable]]
    raw_data: Optional[str]
    severity_id: SeverityID
    severity: Optional[str]
    status: Optional[str]
    status_code: Optional[str]
    status_detail: Optional[str]
    status_id: Optional[StatusID]
    unmapped: Optional[object]
