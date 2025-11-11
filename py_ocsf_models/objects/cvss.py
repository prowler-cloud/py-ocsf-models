from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.metric import Metric
from py_ocsf_models.objects.url import URL


class CVSSScore(BaseModel):
    """
    Common Vulnerability Scoring System (CVSS) details.
    """

    base_score: float
    depth: Optional[str] = None
    metrics: Optional[list[Metric]] = None
    overall_score: Optional[float] = None
    severity: Optional[str] = None
    src_url: Optional[URL] = None
    vector_string: Optional[str] = None
    vendor_name: Optional[str] = None
    version: Optional[str] = None
