from datetime import datetime
from typing import List, Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.cvss import CVSSScore
from py_ocsf_models.objects.cwe import CWE
from py_ocsf_models.objects.epss import EPSS
from py_ocsf_models.objects.product import Product


class CVE(BaseModel):
    """
    Common Vulnerabilities and Exposures (CVE) details.
    """

    created_time: Optional[datetime]
    cvss: Optional[list[CVSSScore]]
    desc: Optional[str]
    epss: Optional[EPSS]
    modified_time: Optional[datetime]
    product: Optional[Product]
    references: Optional[List[str]]
    related_cwes: Optional[List[CWE]]
    title: Optional[str]
    type: Optional[str]
    uid: str
