from typing import Optional

from pydantic.v1 import BaseModel


class Analytic(BaseModel):
    """
    The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.

    Attributes:
    - Category (category) [Optional]: The analytic category.
    - Description (desc) [Optional]: The description of the analytic that generated the finding.
    - Name (name) [Recommended]: The name of the analytic that generated the finding.
    - Type (type) [Optional]: The analytic type.
    - Type ID (type_id) [Required]: The analytic type ID.
    - Unique ID (uid) [Recommended]: The unique identifier of the analytic that generated the finding.
    - Version (version) [Optional]: The analytic version. For example: 1.1.
    """

    category: Optional[str]
    desc: Optional[str]
    name: str
    type: Optional[str]
    type_id: int
    uid: str
    version: Optional[str]
