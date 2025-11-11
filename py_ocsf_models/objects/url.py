from typing import Optional

from pydantic import BaseModel


class URL(BaseModel):
    """
    The Uniform Resource Locator (URL) object describes the characteristics of a URL.

    Attributes:
    """

    categories: Optional[list[str]] = None
    category_ids: Optional[list[int]] = None
    domain: Optional[str] = None
    hostname: Optional[str] = None
    path: Optional[str] = None
    port: Optional[int] = None
    query_string: Optional[str] = None
    resource_type: Optional[str] = None
    scheme: Optional[str] = None
    subdomain: Optional[str] = None
    url_string: Optional[str] = None
