import uuid
from datetime import datetime

import pytest
import requests

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.findings.activity_id import ActivityID
from py_ocsf_models.events.findings.category_uid import CategoryUID
from py_ocsf_models.events.findings.confidence_id import ConfidenceID
from py_ocsf_models.events.findings.detection_finding import DetectionFinding
from py_ocsf_models.events.findings.detection_finding_type_id import (
    DetectionFindingTypeID,
)
from py_ocsf_models.events.findings.finding import FindingInformation
from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.events.findings.status_id import StatusID
from py_ocsf_models.objects.api import (
    API,
    Group,
    RequestElements,
    ResponseElements,
    Service,
)
from py_ocsf_models.objects.cloud import Account, Cloud, Organization
from py_ocsf_models.objects.container import Container, FingerPrint, Image
from py_ocsf_models.objects.cve import CVE
from py_ocsf_models.objects.dns_query import DNSOpcodeID, DNSQuery
from py_ocsf_models.objects.evidence_artifacts import EvidenceArtifacts
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.operating_system import OperatingSystem, TypeID
from py_ocsf_models.objects.product import Feature, Product
from py_ocsf_models.objects.remediation import KBArticle, Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails

PROWLER_VERSION = "4.1.0"
PROWLER_PRODUCT = "Prowler"


