from typing import Optional

from pydantic.v1 import BaseModel

from py_ocsf_models.objects.url import URL


class CWE(BaseModel):
    """
    Common Weakness Enumeration (CWE) details.
    """

    caption: Optional[str]
    src_url: Optional[URL]
    uid: str
