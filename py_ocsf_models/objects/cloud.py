from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.account import Account
from py_ocsf_models.objects.organization import Organization


class Cloud(BaseModel):
    """
    The Cloud object contains information about a cloud account such as AWS Account ID, regions, etc.

    Attributes:
    - Account (account) [Optional]: The account object describes details about the account that was the source or target of the activity.
    - Network Zone (zone) [Optional]: The availability zone in the cloud region, as defined by the cloud provider.
    - Organization (org) [Optional]: Organization and org unit relevant to the event or object.
    - Project ID (project_uid) [Optional]: The unique identifier of a Cloud project.
    - Provider (provider) [Required]: The unique name of the Cloud services provider, such as AWS, MS Azure, GCP, etc.
    - Region (region) [Recommended]: The name of the cloud region, as defined by the cloud provider.
    """

    account: Optional[Account]
    zone: Optional[str]
    org: Optional[Organization]
    project_uid: Optional[str]
    provider: str
    region: Optional[str]
