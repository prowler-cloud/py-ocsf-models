"""Tests for the profile validation module."""

import builtins
from datetime import datetime

import pytest

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.findings.activity_id import ActivityID
from py_ocsf_models.events.findings.detection_finding import DetectionFinding
from py_ocsf_models.events.findings.detection_finding_type_id import (
    DetectionFindingTypeID,
)
from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.objects.cloud import Cloud
from py_ocsf_models.objects.finding_info import FindingInformation
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.product import Product
from py_ocsf_models.profiles import (
    OCSFProfile,
    ProfileValidationError,
    validate_profiles,
)

# ExceptionGroup is Python 3.11+
_ExceptionGroup: type | None = getattr(builtins, "ExceptionGroup", None)


def _create_minimal_finding(**kwargs) -> DetectionFinding:
    """Create a minimal DetectionFinding for testing."""
    defaults = {
        "activity_id": ActivityID.Create,
        "metadata": Metadata(
            version=OCSF_VERSION,
            product=Product(name="Test", vendor_name="Test", version="1.0"),
        ),
        "finding_info": FindingInformation(title="Test Finding", uid="test-123"),
        "severity_id": SeverityID.Informational,
        "time": int(datetime.now().timestamp()),
        "type_uid": DetectionFindingTypeID.Create,
    }
    defaults.update(kwargs)
    return DetectionFinding(**defaults)


class TestCloudProfile:
    """Tests for Cloud profile validation."""

    def test_cloud_profile_valid(self) -> None:
        """Cloud profile passes when cloud field is populated."""
        finding = _create_minimal_finding(
            cloud=Cloud(provider="aws", region="us-east-1"),
        )
        errors = validate_profiles(finding, profiles=["cloud"], raise_on_error=False)
        assert errors == []

    def test_cloud_profile_missing_cloud(self) -> None:
        """Cloud profile fails when cloud is None."""
        finding = _create_minimal_finding()
        errors = validate_profiles(finding, profiles=["cloud"], raise_on_error=False)
        assert len(errors) == 1
        assert errors[0].profile == "cloud"
        assert errors[0].field == "cloud"


class TestDateTimeProfile:
    """Tests for DateTime profile validation."""

    def test_datetime_profile_valid(self) -> None:
        """DateTime profile passes (no required fields)."""
        finding = _create_minimal_finding(time_dt=datetime.now())
        errors = validate_profiles(finding, profiles=["datetime"], raise_on_error=False)
        assert errors == []

    def test_datetime_profile_no_dt_fields(self) -> None:
        """DateTime profile still passes even without *_dt fields (they're optional)."""
        finding = _create_minimal_finding()
        errors = validate_profiles(finding, profiles=["datetime"], raise_on_error=False)
        assert errors == []


class TestNotImplementedProfiles:
    """Tests for profiles that are not yet implemented."""

    def test_security_control_not_implemented(self) -> None:
        """Security Control profile raises NotImplementedError."""
        finding = _create_minimal_finding()
        with pytest.raises(NotImplementedError, match="security_control"):
            validate_profiles(finding, profiles=["security_control"])

    def test_host_profile_not_implemented(self) -> None:
        """Host profile raises NotImplementedError."""
        finding = _create_minimal_finding()
        with pytest.raises(NotImplementedError, match="host"):
            validate_profiles(finding, profiles=["host"])

    def test_osint_profile_not_implemented(self) -> None:
        """OSINT profile raises NotImplementedError."""
        finding = _create_minimal_finding()
        with pytest.raises(NotImplementedError, match="osint"):
            validate_profiles(finding, profiles=["osint"])


class TestValidateProfiles:
    """Tests for the validate_profiles function."""

    def test_validate_profiles_reads_from_metadata(self) -> None:
        """Auto-detects profiles from metadata.profiles."""
        finding = _create_minimal_finding(
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(name="Test", vendor_name="Test", version="1.0"),
                profiles=["cloud"],
            ),
        )
        # Should fail because cloud is None
        errors = validate_profiles(finding, raise_on_error=False)
        assert len(errors) == 1
        assert errors[0].field == "cloud"

    def test_validate_profiles_explicit_override(self) -> None:
        """Explicit profiles param overrides metadata.profiles."""
        finding = _create_minimal_finding(
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(name="Test", vendor_name="Test", version="1.0"),
                profiles=["cloud"],  # Would fail
            ),
            cloud=Cloud(provider="aws"),
        )
        # Explicit datetime profile - should pass (no required fields)
        errors = validate_profiles(finding, profiles=["datetime"], raise_on_error=False)
        assert errors == []

    def test_validate_profiles_raise_on_error_true(self) -> None:
        """Raises ExceptionGroup (3.11+) or ProfileValidationError when raise_on_error=True."""
        finding = _create_minimal_finding()
        if _ExceptionGroup is not None:
            with pytest.raises(_ExceptionGroup) as exc_info:
                validate_profiles(finding, profiles=["cloud"])
            assert "Profile validation failed" in str(exc_info.value)
            assert len(exc_info.value.exceptions) == 1
        else:
            # Python < 3.11 fallback
            with pytest.raises(ProfileValidationError):
                validate_profiles(finding, profiles=["cloud"])

    def test_validate_profiles_raise_on_error_false(self) -> None:
        """Returns error list when raise_on_error=False."""
        finding = _create_minimal_finding()
        errors = validate_profiles(finding, profiles=["cloud"], raise_on_error=False)
        assert isinstance(errors, list)
        assert len(errors) == 1
        assert isinstance(errors[0], ProfileValidationError)

    def test_validate_profiles_cloud_and_datetime(self) -> None:
        """Validates cloud + datetime profiles together (current Prowler usage)."""
        finding = _create_minimal_finding(
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(name="Test", vendor_name="Test", version="1.0"),
                profiles=["cloud", "datetime"],
            ),
            cloud=Cloud(provider="aws", region="us-east-1"),
            time_dt=datetime.now(),
        )
        errors = validate_profiles(finding, raise_on_error=False)
        assert errors == []

    def test_validate_profiles_unknown_profile_ignored(self) -> None:
        """Unknown profile names are silently ignored (no requirements)."""
        finding = _create_minimal_finding()
        errors = validate_profiles(
            finding, profiles=["unknown_profile"], raise_on_error=False
        )
        assert errors == []


class TestOCSFProfileEnum:
    """Tests for the OCSFProfile enum."""

    def test_cloud_profile_value(self) -> None:
        """OCSFProfile.CLOUD has correct value."""
        assert OCSFProfile.CLOUD.value == "cloud"

    def test_datetime_profile_value(self) -> None:
        """OCSFProfile.DATETIME has correct value."""
        assert OCSFProfile.DATETIME.value == "datetime"

    def test_profile_enum_as_string(self) -> None:
        """OCSFProfile values work as strings in validate_profiles."""
        finding = _create_minimal_finding(cloud=Cloud(provider="aws"))
        errors = validate_profiles(
            finding, profiles=[OCSFProfile.CLOUD.value], raise_on_error=False
        )
        assert errors == []
