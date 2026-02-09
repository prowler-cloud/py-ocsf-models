"""OCSF Profile validation module.

This module provides profile validation for OCSF events and findings.
Profiles are optional overlays that add requirements to events.

Currently implemented profiles:
- cloud: Requires the cloud field to be populated
- datetime: No required fields (about having *_dt datetime variants)

Other profiles will raise NotImplementedError until implemented.

Usage:
    from py_ocsf_models.profiles import OCSFProfile, validate_profiles

    # Validate against metadata.profiles
    validate_profiles(finding)

    # Validate against explicit profiles
    validate_profiles(finding, profiles=["cloud", "datetime"])

    # Collect errors without raising
    errors = validate_profiles(finding, raise_on_error=False)
"""

from enum import Enum

from py_ocsf_models.profiles.validators import ProfileValidationError, validate_profiles


class OCSFProfile(str, Enum):
    """OCSF Profiles - values match metadata.profiles strings.

    Only Cloud and DateTime are currently implemented.
    Other profiles will raise NotImplementedError.
    """

    CLOUD = "cloud"
    DATETIME = "datetime"
    # Future profiles (not yet implemented):
    # SECURITY_CONTROL = "security_control"
    # HOST = "host"
    # OSINT = "osint"
    # CONTAINER = "container"
    # INCIDENT = "incident"


__all__ = [
    "OCSFProfile",
    "ProfileValidationError",
    "validate_profiles",
]
