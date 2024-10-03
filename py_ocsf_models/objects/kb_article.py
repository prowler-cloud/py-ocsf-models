from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.operating_system import OperatingSystem
from py_ocsf_models.objects.product import Product


class KBArticle(BaseModel):
    """
    Describes a knowledgebase article, providing essential information such as its classification,
    release date, applicable operating system, and severity. It includes details like the article's
    size, source URL, and whether it has been superseded by another patch.

    Attributes:
    - classification: Vendor's classification of the KB article.
    - created_time: Time the KB article was created.
    - created_time_dt: Time the KB article was created in datetime
    - os: Operating system the KB article applies to.
    - bulletin: Bulletin identifier of the KB article.
    - product: Product details the KB article applies to.
    - severity: Severity rating of the KB article.
    - size: Size of the KB article in bytes.
    - src_url: Link to the KB article from the vendor.
    - is_superseded: Indicates if the article has been replaced by another.
    - title: Title of the KB article.
    - uid: Unique identifier for the KB article.
    """

    classification: Optional[str]
    created_time: Optional[int]
    created_time_dt: Optional[datetime]
    os: OperatingSystem
    bulletin: Optional[str]
    product: Optional[Product]
    severity: str
    size: Optional[int]
    src_url: Optional[str]
    is_superseded: Optional[bool]
    title: str
    uid: str
