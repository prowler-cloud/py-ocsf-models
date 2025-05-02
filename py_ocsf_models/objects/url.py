from typing import Optional

from pydantic.v1 import BaseModel


class URL(BaseModel):
    """
    The Uniform Resource Locator (URL) object describes the characteristics of a URL.

    Attributes:
    """

    categories: Optional[list[str]]
    category_ids: Optional[list[int]]
    domain: Optional[str]
    hostname: Optional[str]
    path: Optional[str]
    port: Optional[int]
    query_string: Optional[str]
    resource_type: Optional[str]
    scheme: Optional[str]
    subdomain: Optional[str]
    url_string: Optional[str]