class TestDetectionFinding:
    @pytest.mark.external_api
    def test_detection_finding(self):
        pod_uuid = str(uuid.uuid4())
        detection_finding = DetectionFinding(
            status=StatusID.New.name,
            status_id=StatusID.New.value,
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(
                    feature=Feature(
                        name=PROWLER_PRODUCT, uid="123", version=PROWLER_VERSION
                    ),
                    lang="en",
                    name=PROWLER_PRODUCT,
                    path="Path",
                    cpe_name="CPE Name",
                    url_string="https://www.example.com",
                    uid="123",
                    vendor_name=PROWLER_PRODUCT,
                    version=PROWLER_VERSION,
                ),
                profiles=["cloud", "datetime"],
            ),
            finding_info=FindingInformation(
                title="Title",
                uid="123",
                created_time=int(datetime.now().timestamp()),
                created_time_dt=datetime.now(),
            ),
            severity_id=SeverityID.Informational,
            severity=SeverityID(1).name,
            activity_name="Create",
            activity_id=1,
            comment="Comment",
            confidence="Low",
            confidence_id=1,
            confidence_score=123,
            end_time=int(datetime.now().timestamp()),
            end_time_dt=datetime.now(),
            start_time=int(datetime.now().timestamp()),
            start_time_dt=datetime.now(),
            resources=[
                ResourceDetails(
                    id="123",
                    name="Resource 1",
                    type="Resource",
                    details="Details of the resource",
                    cloud_partition="aws",
                )
            ],
            category_name=CategoryUID.Findings.name,
            category_uid=CategoryUID.Findings.value,
            class_name="Detection Finding",
            class_uid=2004,
            api=API(
                request=RequestElements(
                    containers=[
                        Container(
                            hash=FingerPrint(
                                algorithm="SHA-256",
                                algorithm_id=3,
                                value="123",
                            ),
                            image=Image(
                                name="Image 1",
                                labels=["Label 1"],
                                path="Path 1",
                                uid="123",
                            ),
                            name="Container 1",
                            network_driver="Network Driver 1",
                            orchestrator="Orchestrator 1",
                            pod_uuid=pod_uuid,
                            runtime="Runtime 1",
                            size=123,
                            uid="123",
                        )
                    ],
                    data={"key": "value"},
                    flags=["Flag 1"],
                    uid="123",
                ),
                response=ResponseElements(
                    containers=[
                        Container(
                            hash=FingerPrint(
                                algorithm="SHA-256",
                                algorithm_id=3,
                                value="123",
                            ),
                            image=Image(
                                name="Image 1",
                                labels=["Label 1"],
                                path="Path 1",
                                uid="123",
                            ),
                            name="Container 1",
                            network_driver="Network Driver 1",
                            orchestrator="Orchestrator 1",
                            pod_uuid=pod_uuid,
                            runtime="Runtime 1",
                            size=123,
                            uid="123",
                        )
                    ],
                    data={"key": "value"},
                    error="Error",
                    error_message="Error Message",
                    flags=["Flag 1"],
                    message="Message",
                    code=123,
                ),
                group=Group(
                    type="Group",
                    desc="Details of the group",
                    domain="Domain 1",
                    name="Group 1",
                    privileges=["Privilege 1"],
                    uid="123",
                ),
                operation="GET",
                service=Service(
                    labels=["Label 1"],
                    name="Service 1",
                    uid="123",
                    version="1.0",
                ),
                version="1.0",
            ),
            cloud=Cloud(
                account=Account(
                    name="Account 1",
                    type="AWS IAM User",
                    type_id="3",
                    uid="123",
                    labels=["label 1"],
                ),
                zone="Zone 1",
                org=Organization(
                    name="Organization 1", ou_uid="123", ou_name="OU 1", uid="123"
                ),
                provider="Provider 1",
                region="Region 1",
            ),
            container=Container(
                hash=FingerPrint(
                    algorithm="SHA-256",
                    algorithm_id=3,
                    value="123",
                ),
                image=Image(
                    name="Image 1",
                    labels=["Label 1"],
                    path="Path 1",
                    uid="123",
                ),
                name="Container 1",
                network_driver="Network Driver 1",
                orchestrator="Orchestrator 1",
                pod_uuid=pod_uuid,
                runtime="Runtime 1",
                size=123,
                uid="123",
            ),
            count=123,
            duration=123,
            time=int(datetime.now().timestamp()),
            time_dt=datetime.now(),
            evidences=[
                EvidenceArtifacts(
                    api=API(
                        request=RequestElements(
                            containers=[
                                Container(
                                    hash=FingerPrint(
                                        algorithm="SHA-256",
                                        algorithm_id=3,
                                        value="123",
                                    ),
                                    image=Image(
                                        name="Image 1",
                                        labels=["Label 1"],
                                        path="Path 1",
                                        uid="123",
                                    ),
                                    name="Container 1",
                                    network_driver="Network Driver 1",
                                    orchestrator="Orchestrator 1",
                                    pod_uuid=pod_uuid,
                                    runtime="Runtime 1",
                                    size=123,
                                    uid="123",
                                )
                            ],
                            data={"key": "value"},
                            flags=["Flag 1"],
                            uid="123",
                        ),
                        response=ResponseElements(
                            containers=[
                                Container(
                                    hash=FingerPrint(
                                        algorithm="SHA-256",
                                        algorithm_id=3,
                                        value="123",
                                    ),
                                    image=Image(
                                        name="Image 1",
                                        labels=["Label 1"],
                                        path="Path 1",
                                        uid="123",
                                    ),
                                    name="Container 1",
                                    network_driver="Network Driver 1",
                                    orchestrator="Orchestrator 1",
                                    pod_uuid=pod_uuid,
                                    runtime="Runtime 1",
                                    size=123,
                                    uid="123",
                                )
                            ],
                            data={"key": "value"},
                            error="Error",
                            error_message="Error Message",
                            flags=["Flag 1"],
                            message="Message",
                            code=123,
                        ),
                        group=Group(
                            type="Group",
                            desc="Details of the group",
                            domain="Domain 1",
                            name="Group 1",
                            privileges=["Privilege 1"],
                            uid="123",
                        ),
                        operation="GET",
                        service=Service(
                            labels=["Label 1"],
                            name="Service 1",
                            uid="123",
                            version="1.0",
                        ),
                        version="1.0",
                    ),
                    query=DNSQuery(
                        opcode="Query",
                        opcode_id=DNSOpcodeID.Query,
                        hostname="www.example.com",
                        packet_uid=123,
                        class_="IN",
                        type="A",
                    ),
                    data={"key": "value"},
                )
            ],
            impact="Low",
            impact_score=75,
            impact_id=1,
            remediation=Remediation(
                desc="Description",
                kb_article_list=[
                    KBArticle(
                        classification="Classification",
                        created_time=int(datetime.now().timestamp()),
                        os=OperatingSystem(
                            cpu_bits=64,
                            country="US",
                            lang="en",
                            name="Name",
                            build="Build",
                            edition="Edition",
                            sp_name="SP Name",
                            sp_ver=123,
                            cpe_name="CPE Name",
                            type="Windows",
                            type_id=100,
                            version="Version",
                        ),
                        bulletin="Bulletin",
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
                        severity="Severity",
                        size=123,
                        src_url="https://www.example.com",
                        is_superseded=True,
                        title="Title",
                        uid="123",
                    )
                ],
                references=["https://www.example.com"],
            ),
            risk_level="Low",
            risk_level_id=1,
            risk_score=75,
            risk_details="Risk Details",
            timezone_offset=123,
            type_uid=DetectionFindingTypeID.Create,
            type_name=f"Detection Finding: {DetectionFindingTypeID.Create.name}",
            vulnerabilities=[
                VulnerabilityDetails(
                    desc="Description",
                    cve=CVE(
                        uid="CVE-2021-1234",
                    ),
                    is_exploit_available=True,
                    first_seen_time=int(datetime.now().timestamp()),
                    first_seen_time_dt=datetime.now(),
                    last_seen_time=int(datetime.now().timestamp()),
                    last_seen_time_dt=datetime.now(),
                    references=["https://www.example.com"],
                    related_vulnerabilities=["123"],
                    remediation=Remediation(
                        desc="Description",
                        kb_article_list=[
                            KBArticle(
                                classification="Classification",
                                created_time=int(datetime.now().timestamp()),
                                created_time_dt=datetime.now(),
                                os=OperatingSystem(
                                    cpu_bits=64,
                                    country="US",
                                    lang="en",
                                    name="Name",
                                    build="Build",
                                    edition="Edition",
                                    sp_name="SP Name",
                                    sp_ver=123,
                                    cpe_name="CPE Name",
                                    type="Windows",
                                    type_id=100,
                                    version="Version",
                                ),
                                bulletin="Bulletin",
                                product=Product(
                                    feature=Feature(
                                        name="Name", uid="123", version="Version"
                                    ),
                                    lang="en",
                                    name="Name",
                                    path="Path",
                                    cpe_name="CPE Name",
                                    url_string="https://www.example.com",
                                    uid="123",
                                    vendor_name="Vendor Name",
                                    version="Version",
                                ),
                                severity="Severity",
                                size=123,
                                src_url="https://www.example.com",
                                is_superseded=True,
                                title="Title",
                                uid="123",
                            )
                        ],
                        references=["https://www.example.com"],
                    ),
                    severity="Severity",
                    title="Title",
                    vendor_name="Vendor Name",
                )
            ],
        )

        # Assert Severity
        assert detection_finding.severity == "Informational"
        assert detection_finding.severity_id == SeverityID.Informational

        # Assert Metadata and Product
        assert detection_finding.metadata.version == OCSF_VERSION
        product = detection_finding.metadata.product
        assert product.feature.name == PROWLER_PRODUCT
        assert product.feature.uid == "123"
        assert product.feature.version == PROWLER_VERSION
        assert product.lang == "en"
        assert product.name == PROWLER_PRODUCT
        assert product.path == "Path"
        assert product.cpe_name == "CPE Name"
        assert product.url_string == "https://www.example.com"
        assert product.uid == "123"
        assert product.vendor_name == PROWLER_PRODUCT
        assert product.version == PROWLER_VERSION

        # Assert FindingInformation
        assert detection_finding.finding_info.title == "Title"
        assert detection_finding.finding_info.uid == "123"

        # Assert simple attributes
        assert detection_finding.severity_id == SeverityID.Informational
        assert detection_finding.activity_name == "Create"
        assert detection_finding.activity_id == ActivityID.Create
        assert detection_finding.comment == "Comment"
        assert detection_finding.confidence == "Low"
        assert detection_finding.confidence_id == ConfidenceID.Low
        assert detection_finding.confidence_score == 123

        # Assert ResourceDetails
        resource = detection_finding.resources[0]
        assert resource.name == "Resource 1"
        assert resource.type == "Resource"

        # Assert Cloud profile and nested objects
        assert detection_finding.api.operation == "GET"
        assert detection_finding.api.version == "1.0"
        assert detection_finding.api.service.name == "Service 1"

        assert detection_finding.cloud.account.name == "Account 1"
        assert detection_finding.cloud.zone == "Zone 1"
        assert detection_finding.cloud.org.name == "Organization 1"
        assert detection_finding.cloud.provider == "Provider 1"
        assert detection_finding.cloud.region == "Region 1"
        assert detection_finding.cloud.account.labels == ["label 1"]

        # Assert DNSQuery
        dns_query = detection_finding.evidences[0].query
        assert dns_query.opcode == "Query"
        assert dns_query.opcode_id == DNSOpcodeID.Query
        assert dns_query.hostname == "www.example.com"
        assert dns_query.packet_uid == 123
        assert dns_query.type == "A"

        # Assert Remediation and KBArticle
        remediation = detection_finding.remediation
        assert remediation.desc == "Description"
        assert len(remediation.references) == 1
        assert remediation.references[0] == "https://www.example.com"

        kb_article = remediation.kb_article_list[0]
        assert kb_article.classification == "Classification"
        assert kb_article.bulletin == "Bulletin"
        assert kb_article.severity == "Severity"
        assert kb_article.size == 123
        assert kb_article.src_url == "https://www.example.com"
        assert kb_article.is_superseded is True
        assert kb_article.title == "Title"
        assert kb_article.uid == "123"

        # Assert VulnerabilityDetails
        vulnerability = detection_finding.vulnerabilities[0]
        assert vulnerability.desc == "Description"
        assert vulnerability.is_exploit_available is True
        assert len(vulnerability.references) == 1
        assert vulnerability.references[0] == "https://www.example.com"
        assert vulnerability.severity == "Severity"
        assert vulnerability.title == "Title"
        assert vulnerability.vendor_name == "Vendor Name"

        # Assert OperatingSystem in KBArticle
        operating_system = kb_article.os
        assert operating_system.cpu_bits == 64
        assert operating_system.country == "US"
        assert operating_system.lang == "en"
        assert operating_system.name == "Name"
        assert operating_system.build == "Build"
        assert operating_system.edition == "Edition"
        assert operating_system.sp_name == "SP Name"
        assert operating_system.sp_ver == 123
        assert operating_system.cpe_name == "CPE Name"
        assert operating_system.type == TypeID.Windows.name
        assert operating_system.type_id == TypeID.Windows
        assert operating_system.version == "Version"

        # Assert EvidenceArtifacts
        evidence_artifact = detection_finding.evidences[0]
        assert evidence_artifact.api.operation == "GET"
        assert evidence_artifact.api.version == "1.0"
        assert evidence_artifact.data == {"key": "value"}

        # Assert Type
        assert detection_finding.type_uid == DetectionFindingTypeID.Create
        assert detection_finding.type_name == "Detection Finding: Create"

        detection_finding_json = detection_finding.model_dump_json(exclude_unset=True)

        self._validate_against_ocsf_schema(detection_finding_json)

    @staticmethod
    def _validate_against_ocsf_schema(json_data: str) -> None:
        """Validate JSON against OCSF schema API."""
        url = "https://schema.ocsf.io/api/v2/validate"
        headers = {"content-type": "application/json"}

        response = requests.post(url, headers=headers, data=json_data)
        assert response.status_code == 200, f"Schema validation failed: {response.text}"
        assert response.json()["error_count"] == 0


