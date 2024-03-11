from typing import Optional

from pydantic import BaseModel


class Enrichment(BaseModel):
    """
    Represents enrichment data associated with a specific attribute, providing additional context or information.
    This can include various types of data, depending on the enrichment type, such as location data for an IP address.

    Attributes:
    - data (dict): The JSON-formatted enrichment data, whose structure depends on the enrichment type.
    - name (str): The name of the attribute being enriched.
    - provider (str): The name of the provider supplying the enrichment data.
    - type (str): The type of enrichment, indicating the nature of the data provided.
    - value (str): The value of the attribute to which the enrichment data pertains.
    """

    data: dict[str, object]
    name: str
    provider: Optional[str]
    type: Optional[str]
    value: str
