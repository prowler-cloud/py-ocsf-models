from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.api import API
from py_ocsf_models.objects.cloud import Cloud


class CloudProfile(BaseModel):
    """
    The attributes that describe information specific to Cloud services/applications.

    Attributes:
    - API Details (api) [Optional]: Describes details about a typical API (Application Programming Interface) call.
    - Cloud (cloud): Describes details about the Cloud environment where the event was originally created or logged.
    """

    api: Optional[API]
    cloud: Cloud
