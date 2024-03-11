from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.objects.device import Device
from py_ocsf_models.objects.product import Product


class SchemaExtension(BaseModel):
    """
    The OCSF Schema Extension object provides detailed information about the schema extension used to construct the event.

    Attributes:
    - Name (name) [Required]: The schema extension name (e.g., dev).
    - Unique ID (uid) [Required]: The unique identifier of the schema extension (e.g., 999).
    - Version (version) [Required]: The version of the schema extension (e.g., 1.0.0-alpha.2).
    """

    name: str
    uid: str
    version: str


class Logger(BaseModel):
    """
    The Logger object represents the device and product where events are stored with times for receipt and transmission. This may be at the source device where the event occurred, a remote scanning device, intermediate hops, or the ultimate destination.

    Attributes:
    - Device (device) [Recommended]: The device where the events are logged.
    - Log Level (log_level) [Optional]: The audit level at which an event was generated.
    - Log Name (log_name) [Recommended]: The event log name (e.g., syslog file name or Windows logging subsystem: Security).
    - Log Provider (log_provider) [Recommended]: The logging provider or logging service that logged the event (e.g., Microsoft-Windows-Security-Auditing).
    - Log Version (log_version) [Optional]: The event log schema version that specifies the format of the original event.
    - Logged Time (logged_time) [Optional]: The time when the logging system collected and logged the event.
    - Name (name) [Recommended]: The name of the logging product instance.
    - Product (product) [Recommended]: The product logging the event (e.g., event source product, management server product, SIEM, etc.).
    - Transmission Time (transmit_time) [Optional]: The time when the event was transmitted from the logging device to its next destination.
    - Unique ID (uid) [Recommended]: The unique identifier of the logging product instance.
    - Version (version) [Optional]: The version of the logging product.
    """

    device: Optional[Device]
    log_level: Optional[str]
    log_name: str
    log_provider: str
    log_version: Optional[str]
    logged_time: Optional[datetime]
    name: str
    product: Product
    transmit_time: Optional[datetime]
    uid: str
    version: Optional[str]


class Metadata(BaseModel):
    """
    The Metadata object describes the metadata associated with the event.

    Attributes:
    - Correlation UID (correlation_uid) [Optional]: Unique identifier used to correlate events.
    - Event Code (event_code) [Optional]: The Event ID or Code describing the event.
    - Event UID (uid) [Optional]: Logging system-assigned unique identifier of an event instance.
    - Labels (labels) [Optional]: List of category labels attached to the event or specific attributes.
    - Log Level (log_level) [Optional]: Audit level at which the event was generated.
    - Log Name (log_name) [Optional]: Event log name (e.g., syslog file name or Windows logging subsystem).
    - Log Provider (log_provider) [Optional]: Logging provider or service that logged the event.
    - Log Version (log_version) [Optional]: Event log schema version specifying the format of the original event.
    - Logged Time (logged_time) [Optional]: Time when the logging system collected and logged the event.
    - Loggers (loggers) [Optional]: Array of Logger objects describing the devices and logging products in the event flow.
    - Modified Time (modified_time) [Optional]: Time when the event was last modified or enriched.
    - Original Time (original_time) [Optional]: Original event time as reported by the event source.
    - Processed Time (processed_time) [Optional]: Event processed time, such as during an ETL operation.
    - Product (product) [Required]: Product that reported the event.
    - Profiles (profiles) [Optional]: List of profiles used to create the event.
    - Extensions (extensions) [Optional]: Schema extensions used to create the event.
    - Sequence (sequence) [Optional]: Sequence number of the event for unambiguous ordering.
    - Tenant UID (tenant_uid) [Optional]: Unique tenant identifier.
    - Version (version) [Required]: Version of the OCSF schema in Semantic Versioning Specification (SemVer).
    """

    correlation_uid: Optional[str]
    event_code: Optional[str]
    uid: Optional[str]
    labels: Optional[List[str]]
    log_level: Optional[str]
    log_name: Optional[str]
    log_provider: Optional[str]
    log_version: Optional[str]
    logged_time: Optional[datetime]
    loggers: Optional[List[Logger]]
    modified_time: Optional[datetime]
    original_time: Optional[str]
    processed_time: Optional[datetime]
    product: Product
    profiles: Optional[List[str]]
    extensions: Optional[List[SchemaExtension]]
    sequence: Optional[int]
    tenant_uid: Optional[str]
    version: str = OCSF_VERSION
