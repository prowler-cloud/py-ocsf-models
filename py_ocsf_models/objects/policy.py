from typing import Optional

from pydantic.v1 import BaseModel


class Policy(BaseModel):
    """
    The Policy object describes the policies that are applicable. Policy attributes provide traceability to the operational state of the security product at the time that the event was captured, facilitating forensics, troubleshooting, and policy tuning/adjustments.

    Attributes:
    - Data (data) [Optional]: Additional data about the policy such as the underlying JSON policy itself or other details.
    - Description (desc) [Optional]: The description of the policy.
    - Group (group) [Optional]: The policy group.
    - Is Applied (is_applied) [Optional]: A determination if the content of a policy was applied to a target or request, or not.
    - Name (name) [Optional]: The policy name. For example: IAM Policy.
    - UID (uid) [Optional]: A unique identifier of the policy instance.
    - Version (version) [Optional]: The policy version number.
    """

    data: Optional[str]
    desc: Optional[str]
    group: Optional[str]
    is_applied: Optional[bool]
    name: Optional[str]
    uid: Optional[str]
    version: Optional[str]
