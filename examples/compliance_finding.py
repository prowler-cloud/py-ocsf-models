#!/usr/bin/env python3

# The following is an example demonstrating how to create an
# OCSF Compliance Finding using py-ocsf-models.
# This example showcases the instantiation of various models and
# their association to create a rich, structured representation of
# a compliance finding.

# Run me from the project root directory with:
#   `poetry run examples/compliance_finding.py | jq`

from datetime import datetime

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.base_event import SeverityID
from py_ocsf_models.events.findings.compliance_finding import (
    ComplianceFinding,
    ComplianceFindingTypeID,
)
from py_ocsf_models.events.findings.finding import ActivityID, CategoryUID, ClassUID
from py_ocsf_models.objects.assessment import Assessment
from py_ocsf_models.objects.check import Check
from py_ocsf_models.objects.compliance import Compliance
from py_ocsf_models.objects.compliance_status import StatusID as ComplianceStatusID
from py_ocsf_models.objects.evidence_artifacts import EvidenceArtifacts
from py_ocsf_models.objects.finding_info import FindingInformation
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.product import Feature, Product
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.url import URL
from py_ocsf_models.objects.verdict import VerdictID

compliance_finding = ComplianceFinding(
    activity_id=ActivityID.Create.value,
    category_uid=CategoryUID.Findings.value,
    class_uid=ClassUID.ComplianceFinding.value,
    metadata=Metadata(
        version=OCSF_VERSION,
        product=Product(
            feature=Feature(name="Name", uid="123", version="Version"),
            lang="en",
            name="Name",
            path="Path",
            cpe_name="CPE Name",
            url_string="https://www.example.com",
            uid="123",
            vendor_name="Vendor Name",
            version="Version",
        ),
    ),
    compliance=Compliance(
        assessments=[
            Assessment(
                category="Access Control",
                name="github authn configuration",
                desc=(
                    "This assessment checks that the repository being "
                    "assessed is hosted on GitHub"
                ),
                uid="123",
                meets_criteria=True,
            )
        ],
        category="Supply Chain Risk Assessment",
        checks=[
            Check(
                name=(
                    "OSPS-AC-01.01: When a user attempts to access a sensitive "
                    "resource in the project's version control system, the "
                    "system MUST require the user to complete a multi-factor "
                    "authentication process."
                ),
                uid="OSPS-AC-01.01",
                version="2025-02-25",
                severity_id=SeverityID.Critical.value,
                standards=["Open Source Project Security Baseline v2025-02-25"],
                status="Pass",
                status_id=ComplianceStatusID.Pass.value,
            )
        ],
        control="OSPS-AC-01",
        desc=(
            "Enforce multi-factor authentication for the project's "
            "version control system, requiring collaborators to provide "
            "a second form of authentication when accessing sensitive "
            "data or modifying repository settings. Passkeys are "
            "acceptable for this control."
        ),
        requirements=["https://baseline.openssf.org/versions/2025-02-25#osps-ac-0101"],
        standards=["Open Source Project Security Baseline v2025-02-25"],
        status_id=ComplianceStatusID.Pass.value,
    ),
    evidences=[
        EvidenceArtifacts(
            name="GitHub required and default configuration",
            resources=[
                ResourceDetails(
                    name="security-baseline",
                    namespace="ossf",
                    uid="https://github.com/ossf/security-baseline",
                    type="GitHub",
                    criticality="Critical",
                    hostname="https://github.com/ossf/security-baseline",
                )
            ],
            url=URL(
                url_string="https://github.com/ossf/security-baseline",
            ),
            verdict_id=VerdictID.Benign.value,
        )
    ],
    finding_info=FindingInformation(
        title=(
            "Repository is hosted on GitHub and subject to required and "
            "default configured MFA authentication"
        ),
        desc=(
            "The repository is verified as hosted on GitHub and adheres "
            "to GitHub's authentication policies for MFA. See "
            "https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication"
        ),
        uid="123",
    ),
    severity_id=SeverityID.Critical.value,
    time=int(datetime.now().timestamp()),
    timezone_offset=0,
    type_uid=ComplianceFindingTypeID.Create,
)

# Serialize to JSON
compliance_finding_json = compliance_finding.json(exclude_unset=True)
print(compliance_finding_json)
