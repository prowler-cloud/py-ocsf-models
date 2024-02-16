from typing import List, Optional

from pydantic import BaseModel


class Service(BaseModel):
    """
    Encapsulates information about a service, including its name, unique identifier, version, and any associated labels.
    This model is designed to represent services in a microservices architecture or within any application ecosystem, providing
    a way to uniquely identify and describe services.

    Attributes:
    - labels (Optional[List[str]]): A list of labels or tags associated with the service, providing additional metadata.
    - name (str): The name of the service, clearly identifying it within the system.
    - uid (str): A unique identifier for the service, ensuring distinct recognition.
    - version (str): The version of the service, helping to track changes or updates over time.
    """

    labels: Optional[List[str]]
    name: str
    uid: str
    version: str
