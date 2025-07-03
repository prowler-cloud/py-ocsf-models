from datetime import datetime

import requests

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.findings.activity_id import ActivityID
from py_ocsf_models.events.findings.application_security_posture_finding import (
    ApplicationSecurityPostureFinding,
    ApplicationSecurityPostureFindingTypeID,
)
from py_ocsf_models.events.findings.category_uid import CategoryUID
from py_ocsf_models.events.findings.class_uid import ClassUID
from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.objects.cve import CVE
from py_ocsf_models.objects.cvss import CVSSScore
from py_ocsf_models.objects.cwe import CWE
from py_ocsf_models.objects.epss import EPSS
from py_ocsf_models.objects.finding_info import FindingInformation
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.metric import Metric
from py_ocsf_models.objects.product import Feature, Product
from py_ocsf_models.objects.remediation import Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.url import URL
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails


class TestApplicationSecurityPostureFinding:
    def test_application_security_posture_finding(self) -> None:
        """
        Tests the creation and validation of an ApplicationSecurityPostureFinding OCSF event.
        This test populates an ApplicationSecurityPostureFinding object with
        sample data covering SAST, SCA, DAST, IaC, and Secret findings,
        and then validates it against the OCSF schema validator.
        """
        app_sec_finding = ApplicationSecurityPostureFinding(
            activity_id=ActivityID.Update.value,
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(
                    feature=Feature(
                        name="AppScan", uid="appscan-feat-1", version="1.0"
                    ),
                    lang="en",
                    name="Application Security Scanner",
                    path="Path/to/scanner",
                    cpe_name="cpe:/a:ibm:appscan:1.0",
                    url_string="https://www.ibm.com/appscan",
                    uid="appscan-prod-1",
                    vendor_name="IBM",
                    version="1.0",
                ),
            ),
            vulnerabilities=[
                VulnerabilityDetails(
                    cve=CVE(
                        uid="CVE-2021-44228",
                        desc="Apache Log4j2 JNDI Remote Code Execution",
                        cvss=CVSSScore(
                            base_score=10.0,
                            version="3.1",
                            vector_string="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
                            metrics=[Metric(name="privilegesRequired", value="NONE")],
                        ),
                        references=["https://nvd.nist.gov/vuln/detail/CVE-2021-44228"],
                        epss=EPSS(score="0.975620000", percentile="0.999980000"),
                    ),
                    cwe=CWE(
                        uid="CWE-079",
                        caption="Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
                        src_url=URL(
                            url_string="https://cwe.mitre.org/data/definitions/79.html"
                        ),
                    ),
                    desc="A critical vulnerability in Log4j2 allowing remote code execution.",
                    remediation=Remediation(
                        desc="Upgrade Log4j2 to version 2.17.1 or later.",
                    ),
                    severity=SeverityID.Critical.name,
                    title="vuln-log4shell-001",
                )
            ],
            resources=[
                ResourceDetails(
                    name="my-web-application",
                    namespace="prod",
                    uid="app-12345",
                    type="Application",
                    criticality="High",
                )
            ],
            finding_info=FindingInformation(
                title="Critical Application Security Posture Findings Detected",
                desc=(
                    "Multiple critical and high severity vulnerabilities detected across "
                    "SAST, SCA, DAST, IaC, and Secret scanning for the application."
                ),
                uid="app-sec-finding-001",
            ),
            severity_id=SeverityID.Critical.value,
            time=int(datetime.now().timestamp()),
            time_dt=datetime.now(),
            timezone_offset=0,
            type_uid=ApplicationSecurityPostureFindingTypeID.Create,
        )

        # Assertions to validate the populated object
        assert app_sec_finding.severity_id == SeverityID.Critical.value
        assert (
            app_sec_finding.class_uid
            == ClassUID.ApplicationSecurityPostureFinding.value
        )
        assert app_sec_finding.category_name == CategoryUID.Findings.name
        assert app_sec_finding.category_uid == CategoryUID.Findings.value
        assert app_sec_finding.activity_id == ActivityID.Update.value

        # Vulnerability assertions
        vulnerability = app_sec_finding.vulnerabilities[0]
        assert vulnerability.cve.uid == "CVE-2021-44228"
        assert vulnerability.cve.cvss.base_score == 10.0
        assert vulnerability.cve.cvss.version == "3.1"
        assert (
            vulnerability.cve.cvss.vector_string
            == "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H"
        )
        assert vulnerability.cve.cvss.metrics[0].name == "privilegesRequired"
        assert vulnerability.cve.cvss.metrics[0].value == "NONE"
        assert vulnerability.cve.references == [
            "https://nvd.nist.gov/vuln/detail/CVE-2021-44228"
        ]
        assert vulnerability.cve.epss.score == "0.975620000"
        assert vulnerability.cve.epss.percentile == 0.99998
        assert vulnerability.cwe.uid == "CWE-079"
        assert vulnerability.severity == SeverityID.Critical.name
        assert vulnerability.title == "vuln-log4shell-001"
        assert vulnerability.remediation

        # Finding Info assertions
        assert (
            app_sec_finding.finding_info.title
            == "Critical Application Security Posture Findings Detected"
        )

        assert app_sec_finding.finding_info.uid == "app-sec-finding-001"

        # Resources details
        resource = app_sec_finding.resources[0]
        assert resource.criticality == "High"
        assert resource.type == "Application"
        assert resource.name == "my-web-application"
        assert resource.namespace == "prod"
        assert resource.uid == "app-12345"

        # Convert to JSON and validate against OCSF schema
        app_sec_finding_json = app_sec_finding.json(exclude_unset=True)
        url = "https://schema.ocsf.io/api/v2/validate"
        headers = {"content-type": "application/json"}

        response = requests.post(url, headers=headers, data=app_sec_finding_json)
        assert response.status_code == 200, f"Schema validation failed: {response.text}"
        print("ApplicationSecurityPostureFinding schema validated successfully!")