class TestDetectionFindingMinimal:
    """Tests for minimal DetectionFinding with only required fields."""

    def test_detection_finding_minimal(self) -> None:
        """Test with only required fields - validates schema requirements."""
        from py_ocsf_models.events.findings.finding import FindingInformation

        finding = DetectionFinding(
            activity_id=ActivityID.Create,
            metadata=Metadata(
                version=OCSF_VERSION,
                product=Product(
                    name="Test Product",
                    vendor_name="Test Vendor",
                    version="1.0",
                ),
            ),
            finding_info=FindingInformation(title="Test Finding", uid="test-123"),
            severity_id=SeverityID.Informational,
            time=int(datetime.now().timestamp()),
            type_uid=DetectionFindingTypeID.Create,
        )

        # Verify optional fields are None
        assert finding.cloud is None
        assert finding.action_id is None
        assert finding.disposition_id is None
        assert finding.actor is None
        assert finding.malware is None

        # Verify required fields are set
        assert finding.activity_id == ActivityID.Create
        assert finding.severity_id == SeverityID.Informational
        assert finding.metadata is not None
        assert finding.finding_info is not None


class TestDetectionFindingValidation:
    """Tests for field validation constraints."""

    def _create_base_finding(self, **kwargs) -> DetectionFinding:
        """Create a base finding for testing."""
        from py_ocsf_models.events.findings.finding import FindingInformation

        defaults = {
            "activity_id": ActivityID.Create,
            "metadata": Metadata(
                version=OCSF_VERSION,
                product=Product(name="Test", vendor_name="Test", version="1.0"),
            ),
            "finding_info": FindingInformation(title="Test", uid="test-123"),
            "severity_id": SeverityID.Informational,
            "time": int(datetime.now().timestamp()),
            "type_uid": DetectionFindingTypeID.Create,
        }
        defaults.update(kwargs)
        return DetectionFinding(**defaults)

    def test_impact_score_rejects_over_100(self) -> None:
        """impact_score must be <= 100."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            self._create_base_finding(impact_score=150)

    def test_impact_score_rejects_negative(self) -> None:
        """impact_score must be >= 0."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            self._create_base_finding(impact_score=-1)

    def test_impact_score_accepts_boundary(self) -> None:
        """impact_score accepts 0 and 100."""
        finding_zero = self._create_base_finding(impact_score=0)
        assert finding_zero.impact_score == 0

        finding_hundred = self._create_base_finding(impact_score=100)
        assert finding_hundred.impact_score == 100

    def test_risk_score_rejects_invalid(self) -> None:
        """risk_score must be 0-100."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            self._create_base_finding(risk_score=101)

    def test_timezone_offset_rejects_out_of_range(self) -> None:
        """timezone_offset must be -1080 to 1080."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            self._create_base_finding(timezone_offset=1081)

        with pytest.raises(ValidationError):
            self._create_base_finding(timezone_offset=-1081)

    def test_timezone_offset_accepts_boundary(self) -> None:
        """timezone_offset accepts -1080 and 1080."""
        finding_min = self._create_base_finding(timezone_offset=-1080)
        assert finding_min.timezone_offset == -1080

        finding_max = self._create_base_finding(timezone_offset=1080)
        assert finding_max.timezone_offset == 1080

    def test_raw_data_size_rejects_negative(self) -> None:
        """raw_data_size must be >= 0."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            self._create_base_finding(raw_data_size=-1)

    def test_raw_data_size_accepts_zero(self) -> None:
        """raw_data_size accepts 0."""
        finding = self._create_base_finding(raw_data_size=0)
        assert finding.raw_data_size == 0


class TestDetectionFindingNewFields:
    """Tests for new OCSF 1.7.0 fields."""

    def _create_base_finding(self, **kwargs) -> DetectionFinding:
        """Create a base finding for testing."""
        from py_ocsf_models.events.findings.finding import FindingInformation

        defaults = {
            "activity_id": ActivityID.Create,
            "metadata": Metadata(
                version=OCSF_VERSION,
                product=Product(name="Test", vendor_name="Test", version="1.0"),
            ),
            "finding_info": FindingInformation(title="Test", uid="test-123"),
            "severity_id": SeverityID.Informational,
            "time": int(datetime.now().timestamp()),
            "type_uid": DetectionFindingTypeID.Create,
        }
        defaults.update(kwargs)
        return DetectionFinding(**defaults)

    def test_detection_finding_with_action_fields(self) -> None:
        """Test action_id and action fields."""
        from py_ocsf_models.events.findings.action_id import ActionID

        finding = self._create_base_finding(
            action_id=ActionID.Denied,
            action="Denied",
        )
        assert finding.action_id == ActionID.Denied
        assert finding.action == "Denied"

    def test_detection_finding_with_disposition_fields(self) -> None:
        """Test disposition_id and disposition fields."""
        from py_ocsf_models.events.findings.disposition_id import DispositionID

        finding = self._create_base_finding(
            disposition_id=DispositionID.Blocked,
            disposition="Blocked",
        )
        assert finding.disposition_id == DispositionID.Blocked
        assert finding.disposition == "Blocked"

    def test_detection_finding_with_verdict_fields(self) -> None:
        """Test verdict_id and verdict fields."""
        from py_ocsf_models.objects.verdict import VerdictID

        finding = self._create_base_finding(
            verdict_id=VerdictID.TruePositive,
            verdict="True Positive",
        )
        assert finding.verdict_id == VerdictID.TruePositive
        assert finding.verdict == "True Positive"

    def test_detection_finding_with_priority_fields(self) -> None:
        """Test priority_id and priority fields."""
        from py_ocsf_models.events.findings.priority_id import PriorityID

        finding = self._create_base_finding(
            priority_id=PriorityID.Critical,
            priority="Critical",
        )
        assert finding.priority_id == PriorityID.Critical
        assert finding.priority == "Critical"

    def test_detection_finding_with_is_alert(self) -> None:
        """Test is_alert boolean field."""
        finding = self._create_base_finding(is_alert=True)
        assert finding.is_alert is True

    def test_detection_finding_with_is_suspected_breach(self) -> None:
        """Test is_suspected_breach boolean field."""
        finding = self._create_base_finding(is_suspected_breach=True)
        assert finding.is_suspected_breach is True

    def test_detection_finding_with_src_url(self) -> None:
        """Test src_url field."""
        finding = self._create_base_finding(src_url="https://example.com/finding/123")
        assert finding.src_url == "https://example.com/finding/123"

    def test_detection_finding_with_actor(self) -> None:
        """Test actor field."""
        from py_ocsf_models.objects.actor import Actor

        actor = Actor(app_name="SecurityScanner", app_uid="scanner-001")
        finding = self._create_base_finding(actor=actor)
        assert finding.actor is not None
        assert finding.actor.app_name == "SecurityScanner"

    def test_detection_finding_with_malware(self) -> None:
        """Test malware field."""
        from py_ocsf_models.objects.malware import Malware, MalwareClassificationID

        malware = Malware(
            classification_ids=[MalwareClassificationID.Ransomware],
            name="TestMalware",
        )
        finding = self._create_base_finding(malware=[malware])
        assert len(finding.malware) == 1
        assert finding.malware[0].name == "TestMalware"

    def test_detection_finding_with_tickets(self) -> None:
        """Test tickets field."""
        from py_ocsf_models.objects.ticket import Ticket

        ticket = Ticket(uid="JIRA-123", title="Security Alert")
        finding = self._create_base_finding(tickets=[ticket])
        assert len(finding.tickets) == 1
        assert finding.tickets[0].uid == "JIRA-123"

    def test_detection_finding_with_firewall_rule(self) -> None:
        """Test firewall_rule field."""
        from py_ocsf_models.objects.firewall_rule import FirewallRule

        rule = FirewallRule(name="Block SSH", uid="rule-001")
        finding = self._create_base_finding(firewall_rule=rule)
        assert finding.firewall_rule is not None
        assert finding.firewall_rule.name == "Block SSH"

    def test_detection_finding_with_authorizations(self) -> None:
        """Test authorizations field."""
        from py_ocsf_models.objects.authorization import AuthorizationResult

        auth = AuthorizationResult(decision="denied")
        finding = self._create_base_finding(authorizations=[auth])
        assert len(finding.authorizations) == 1
        assert finding.authorizations[0].decision == "denied"
