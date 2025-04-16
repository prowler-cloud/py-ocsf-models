from enum import IntEnum
from typing import Optional

from pydantic.v1 import BaseModel


class TypeID(IntEnum):
    Unknown = 0
    LDAP_Account = 1
    Windows_Account = 2
    AWS_IAM_User = 3
    AWS_IAM_Role = 4
    GCP_Account = 5
    Azure_AD_Account = 6
    MacOS_Account = 7
    Apple_Account = 8
    Linux_Account = 9
    AWS_Account = 10
    Other = 99


class Account(BaseModel):
    """
    The Account object contains details about the account that initiated or performed a specific activity within a system or application.

    Attributes:
    - Name (name) [Recommended]: The name of the account (e.g. GCP Account Name).
    - Type (type) [Optional]: The account type, normalized to the caption of 'account_type_id'. In the case of 'Other', it is defined by the event source.
    - Type ID (type_id) [Recommended]: The normalized account type identifier.
    - Unique ID (uid) [Recommended]: The unique identifier of the account (e.g. AWS Account ID).
    - Labels (labels) [Optional]: The labels associated with the account.

    """

    name: str
    type: Optional[str]
    type_id: TypeID
    uid: str
    labels: Optional[list[str]]
