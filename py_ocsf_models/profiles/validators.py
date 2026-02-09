"""Declarative profile validation with type-safe Protocols.

Currently implemented profiles: cloud, datetime
Other profiles will raise NotImplementedError.

Usage:
    from py_ocsf_models.profiles.validators import validate_profiles

    # Validate using metadata.profiles
    validate_profiles(finding)

    # Validate with explicit profiles
    validate_profiles(finding, profiles=["cloud"])

    # Collect errors without raising
    errors = validate_profiles(finding, raise_on_error=False)
"""

import builtins
from typing import Any, Optional

# ExceptionGroup is built-in in Python 3.11+, None otherwise
_ExceptionGroup: type | None = getattr(builtins, "ExceptionGroup", None)


class ProfileValidationError(ValueError):
    """Raised when a finding doesn't satisfy profile requirements.

    Attributes:
        profile: The profile name that failed validation.
        field: The field that is missing or invalid.
    """

    def __init__(self, profile: str, field: str, message: str = "required") -> None:
        self.profile = profile
        self.field = field
        super().__init__(f"[{profile}] {field}: {message}")


# Declarative profile requirements - DRY, easy to extend
# Each profile maps to a dict with "required" and "optional" field lists
PROFILE_REQUIREMENTS: dict[str, dict[str, list[str]]] = {
    "cloud": {"required": ["cloud"], "optional": ["api"]},
    "datetime": {
        "required": [],
        "optional": ["time_dt", "start_time_dt", "end_time_dt"],
    },
    # DateTime has no required fields - it's about having *_dt variants available
}

# Profiles not yet implemented (will raise NotImplementedError)
NOT_IMPLEMENTED_PROFILES = frozenset(
    {"security_control", "host", "osint", "container", "incident"}
)


def _validate_single_profile(
    finding: Any, profile: str
) -> list[ProfileValidationError]:
    """Validate a finding against a single profile's requirements.

    Args:
        finding: The finding to validate.
        profile: The profile name to validate against.

    Returns:
        List of validation errors (empty if valid).

    Raises:
        NotImplementedError: If the profile is not yet supported.
    """
    if profile in NOT_IMPLEMENTED_PROFILES:
        raise NotImplementedError(f"Profile '{profile}' is not yet supported.")

    reqs = PROFILE_REQUIREMENTS.get(profile)
    if reqs is None:
        return []  # Unknown profile - no requirements to check

    errors: list[ProfileValidationError] = []
    for field in reqs.get("required", []):
        if getattr(finding, field, None) is None:
            errors.append(ProfileValidationError(profile, field))
    return errors


def validate_profiles(
    finding: Any,
    profiles: Optional[list[str]] = None,
    raise_on_error: bool = True,
) -> list[ProfileValidationError]:
    """Validate a finding against profiles.

    If profiles is None, reads from finding.metadata.profiles.

    Args:
        finding: The finding to validate.
        profiles: Explicit list of profile names, or None to use metadata.profiles.
        raise_on_error: If True, raises ExceptionGroup on validation errors.

    Returns:
        List of validation errors (empty if valid).

    Raises:
        NotImplementedError: If a profile is not yet supported.
        ExceptionGroup: If raise_on_error=True and validation fails (Python 3.11+).
        ProfileValidationError: If raise_on_error=True and validation fails (Python < 3.11).

    Example:
        >>> finding = DetectionFinding(cloud=None, ...)
        >>> validate_profiles(finding, profiles=["cloud"])
        ExceptionGroup: Profile validation failed  # Python 3.11+
          ProfileValidationError: [cloud] cloud: required
    """
    if profiles is None:
        profiles = getattr(finding.metadata, "profiles", None) or []

    all_errors: list[ProfileValidationError] = []
    for profile in profiles:
        all_errors.extend(_validate_single_profile(finding, profile))

    if raise_on_error and all_errors:
        if _ExceptionGroup is not None:
            raise _ExceptionGroup("Profile validation failed", all_errors)
        # Fallback for Python < 3.11: raise first error, note others in message
        first = all_errors[0]
        if len(all_errors) > 1:
            msg = f"{first} (and {len(all_errors) - 1} more errors)"
            raise ProfileValidationError(first.profile, first.field, msg)
        raise first
    return all_errors
