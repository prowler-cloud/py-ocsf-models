from enum import IntEnum

from pydantic.v1 import BaseModel


class PhaseID(IntEnum):
    """
    The Kill Chain Phase object represents a single phase of a cyber attack, including the initial reconnaissance and planning stages up to the final objective of the attacker. It provides a detailed description of each phase and its associated activities within the broader context of a cyber attack.

    Attributes:
    - Unknown (0): The kill chain phase is unknown.
    - Reconnaissance (1): The attackers pick a target and perform a detailed analysis, start collecting information (email addresses, conferences information, etc.) and evaluate the victim’s vulnerabilities to determine how to exploit them.
    - Weaponization (2): The attackers develop a malware weapon and aim to exploit the discovered vulnerabilities.
    - Delivery (3): The intruders will use various tactics, such as phishing, infected USB drives, etc.
    - Exploitation (4): The intruders start leveraging vulnerabilities to executed code on the victim’s system.
    - Installation (5): The intruders install malware on the victim’s system.
    - Command & Control (6): Malware opens a command channel to enable the intruders to remotely manipulate the victim's system.
    - Actions on Objectives (7): With hands-on keyboard access, intruders accomplish the mission’s goal.
    - Other (99): The kill chain phase is not mapped. See the phase attribute, which contains a data source specific value.
    """

    Unknown = 0
    Reconnaissance = 1
    Weaponization = 2
    Delivery = 3
    Exploitation = 4
    Installation = 5
    Command_Control = 6
    Actions_on_Objectives = 7
    Other = 99


class KillChainPhase(BaseModel):
    """
    Base model representing a Cyber Kill Chain phase.

    Attributes:
    - Kill Chain Phase (phase) [Recommended]: The cyber kill chain phase.
    - Kill Chain Phase ID (phase_id) [Required]: The cyber kill chain phase identifier.
    """

    phase: str
    phase_id: PhaseID
