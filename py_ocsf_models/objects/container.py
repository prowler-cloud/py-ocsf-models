from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from py_ocsf_models.objects.fingerprint import FingerPrint
from py_ocsf_models.objects.image import Image


class Container(BaseModel):
    """
    Represents a container instance within a containerized application environment, detailing its image source,
    operational parameters, and unique identifiers.

    Attributes:
    - hash: The commit or SHA256 hash of the container image.
    - image: The container image details including name and potentially its tag.
    - tag: The image tag, specifying version, format, or OS.
    - name: The name of the container.
    - network_driver: The network driver used by the container.
    - orchestrator: The orchestrator managing the container.
    - pod_uuid: The unique identifier of the pod hosting the container.
    - runtime: The container runtime backend.
    - size: The size of the container image in bytes.
    - uid: The unique identifier for this container instance.
    """

    hash: Optional[FingerPrint]
    image: Optional[Image]
    tag: Optional[str]
    name: str
    network_driver: Optional[str]
    orchestrator: Optional[str]
    pod_uuid: Optional[UUID]
    runtime: Optional[str]
    size: Optional[int]
    uid: str
