from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel

from py_ocsf_models.objects.device_hardware_info import DeviceHardwareInfo
from py_ocsf_models.objects.geolocation import GeoLocation
from py_ocsf_models.objects.group import Group
from py_ocsf_models.objects.image import Image
from py_ocsf_models.objects.network_interface import NetworkInterface
from py_ocsf_models.objects.operating_system import OperatingSystem
from py_ocsf_models.objects.organization import Organization


class DeviceType(IntEnum):
    """
    Enum representing different types of devices.

    Attributes:
    - Unknown (0): The type is unknown.
    - Server (1): A server.
    - Desktop (2): A desktop computer.
    - Laptop (3): A laptop computer.
    - Tablet (4): A tablet computer.
    - Mobile (5): A mobile phone.
    - Virtual (6): A virtual machine.
    - IOT (7): An Internet of Things (IOT) device.
    - Browser (8): A web browser.
    - Firewall (9): A networking firewall.
    - Switch (10): A networking switch.
    - Hub (11): A networking hub.
    - Other (99): The type is not mapped. See the type attribute, which contains a data source specific value.
    """

    Unknown = 0
    Server = 1
    Desktop = 2
    Laptop = 3
    Tablet = 4
    Mobile = 5
    Virtual = 6
    IOT = 7
    Browser = 8
    Firewall = 9
    Switch = 10
    Hub = 11
    Other = 99


class RiskLevelID(IntEnum):
    """
    Enum representing different risk level IDs.

    Attributes:
    - Info (0): Informational risk level.
    - Low (1): Low risk level.
    - Medium (2): Medium risk level.
    - High (3): High risk level.
    - Critical (4): Critical risk level.
    """

    Info = 0
    Low = 1
    Medium = 2
    High = 3
    Critical = 4


class Device(BaseModel):
    """
    Represents a device, providing details such as hostname, IP address, operating system, etc.

    Attributes:
    - Alternate ID (uid_alt) [Optional]: An alternate unique identifier of the device, if any.
    - Autoscale UID (autoscale_uid) [Optional]: The unique identifier of the cloud autoscale configuration.
    - Compliant Device (is_compliant) [Optional]: Indicates if the event occurred on a compliant device.
    - Created Time (created_time) [Optional]: The time when the device was known to have been created.
    - Description (desc) [Optional]: The description of the device, as reported by the operating system.
    - Domain (domain) [Optional]: The network domain where the device resides.
    - First Seen (first_seen_time) [Optional]: The initial discovery time of the device.
    - Geo Location (location) [Optional]: The geographical location of the device.
    - Groups (groups) [Optional]: The group names to which the device belongs.
    - Hardware Info (hw_info) [Optional]: The endpoint hardware information.
    - Hostname (hostname) [Recommended]: The device hostname.
    - Hypervisor (hypervisor) [Optional]: The name of the hypervisor running on the device.
    - IMEI (imei) [Optional]: The International Mobile Station Equipment Identifier associated with the device.
    - IP Address (ip) [Recommended]: The device IP address, in either IPv4 or IPv6 format.
    - Image (image) [Optional]: The image used as a template to run the virtual machine.
    - Instance ID (instance_uid) [Recommended]: The unique identifier of a VM instance.
    - Last Seen (last_seen_time) [Optional]: The most recent discovery time of the device.
    - MAC Address (mac) [Optional]: The MAC address of the endpoint.
    - Managed Device (is_managed) [Optional]: Indicates if the event occurred on a managed device.
    - Modified Time (modified_time) [Optional]: The time when the device was last known to have been modified.
    - Name (name) [Recommended]: The alternate device name, ordinarily as assigned by an administrator.
    - Network Interface ID (interface_uid) [Recommended]: The unique identifier of the network interface.
    - Network Interface Name (interface_name) [Recommended]: The name of the network interface.
    - Network Interfaces (network_interfaces) [Optional]: The network interfaces associated with the device.
    - Network Zone (zone) [Optional]: The network zone or LAN segment.
    - OS (os) [Optional]: The endpoint operating system.
    - Organization (org) [Optional]: Organization and org unit related to the device.
    - Personal Device (is_personal) [Optional]: Indicates if the event occurred on a personal device.
    - Region (region) [Recommended]: The region where the virtual machine is located.
    - Risk Level (risk_level) [Optional]: The risk level of the device.
    - Risk Level ID (risk_level_id) [Optional]: The normalized risk level ID.
    - Risk Score (risk_score) [Optional]: The risk score as reported by the event source.
    - Subnet (subnet) [Optional]: The subnet mask.
    - Subnet UID (subnet_uid) [Optional]: The unique identifier of a virtual subnet.
    - Trusted Device (is_trusted) [Optional]: Indicates if the event occurred on a trusted device.
    - Type (type) [Optional]: The device type.
    - Type ID (type_id) [Required]: The device type ID.
    - Unique ID (uid) [Recommended]: The unique identifier of the device.
    - VLAN (vlan_uid) [Optional]: The Virtual LAN identifier.
    - VPC UID (vpc_uid) [Optional]: The unique identifier of the Virtual Private Cloud (VPC).
    """

    uid_alt: Optional[str] = None
    autoscale_uid: Optional[str] = None
    is_compliant: Optional[bool] = None
    created_time: Optional[datetime] = None
    desc: Optional[str] = None
    domain: Optional[str] = None
    first_seen_time: Optional[datetime] = None
    location: Optional[GeoLocation] = None
    groups: Optional[List[Group]] = None
    hw_info: Optional[DeviceHardwareInfo] = None
    hostname: str
    hypervisor: Optional[str] = None
    imei: Optional[str] = None
    ip: str
    image: Optional[Image] = None
    instance_uid: Optional[str] = None
    last_seen_time: Optional[datetime] = None
    mac: Optional[str] = None
    is_managed: Optional[bool] = None
    modified_time: Optional[datetime] = None
    name: str
    interface_uid: Optional[str] = None
    interface_name: Optional[str] = None
    network_interfaces: Optional[List[NetworkInterface]] = None
    zone: Optional[str] = None
    os: Optional[OperatingSystem] = None
    org: Optional[Organization] = None
    is_personal: Optional[bool] = None
    region: str
    risk_level: Optional[str] = None
    risk_level_id: Optional[RiskLevelID] = None
    risk_score: Optional[int] = None
    subnet: Optional[str] = None
    subnet_uid: Optional[str] = None
    is_trusted: Optional[bool] = None
    type: Optional[str] = None
    type_id: DeviceType
    uid: str
    vlan_uid: Optional[str] = None
    vpc_uid: Optional[str] = None
