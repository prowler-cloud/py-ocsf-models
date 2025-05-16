from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.api import API
from py_ocsf_models.objects.device import Device
from py_ocsf_models.objects.dns_query import DNSQuery
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.url import URL
from py_ocsf_models.objects.verdict import VerdictID


class EvidenceArtifacts(BaseModel):
    """
    A collection of evidence artifacts associated to the activity/activities that triggered a security detection.


    Attributes:
    - API Details (api) [Recommended]: Describes details about the API call associated with the activity that triggered the detection.
    - DNS Query (query) [Recommended]: Describes details about the DNS query associated with the activity that triggered the detection.
    - Data (data) [Optional]: Additional evidence data that is not accounted for in the specific evidence attributes. Use only when absolutely necessary.
    - Device (device) [Optional]: An addressable device, computer system or host associated to the activity that triggered the detection.
    - Name (name) [Optional]: The naming convention or type identifier of the evidence associated with the security detection. For example, the @odata.type from Microsoft Graph Alerts V2 or display_name from CrowdStrike Falcon Incident Behaviors.
    - Resources (resources) [Optional]: Describes details about the cloud resources directly related to activity that triggered the detection. For resources impacted by the detection, use Affected Resources at the top-level of the finding.
    - URL (url) [Optional]: The URL that pertains to the event or object associated to the activity that triggered the detection.
    - Verdict ID (verdict_id) [Optional]: The normalized verdict (or status) ID of the evidence associated with the security detection. For example, Microsoft Graph Security Alerts contain a verdict enumeration for each type of evidence associated with the Alert. This is typically set by an automated investigation process or an analyst/investigator assigned to the finding.
    """

    api: Optional[API]
    # TODO
    # actor: Optional[Actor]
    # connection_info: Optional[NetworkConnectionInformation]
    data: Optional[dict[str, object]]
    # TODO
    # dst_endpoint: Optional[NetworkEndpoint]
    # file: Optional[File]
    # process: Optional[Process]
    # src_endpoint: Optional[NetworkEndpoint]
    device: Optional[Device]
    name: Optional[str]
    query: Optional[DNSQuery]
    resources: Optional[list[ResourceDetails]]
    url: Optional[URL]
    verdict_id: Optional[VerdictID] = VerdictID.Unknown
