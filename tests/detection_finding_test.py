from datetime import datetime

from py_ocsf_models.events.findings.detection_finding import DetectionFinding
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
from py_ocsf_models.objects.operating_system import OperatingSystem
from py_ocsf_models.objects.product import Product
from py_ocsf_models.objects.remediation import KBArticle, Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails
from py_ocsf_models.profiles.cloud import CloudProfile
from py_ocsf_models.profiles.container import ContainerProfile


class Test_DetectionFinding:
    def test_detection_finding(self):
        d = DetectionFinding(
            resources=[
                ResourceDetails(
                    id="123",
                    name="Resource 1",
                    type="Resource",
                    details="Details of the resource",
                )
            ],
            category_name="Findings",
            category_uid=2,
            class_name="Detection Finding",
            class_uid=2004,
            cloud=CloudProfile(
                api=API(
                    request=RequestElements(
                        headers={"Content-Type": "application/json"}, body="{}"
                    ),
                    response=ResponseElements(
                        headers={"Content-Type": "application/json"}, body="{}"
                    ),
                    group=Group(
                        id="123",
                        name="Group 1",
                        type="Group",
                        details="Details of the group",
                    ),
                    operation="GET",
                    service=Service(
                        name="Service 1",
                        type="Service",
                        details="Details of the service",
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
                container=ContainerProfile(
                    container=Container(
                        hash=FingerPrint(algorithm="SHA256", value="123"),
                        image=Image(
                            name="Image 1", type="Image", details="Details of the image"
                        ),
                        tag="Tag 1",
                        name="Container 1",
                        network_driver="Network Driver 1",
                        orchestrator="Orchestrator 1",
                        pod_uuid="123",
                        runtime="Runtime 1",
                        size=123,
                        uid="123",
                    ),
                    namespace_pid=123,
                ),
            ),
            count=123,
            duration=123,
            event_time=datetime.now(),
            evidences=[
                EvidenceArtifacts(
                    api=API(
                        request=RequestElements(
                            headers={"Content-Type": "application/json"}, body="{}"
                        ),
                        response=ResponseElements(
                            headers={"Content-Type": "application/json"}, body="{}"
                        ),
                        group=Group(
                            id="123",
                            name="Group 1",
                            type="Group",
                            details="Details of the group",
                        ),
                        operation="GET",
                        service=Service(
                            name="Service 1",
                            type="Service",
                            details="Details of the service",
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
            impact_id=123,
            remediation=Remediation(
                desc="Description",
                kb_article_list=[
                    KBArticle(
                        classification="Classification",
                        created_time=datetime.now(),
                        os=OperatingSystem(
                            family="Family",
                            name="Name",
                            platform="Platform",
                            version="Version",
                        ),
                        bulletin="Bulletin",
                        product=Product(name="Name", type="Type", details="Details"),
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
            risk_level_id=123,
            risk_score=123,
            timezone_offset=123,
            type_id=123,
            type_name="Type Name",
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
                                family="Family",
                                name="Name",
                                platform="Platform",
                                version="Version",
                            ),
                            bulletin="Bulletin",
                            product=Product(
                                name="Name", type="Type", details="Details"
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
                                    family="Family",
                                    name="Name",
                                    platform="Platform",
                                    version="Version",
                                ),
                                bulletin="Bulletin",
                                product=Product(
                                    name="Name", type="Type", details="Details"
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

        print(d)
        assert d is not None
