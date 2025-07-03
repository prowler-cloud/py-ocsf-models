from datetime import datetime
from typing import Optional

from pydantic.v1 import BaseModel


class EPSS(BaseModel):
    """
    The Exploit Prediction Scoring System (EPSS) object describes the estimated probability a vulnerability will be exploited. EPSS is a community-driven effort to combine descriptive information about vulnerabilities (CVEs) with evidence of actual exploitation in-the-wild. (EPSS).
    """

    created_time: Optional[datetime]
    percentile: Optional[float]
    score: str
    version: Optional[str]
