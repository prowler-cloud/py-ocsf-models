from typing import Optional
from pydantic import BaseModel
from enum import Enum



class TypeID(str, Enum):
#     0	Unknown
# The account type is unknown.
# 1	LDAP Account
# 2	Windows Account
# 3	AWS IAM User
# 4	AWS IAM Role
# 5	GCP Account
# 6	Azure AD Account
# 7	Mac OS Account
# 8	Apple Account
# 9	Linux Account
# 10	AWS Account
# 99	Other
    
class Account(BaseModel):
    """
    The Account object contains details about the account that initiated or performed a specific activity within a system or application.

    
    """
    name: str
    type: Optional[str]
    type_id: TypeID
    uid: str