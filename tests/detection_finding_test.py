import uuid
from datetime import datetime

from py_ocsf_models import OCSF_VERSION
from py_ocsf_models.events.base_event import SeverityID
from py_ocsf_models.events.findings.detection_finding import (
    CategoryUID,
    DetectionFinding,
)
from py_ocsf_models.events.findings.detection_finding import (
    TypeID as DetectionFindingTypeID,
)
from py_ocsf_models.events.findings.finding import (
    ActivityID,
    ConfidenceID,
    FindingInformation,
)
from py_ocsf_models.objects.api import (
    API,
    Group,
    RequestElements,
    ResponseElements,
    Service,
)
from py_ocsf_models.objects.cloud import Account, Cloud, Organization
from py_ocsf_models.objects.container import Container, FingerPrint, Image
from py_ocsf_models.objects.dns_query import DNSOpcodeID, DNSQuery
from py_ocsf_models.objects.evidence_artifacts import EvidenceArtifacts
from py_ocsf_models.objects.fingerprint import AlgorithmID
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.operating_system import OperatingSystem, TypeID
from py_ocsf_models.objects.product import Feature, Product
from py_ocsf_models.objects.remediation import KBArticle, Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails

PROWLER_VERSION = "4.0.0"
PROWLER_PRODUCT = "Prowler"


class TestDetectionFinding:
    def test_detection_finding(self):
        pod_uuid = str(uuid.uuid4())
        detection_finding = DetectionFinding(
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
            ),
            finding_info=FindingInformation(
                title="Title",
                uid="123",
            ),
            severity_id=SeverityID.Informational,
            severity=SeverityID(1).name,
            activity_name="Activity Name",
            activity_id=1,
            comment="Comment",
            confidence="Confidence",
            confidence_id=1,
            confidence_score=123,
            end_time=datetime.now(),
            start_time=datetime.now(),
            resources=[
                ResourceDetails(
                    id="123",
                    name="Resource 1",
                    type="Resource",
                    details="Details of the resource",
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
                                algorithm="SHA256",
                                algorithm_id=3,
                                value="123",
                            ),
                            image=Image(
                                tag="Tag 1",
                                name="Image 1",
                                labels=["Label 1"],
                                path="Path 1",
                                uid="123",
                            ),
                            tag="Tag 1",
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
                                algorithm="SHA256",
                                algorithm_id=3,
                                value="123",
                            ),
                            image=Image(
                                tag="Tag 1",
                                name="Image 1",
                                labels=["Label 1"],
                                path="Path 1",
                                uid="123",
                            ),
                            tag="Tag 1",
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
                    name="Account 1", type="Account", type_id="3", uid="123"
                ),
                zone="Zone 1",
                org=Organization(
                    name="Organization 1", ou_id="123", ou_name="OU 1", uid="123"
                ),
                project_uid="123",
                provider="Provider 1",
                region="Region 1",
            ),
            container=Container(
                hash=FingerPrint(
                    algorithm="SHA256",
                    algorithm_id=3,
                    value="123",
                ),
                image=Image(
                    tag="Tag 1",
                    name="Image 1",
                    labels=["Label 1"],
                    path="Path 1",
                    uid="123",
                ),
                tag="Tag 1",
                name="Container 1",
                network_driver="Network Driver 1",
                orchestrator="Orchestrator 1",
                pod_uuid=pod_uuid,
                runtime="Runtime 1",
                size=123,
                uid="123",
            ),
            namespace_pid=123,
            count=123,
            duration=123,
            event_time=datetime.now(),
            evidences=[
                EvidenceArtifacts(
                    api=API(
                        request=RequestElements(
                            containers=[
                                Container(
                                    hash=FingerPrint(
                                        algorithm="SHA256",
                                        algorithm_id=3,
                                        value="123",
                                    ),
                                    image=Image(
                                        tag="Tag 1",
                                        name="Image 1",
                                        labels=["Label 1"],
                                        path="Path 1",
                                        uid="123",
                                    ),
                                    tag="Tag 1",
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
                                        algorithm="SHA256",
                                        algorithm_id=3,
                                        value="123",
                                    ),
                                    image=Image(
                                        tag="Tag 1",
                                        name="Image 1",
                                        labels=["Label 1"],
                                        path="Path 1",
                                        uid="123",
                                    ),
                                    tag="Tag 1",
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
            impact="Impact",
            impact_score=123,
            impact_id=1,
            remediation=Remediation(
                desc="Description",
                kb_article_list=[
                    KBArticle(
                        classification="Classification",
                        created_time=datetime.now(),
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
                            type="Type",
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
            risk_level="Risk Level",
            risk_level_id=1,
            risk_score=123,
            timezone_offset=123,
            type_uid=DetectionFindingTypeID.Create,
            type_name=DetectionFindingTypeID.Create.name,
            vulnerabilities=[
                VulnerabilityDetails(
                    desc="Description",
                    is_exploit_available=True,
                    first_seen_time=datetime.now(),
                    kb_article_list=[
                        KBArticle(
                            classification="Classification",
                            created_time=datetime.now(),
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
                                type="Type",
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
                    last_seen_time=datetime.now(),
                    references=["https://www.example.com"],
                    related_vulnerabilities=["123"],
                    remediation=Remediation(
                        desc="Description",
                        kb_article_list=[
                            KBArticle(
                                classification="Classification",
                                created_time=datetime.now(),
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
                                    type="Type",
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
        assert detection_finding.activity_name == "Activity Name"
        assert detection_finding.activity_id == ActivityID.Create
        assert detection_finding.comment == "Comment"
        assert detection_finding.confidence == "Confidence"
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

        # Assert ContainerProfile and nested objects
        container = detection_finding.container
        assert str(container.pod_uuid) == pod_uuid
        assert container.network_driver == "Network Driver 1"
        assert container.orchestrator == "Orchestrator 1"
        assert container.size == 123

        # Assert Image and FingerPrint
        image = container.image
        assert image.tag == "Tag 1"
        assert image.name == "Image 1"
        assert "Label 1" in image.labels
        assert image.path == "Path 1"
        assert image.uid == "123"

        fingerprint = container.hash
        assert fingerprint.algorithm == "SHA256"
        assert fingerprint.algorithm_id == AlgorithmID.SHA_256
        assert fingerprint.value == "123"

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
        assert "https://www.example.com" in remediation.references

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
        assert "https://www.example.com" in vulnerability.references
        assert vulnerability.severity == "Severity"
        assert vulnerability.title == "Title"
        assert vulnerability.vendor_name == "Vendor Name"

        # Assert OperatingSystem in KBArticle
        os = kb_article.os
        assert os.cpu_bits == 64
        assert os.country == "US"
        assert os.lang == "en"
        assert os.name == "Name"
        assert os.build == "Build"
        assert os.edition == "Edition"
        assert os.sp_name == "SP Name"
        assert os.sp_ver == 123
        assert os.cpe_name == "CPE Name"
        assert os.type == "Type"
        assert os.type_id == TypeID.Windows
        assert os.version == "Version"

        # Assert EvidenceArtifacts
        evidence_artifact = detection_finding.evidences[0]
        assert evidence_artifact.api.operation == "GET"
        assert evidence_artifact.api.version == "1.0"
        assert evidence_artifact.data == {"key": "value"}

        # Assert Type
        assert detection_finding.type_uid == DetectionFindingTypeID.Create
        assert detection_finding.type_name == "Create"
