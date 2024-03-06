from typing import Optional

from objects.api import API
from objects.cloud import Cloud
from pydantic import BaseModel


class CloudProfile(BaseModel):
    """
    The attributes that describe information specific to Cloud services/applications.

    Attributes:
    - API Details (api) [Optional]: Describes details about a typical API (Application Programming Interface) call.
    - Cloud (cloud): Describes details about the Cloud environment where the event was originally created or logged.
    """

    api: Optional[API]
    cloud: Cloud
