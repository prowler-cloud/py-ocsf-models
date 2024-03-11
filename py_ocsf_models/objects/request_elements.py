from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.container import Container


class RequestElements(BaseModel):
    """
    Represents the elements of an API request, especially in containerized applications.
    It includes details about the containers involved, any additional data associated with the request,
    communication flags, and a unique identifier for the request.

    Attributes:
    - containers: An array of containers involved in the API request/response process.
    - data: Additional JSON-formatted data associated with the API request.
    - flags: A list of communication flags indicating specific characteristics or behaviors of the request.
    - uid: A unique identifier for the API request.
    """

    containers: Optional[list[Container]]
    data: Optional[dict[str, object]]
    flags: Optional[list[str]]
    uid: str
