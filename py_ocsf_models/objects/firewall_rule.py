from typing import Optional

from pydantic import BaseModel


class FirewallRule(BaseModel):
    """
    The Firewall Rule object describes a firewall rule that triggered or matched.

    Constraint: At least one of name, uid must be present.

    Attributes:
    - Category (category) [Optional]: The rule category.
    - Condition (condition) [Optional]: The rule condition expression.
    - Description (desc) [Optional]: The description of the rule.
    - Duration (duration) [Optional]: The rule duration in milliseconds.
    - Match Details (match_details) [Optional]: Details about what matched the rule.
    - Match Location (match_location) [Optional]: The location in the request/response that matched.
    - Name (name) [Recommended]: The name of the rule.
    - Rate Limit (rate_limit) [Optional]: The rate limit value.
    - Sensitivity (sensitivity) [Optional]: The sensitivity level.
    - Type (type) [Optional]: The rule type.
    - UID (uid) [Recommended]: The unique identifier of the rule.
    - Version (version) [Optional]: The rule version.
    """

    category: Optional[str] = None
    condition: Optional[str] = None
    desc: Optional[str] = None
    duration: Optional[int] = None
    match_details: Optional[list[str]] = None
    match_location: Optional[str] = None
    name: Optional[str] = None
    rate_limit: Optional[int] = None
    sensitivity: Optional[str] = None
    type: Optional[str] = None
    uid: Optional[str] = None
    version: Optional[str] = None
