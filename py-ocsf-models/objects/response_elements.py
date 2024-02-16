from typing import Dict, Optional

from objects.container import Container
from pydantic import BaseModel


class ResponseElements(BaseModel):
    """
    Represents the elements of an API response, particularly useful in containerized applications for capturing the output of containers, the response data, any associated error codes or messages, communication flags, and a descriptive message about the response.

    Attributes:
    - containers (Optional[list[Container]]): Set of containers related to the API response.
    - data (Optional[Dict]): Additional JSON-formatted data associated with the API response.
    - error (Optional[str]): Error code associated with the response.
    - error_message (Optional[str]): Descriptive error message.
    - flags (Optional[list[str]]): Communication flags providing context about the response.
    - message (Optional[str]): General description or findings from the API response.
    - code (Optional[int]): Numeric response code indicating the outcome of the API request.
    """

    containers: Optional[list[Container]]
    data: Optional[Dict]
    error: Optional[str]
    error_message: Optional[str]
    flags: Optional[list[str]]
    message: Optional[str]
    code: Optional[int]
