from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.account import Account
from py_ocsf_models.objects.group import Group
from py_ocsf_models.objects.ldap_person import LDAPPerson
from py_ocsf_models.objects.organization import Organization


class User(BaseModel):
    """
    The User object describes the characteristics of a user/person or a security principal. Defined by D3FEND d3f:UserAccount.

    Attributes:
    - Account (account) [Optional]: The user's account or the account associated with the user.
    - Alternate ID (uid_alt) [Optional]: The alternate user identifier. For example, the Active Directory user GUID or AWS user Principal ID.
    - Domain (domain) [Optional]: The domain where the user is defined. For example: the LDAP or Active Directory domain.
    - Email Address (email_addr) [Optional]: The user's primary email address.
    - Full Name (full_name) [Optional]: The full name of the person, as per the LDAP Common Name attribute (cn).
    - Groups (groups) [Optional]: The administrative groups to which the user belongs.
    - LDAP Person (ldap_person) [Optional]: The additional LDAP attributes that describe a person.
    - Name (name) [Recommended]: The username. For example, janedoe1.
    - Organization (org) [Optional]: Organization and org unit related to the user.
    - Type (type) [Optional]: The type of the user. For example, System, AWS IAM User, etc.
    - Type ID (type_id) [Recommended]: The account type identifier.
    - Unique ID (uid) [Recommended]: The unique user identifier. For example, the Windows user SID, ActiveDirectory DN or AWS user ARN.
    - User Credential ID (credential_uid) [Optional]: The unique identifier of the user's credential. For example, AWS Access Key ID.
    """

    account: Account
    uid_alt: Optional[str]
    domain: Optional[str]
    email_addr: Optional[str]
    groups: Optional[list[Group]]
    ldap_person: Optional[LDAPPerson]
    name: str
    org: Optional[Organization]
    type: Optional[str]
    type_id: int
    uid: str
    credential_uid: Optional[str]
