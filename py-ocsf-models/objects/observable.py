from typing import Optional

from pydantic import BaseModel


class Observable(BaseModel):
    """
    The observable object is a pivot element that contains related information found in many places in the event.

    Attributes:
    - Name (name): The full name of the observable attribute. The name is a pointer/reference to an attribute within the event data. For example: file.name.
    - Reputation Scores (reputation) [Optional]: Contains the original and normalized reputation scores.
    - Type (type) [Optional]: The observable value type name.
    - Type ID (type_id): The observable value type identifier.
    - Value (value) [Optional]: The value associated with the observable attribute. The meaning of the value depends on the observable type. If the name refers to a scalar attribute, then the value is the value of the attribute. If the name refers to an object attribute, then the value is not populated.
    """

    name: str
    # TODO
    # reputation: Optional[Reputation]
    type: Optional[str]
    # TODO
    # type_id: TypeID
    value: Optional[str]
