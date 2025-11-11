from typing import Optional

from pydantic import BaseModel


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

    data: Optional[str] = None
    desc: Optional[str] = None
    group: Optional[str] = None
    is_applied: Optional[bool] = None
    name: Optional[str] = None
    uid: Optional[str] = None
    version: Optional[str] = None
