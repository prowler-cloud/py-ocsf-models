from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.container import Container


class ContainerProfile(BaseModel):
    """
    The container context for a process.

    Attributes:
    - Container (container) [Recommended]: The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.
    - Namespace PID (namespace_pid) [Recommended]: If running under a process namespace (such as in a container), the process identifier within that process namespace.
    """

    container: Optional[Container]
    namespace_pid: Optional[int]
