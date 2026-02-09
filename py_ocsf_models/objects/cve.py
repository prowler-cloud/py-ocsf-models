from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.cvss import CVSSScore
from py_ocsf_models.objects.cwe import CWE
from py_ocsf_models.objects.epss import EPSS
from py_ocsf_models.objects.product import Product


class CVE(BaseModel):
    """
    Common Vulnerabilities and Exposures (CVE) details.
    """

    created_time: Optional[datetime] = None
    cvss: Optional[list[CVSSScore]] = None
    desc: Optional[str] = None
    epss: Optional[EPSS] = None
    modified_time: Optional[datetime] = None
    product: Optional[Product] = None
    references: Optional[list[str]] = None
    related_cwes: Optional[list[CWE]] = None
    title: Optional[str] = None
    type: Optional[str] = None
    uid: str
