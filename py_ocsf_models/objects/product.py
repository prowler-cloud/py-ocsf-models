from typing import Optional

from pydantic import BaseModel


class Feature(BaseModel):
    """
    Represents a specific feature of a product, detailing its name, unique identifier, and version.
    This class is useful for tracking features within products, especially for version control and
    identifying specific capabilities or components.

    Attributes:
    - name: The name of the feature.
    - uid: The unique identifier for the feature.
    - version: The version of the feature.
    """

    name: str
    uid: str
    version: str


class Product(BaseModel):
    """
    Represents product information, including its name, version, vendor, and potentially its feature set.
    It may also include localization details (language), installation specifics (path), and identification
    data like a CPE name or a unique identifier.

    Attributes:
    - feature: The feature within the product that reported the event.
    - lang: ISO 639-1 two-letter lowercase language code.
    - name: Name of the product.
    - path: Installation path of the product.
    - cpe_name: Common Platform Enumeration (CPE) identifier.
    - url_string: URL pointing to the product information.
    - uid: Unique identifier of the product.
    - vendor_name: Vendor of the product.
    - version: Version of the product.
    """

    feature: Optional[Feature]
    lang: Optional[str]
    name: str
    path: Optional[str]
    cpe_name: Optional[str]
    url_string: Optional[str]
    uid: str
    vendor_name: str
    version: Optional[str]
