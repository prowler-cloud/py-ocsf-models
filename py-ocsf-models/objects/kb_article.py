from datetime import datetime
from typing import Optional

from objects.operating_system import OperatingSystem
from objects.product import Product
from pydantic import BaseModel, HttpUrl


class KBArticle(BaseModel):
    """
    Describes a knowledgebase article, providing essential information such as its classification,
    release date, applicable operating system, and severity. It includes details like the article's
    size, source URL, and whether it has been superseded by another patch.

    Attributes:
    - classification: Vendor's classification of the KB article.
    - created_time: Release date of the KB article.
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
    created_time: Optional[datetime]
    os: OperatingSystem
    bulletin: Optional[str]
    product: Optional[Product]
    severity: str
    size: Optional[int]
    src_url: Optional[HttpUrl]
    is_superseded: Optional[bool]
    title: str
    uid: str
