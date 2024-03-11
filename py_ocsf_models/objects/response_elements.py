from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.container import Container


class ResponseElements(BaseModel):
    """
    Represents the elements of an API response, particularly useful in containerized applications for capturing the output of containers, the response data, any associated error codes or messages, communication flags, and a descriptive message about the response.

    Attributes:
    - Containers (containers) [Optional]: When working with containerized applications, the set of containers which write to the standard the output of a particular logging driver. For example, this may be the set of containers involved in handling api requests and responses for a containerized application.
    - Data(data) [Optional]: The additional data that is associated with the api response.
    - Error Code (error) [Optional]: Error code associated with the response.
    - Error Message	(error_message) [Optional]: Descriptive error message.
    - Flags	(flags) [Optional]: The list of communication flags, normalized to the captions of the flag_ids values. In the case of 'Other', they are defined by the event source.
    - Message (message) [Optional]: The description of the event/finding, as defined by the source.
    - Response Code	(code) [Optional]: The numeric response sent to a request.

    """

    containers: Optional[list[Container]]
    data: Optional[dict[str, object]]
    error: Optional[str]
    error_message: Optional[str]
    flags: Optional[list[str]]
    message: Optional[str]
    code: Optional[int]
