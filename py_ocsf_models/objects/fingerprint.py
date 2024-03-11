from enum import IntEnum
from typing import Optional

from pydantic import BaseModel


class AlgorithmID(IntEnum):
    """
    The identifier of the normalized hash algorithm, which was used to create the digital fingerprint.

    0 Unknown: The algorithm is unknown.
    1 MD5: MD5 message-digest algorithm producing a 128-bit (16-byte) hash value.
    2 SHA-1: Secure Hash Algorithm 1 producing a 160-bit (20-byte) hash value.
    3 SHA-256: Secure Hash Algorithm 2 producing a 256-bit (32-byte) hash value.
    4 SHA-512: Secure Hash Algorithm 2 producing a 512-bit (64-byte) hash value.
    5 CTPH: The ssdeep generated fuzzy checksum. Also known as Context Triggered Piecewise Hash (CTPH).
    6 TLSH: The TLSH fuzzy hashing algorithm.
    7 quickXorHash: Microsoft simple non-cryptographic hash algorithm that works by XORing the bytes in a circular-shifting fashion.
    99 Other: The algorithm is not mapped. See the algorithm attribute, which contains a data source specific value.

    """

    Unknown: int = 0
    MD5: int = 1
    SHA_1: int = 2
    SHA_256: int = 3
    SHA_512: int = 4
    CTPH: int = 5
    TLSH: int = 6
    QuickXorHash: int = 7
    Other: int = 99


class FingerPrint(BaseModel):
    """
    Represents a digital fingerprint created using a specific hashing algorithm. This class
    encapsulates details about the algorithm used and the resulting hash value.

    Attributes:
    - Algorithm (algorithm) [Optional]: The hash algorithm used to create the digital fingerprint, normalized to the caption of 'algorithm_id'. In the case of 'Other', it is defined by the event source.
    - Algorithm ID (algorithm_id): The identifier of the normalized hash algorithm, which was used to create the digital fingerprint.
    - Value (value): The digital fingerprint value.
    """

    algorithm: Optional[str]
    algorithm_id: AlgorithmID
    value: str
