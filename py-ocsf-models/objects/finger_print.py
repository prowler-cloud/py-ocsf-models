from typing import Optional

from pydantic import BaseModel


class AlgorithmID(int, Enum):
    Unknown = 0
    MD5 = 1
    SHA_1 = 2
    SHA_256 = 3
    SHA_512 = 4
    CTPH = 5  # Context Triggered Piecewise Hashing (also known as ssdeep)
    TLSH = 6
    QuickXorHash = 7
    Other = 99


class FingerPrint(BaseModel):
    """
    Represents a digital fingerprint created using a specific hashing algorithm. This class
    encapsulates details about the algorithm used and the resulting hash value.

    Attributes:
    - algorithm (Optional[str]): The name of the hash algorithm, if 'Other', defined by the event source.
    - algorithm_id (AlgorithmID): The identifier of the hash algorithm used.
    - value (str): The hash value or the digital fingerprint itself.
    """

    algorithm: Optional[str]
    algorithm_id: AlgorithmID
    value: str
