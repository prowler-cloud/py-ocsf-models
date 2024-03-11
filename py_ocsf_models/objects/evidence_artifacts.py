from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.api import API
from py_ocsf_models.objects.dns_query import DNSQuery


class EvidenceArtifacts(BaseModel):
    """
    A collection of evidence artifacts associated to the activity/activities that triggered a security detection.


    Attributes:
    - API Details (api) [Recommended]: Describes details about the API call associated with the activity that triggered the detection.
    - Actor (actor) [Recommended]: Describes details about the user/role/process that was the source of the activity that triggered the detection.
    - Connection Info (connection_info) [Recommended]: Describes details about the network connection associated with the activity that triggered the detection.
    - DNS Query (query) [Recommended]: Describes details about the DNS query associated with the activity that triggered the detection.
    - Data (data) [Optional]: Additional evidence data that is not accounted for in the specific evidence attributes. Use only when absolutely necessary.
    - Destination Endpoint (dst_endpoint) [Recommended]: Describes details about the destination of the network activity that triggered the detection.
    - File (file) [Recommended]: Describes details about the file associated with the activity that triggered the detection.
    - Process (process) [Recommended]: Describes details about the process associated with the activity that triggered the detection.
    - Source Endpoint (src_endpoint) [Recommended]: Describes details about the source of the network activity that triggered the detection.
    """

    api: Optional[API]
    # TODO
    # actor: Optional[Actor]
    # connection_info: Optional[NetworkConnectionInformation]
    query: Optional[DNSQuery]
    data: Optional[dict[str, object]]
    # TODO
    # dst_endpoint: Optional[NetworkEndpoint]
    # file: Optional[File]
    # process: Optional[Process]
    # src_endpoint: Optional[NetworkEndpoint]
