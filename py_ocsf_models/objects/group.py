from typing import Optional

from pydantic import BaseModel


class Group(BaseModel):
    """
    The Group object represents a collection or association of entities, such as users, policies, or devices. It serves as a logical grouping mechanism to organize and manage entities with similar characteristics or permissions within a system or organization.

    Attributes:
    - Account Type (type) [Optional]: The type of the group or account.
    - Description (desc) [Optional]: The group description.
    - Domain (domain) [Optional]: The domain where the group is defined. For example: the LDAP or Active Directory domain.
    - Name (name) [Recommended]: The group name.
    - Privileges (privileges) [Optional]: The group privileges.
    - Unique ID	(uid) [Recommended]: TThe unique identifier of the group. For example, for Windows events this is the security identifier (SID) of the group.
    """

    type: Optional[str]
    desc: Optional[str]
    domain: Optional[str]
    name: Optional[str]
    privileges: Optional[list[str]]
    uid: Optional[str]
