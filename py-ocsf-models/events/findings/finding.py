from datetime import datetime
from enum import Enum
from typing import Optional

from events.base_event import BaseEvent
from pydantic import BaseModel


class ActivityID(Enum):
    """
    The normalized identifier of the finding activity.

    0 Unknown: The event activity is unknown.
    1 Create: A finding was created.
    2 Update: A finding was updated.
    3 Close: A finding was closed.
    99 Other: The event activity is not mapped. See the activity_name attribute, which contains a data source specific value.
    """

    Unknown = 0
    Create = 1
    Update = 2
    Close = 3
    Other = 99


class ConfidenceID(Enum):
    """
    The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

    0 Unknown: The normalized confidence is unknown.
    1 Low
    2 Medium
    3 High
    99 Other: The confidence is not mapped to the defined enum values. See the confidence attribute, which contains a data source specific value.

    """

    Unknown = 0
    Low = 1
    Medium = 2
    High = 3
    Other = 99


class Finding(BaseEvent, BaseModel):
    """
    The Finding event is a generic event that defines a set of attributes available in the Findings category.

    Attributes:
    - Activity (activity_name) [Optional]: The finding activity name, as defined by the activity_id.
    - Comment (comment) [Optional]: A user provided comment about the finding.
    - Confidence (confidence) [Optional]: The confidence, normalized to the caption of the confidence_id value. In the case of 'Other', it is defined by the event source.
    - Confidence ID (confidence_id) [Optional]: Represents the accuracy of the detection rule. A low confidence indicates a broad finding scope that may include benign events.
    - Confidence Score (confidence_score) [Optional]: The confidence score as reported by the event source.
    - End Time (end_time) [Optional]: Timestamp of the most recent event included in the finding.
    - Finding Information (finding_info) [Required]: Describes the supporting information about a generated finding.
    - Start Time (start_time) [Optional]: Time of the earliest event included in the finding.

    """

    activity_name: Optional[str]
    activity_id: ActivityID
    comment: Optional[str]
    confidence: Optional[str]
    confidence_id: Optional[ConfidenceID]
    confidence_score: Optional[int]
    # TODO: comes from cloud
    # device: Optional[Device]
    end_time: Optional[datetime]
    # TODO
    # finding_info: FindingInformation
    start_time: Optional[datetime]
