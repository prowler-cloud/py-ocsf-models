from datetime import datetime

import requests

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.findings.activity_id import ActivityID
from py_ocsf_models.events.findings.category_uid import CategoryUID
from py_ocsf_models.events.findings.class_uid import ClassUID
from py_ocsf_models.events.findings.compliance_finding import (
    ComplianceFinding,
    ComplianceFindingTypeID,
)
from py_ocsf_models.events.findings.severity_id import SeverityID
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


class TestComplianceFinding:
    def test_compliance_finding(self):
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
                profiles=["datetime"],
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
                requirements=[
                    "https://baseline.openssf.org/versions/2025-02-25#osps-ac-0101"
                ],
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
            time_dt=datetime.now(),
            timezone_offset=0,
            type_uid=ComplianceFindingTypeID.Create,
        )

        assert compliance_finding.severity_id == SeverityID.Critical.value

        assert compliance_finding.compliance.checks[0].uid == "OSPS-AC-01.01"
        assert compliance_finding.compliance.checks[0].standards == [
            "Open Source Project Security Baseline v2025-02-25"
        ]

        check = compliance_finding.compliance.checks[0]
        assert check.status == "Pass"
        assert check.status_id == ComplianceStatusID.Pass.value

        evidence = compliance_finding.evidences[0]
        assert evidence.name == "GitHub required and default configuration"
        assert evidence.resources[0].name == "security-baseline"

        title = compliance_finding.finding_info.title
        expected_title = (
            "Repository is hosted on GitHub and subject to required and "
            "default configured MFA authentication"
        )
        assert title == expected_title
        desc = compliance_finding.finding_info.desc
        expected_desc = (
            "The repository is verified as hosted on GitHub and adheres "
            "to GitHub's authentication policies for MFA. See "
            "https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication"
        )
        assert desc == expected_desc
        uid = compliance_finding.finding_info.uid
        assert uid == "123"

        compliance_finding_json = compliance_finding.json(exclude_unset=True)
        url = "https://schema.ocsf.io/api/v2/validate"
        headers = {"content-type": "application/json"}

        response = requests.post(url, headers=headers, data=compliance_finding_json)
        assert response.status_code == 200, f"Schema validation failed: {response.text}"
        assert response.json()["error_count"] == 0
