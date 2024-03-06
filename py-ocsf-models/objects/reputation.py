from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ScoreID(Enum):
    """
    The normalized reputation score identifier.

    0	Unknown: The reputation score is unknown.
    1	Very Safe: Long history of good behavior.
    2	Safe: Consistently good behavior.
    3	Probably Safe: Reasonable history of good behavior.
    4	Leans Safe: Starting to establish a history of normal behavior.
    5	May not be Safe: No established history of normal behavior.
    6	Exercise Caution: Starting to establish a history of suspicious or risky behavior.
    7	Suspicious/Risky: A site with a history of suspicious or risky behavior. (spam, scam, potentially unwanted software, potentially malicious).
    8	Possibly Malicious: Strong possibility of maliciousness.
    9	Probably Malicious: Indicators of maliciousness.
    10	Malicious: Proven evidence of maliciousness.
    99	Other: The reputation score is not mapped. See the rep_score attribute, which contains a data source specific value.
    """

    Unkwown: 0
    VerySafe: 1
    Safe: 2
    ProbablySafe: 3
    LeansSafe: 4
    MayNotBeSafe: 5
    ExerciseCaution: 6
    SuspiciousRisky: 7
    PossiblyMalicious: 8
    ProbablyMalicious: 9
    Malicious: 10
    Other: 99


class Reputation(BaseModel):
    """
    Reputation object describes the reputation/risk score of an entity (e.g. device, user, domain).

    Attributes:
    - Reputation Score (base_score): The reputation score as reported by the event source.
    - Provider (provider): The provider of the reputation information.
    - Reputation Score (score) [Optional]: An additional score associated with the reputation.
    - Reputation Score ID (score_id): The normalized reputation score identifier.
    """

    base_score: int
    provider: Optional[str]
    score: Optional[float]
    score_id: ScoreID
