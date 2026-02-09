from typing import Optional

from pydantic import BaseModel

from py_ocsf_models.objects.policy import Policy


class AuthorizationResult(BaseModel):
    """
    The Authorization Result object describes the outcome of an authorization decision.

    Attributes:
    - Decision (decision) [Recommended]: The authorization result/outcome, e.g. "allowed", "denied".
    - Policy (policy) [Optional]: Details about the Identity/Access management policies that are applicable.
    """

    decision: Optional[str] = None
    policy: Optional[Policy] = None
