from datetime import datetime
from pydantic.v1 import BaseModel
from typing import List, Optional

from py_ocsf_models.objects.cvss import CVSSScore
from py_ocsf_models.objects.epss import EPSS
from py_ocsf_models.objects.product import Product
from py_ocsf_models.objects.cwe import CWE



class CVE(BaseModel):
    """
    Common Vulnerabilities and Exposures (CVE) details.
    """
    created_time: Optional[datetime]
    cvss: Optional[CVSSScore]
    desc: Optional[str]
    epss: Optional[EPSS]
    modified_time: Optional[datetime]
    product: Optional[Product]
    references: Optional[List[str]]
    related_cwes: Optional[List[CWE]]
    title: Optional[str]
    type: Optional[str]
    uid: str
