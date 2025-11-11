from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.url import URL


class CWE(BaseModel):
    """
    Common Weakness Enumeration (CWE) details.
    """

    caption: Optional[str] = None
    src_url: Optional[URL] = None
    uid: str
