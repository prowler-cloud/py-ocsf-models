from typing import Optional

from objects.group import Group
from objects.request_elements import RequestElements
from objects.response_elements import ResponseElements
from objects.service import Service
from pydantic import BaseModel


class API(BaseModel):
    """
    Represents the details of an API interaction, including both request and response elements,
    as well as metadata about the API's operation and the service it belongs to.

    Attributes:
    - request (Optional[RequestElements]): Details pertaining to the API request.
    - response (Optional[ResponseElements]): Details pertaining to the API response.
    - group (Optional[Group]): Information about the API group, if applicable.
    - operation (str): The HTTP verb or operation associated with the API request, such as GET, POST, PUT, DELETE.
    - service (Optional[Service]): Information about the API service, including its name and other relevant details.
    - version (Optional[str]): The version of the API, indicating the specific iteration of the API service being used.
    """

    request: Optional[RequestElements]
    response: Optional[ResponseElements]
    group: Optional[Group]
    operation: str
    service: Optional[Service]
    version: Optional[str]
