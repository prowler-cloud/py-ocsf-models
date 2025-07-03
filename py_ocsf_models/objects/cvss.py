from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.metric import Metric
from py_ocsf_models.objects.url import URL


class CVSSScore(BaseModel):
    """
    Common Vulnerability Scoring System (CVSS) details.
    """

    base_score: float
    depth: Optional[str]
    metrics: Optional[list[Metric]]
    overall_score: Optional[float]
    severity: Optional[str]
    src_url: Optional[URL]
    vector_string: Optional[str]
    vendor_name: Optional[str]
    version: Optional[str]
