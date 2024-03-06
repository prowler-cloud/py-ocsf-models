# py-ocsf-models

The `py-ocsf-models` package offers a Python implementation of the Open Cybersecurity Schema Framework (OCSF) models, facilitating the manipulation and understanding of cybersecurity data within Python applications. This package provides a rich set of models covering various aspects of cybersecurity events, findings, objects, and profiles as defined by the OCSF Schema, enabling developers to work with structured cybersecurity data efficiently.

In [Prowler](https://github.com/prowler-cloud/prowler), we leverage the py-ocsf-models package to generate JSON formatted OCSF outputs, specifically focusing on Detection Findings. This integration facilitates the standardization and sharing of cybersecurity findings in a structured and widely-accepted format, enhancing the interoperability between different security tools and platforms.

## Features

- **Comprehensive OCSF Schema Implementation**: Includes models for events, findings, objects, and profiles, covering the entire OCSF Schema.
- **Easy Data Manipulation**: Easily create, modify, and interact with cybersecurity data structures.
- **Serialization and Deserialization Support**: Convert OCSF model instances to and from JSON for easy storage and transmission.
- **Extensible Design**: Extend and customize models to fit specific requirements while staying compliant with the OCSF schema.

## Installation

Install `py-ocsf-models` using pip:

```bash
pip install py-ocsf-models
```

Import the package in your Python application:

```python
import py_ocsf_models
```

## Usage Example
The following is an example demonstrating how to create a full OCSF Detection Finding using py-ocsf-models. This example showcases the instantiation of various models and their association to create a rich, structured representation of a detection finding.

```python
from datetime import datetime
import uuid
from py_ocsf_models.events.findings.detection_finding import DetectionFinding
from py_ocsf_models.events.findings.finding import FindingInformation
from py_ocsf_models.objects.api import API, Group, RequestElements, ResponseElements, Service
from py_ocsf_models.objects.cloud import Account, Cloud, Organization
from py_ocsf_models.objects.container import Container, FingerPrint, Image
from py_ocsf_models.objects.dns_query import DNSOpcodeID, DNSQuery
from py_ocsf_models.objects.evidence_artifacts import EvidenceArtifacts
from py_ocsf_models.objects.metadata import Metadata
from py_ocsf_models.objects.operating_system import OperatingSystem
from py_ocsf_models.objects.product import Feature, Product
from py_ocsf_models.objects.remediation import KBArticle, Remediation
from py_ocsf_models.objects.resource_details import ResourceDetails
from py_ocsf_models.objects.vulnerability_details import VulnerabilityDetails
from py_ocsf_models.profiles.cloud import CloudProfile
from py_ocsf_models.profiles.container import ContainerProfile

# Example instantiation of a DetectionFinding object with nested structures
detection_finding = DetectionFinding(
        metadata=Metadata(
            version="1.0",
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
        finding_info=FindingInformation(
            title="Title",
            uid="123",
        ),
        severity_id=1,
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
        category_name="Findings",
        category_uid=2,
        class_name="Detection Finding",
        class_uid=2004,
        cloud=CloudProfile(
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
                            pod_uuid=str(uuid.uuid4()),
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
                            pod_uuid=str(uuid.uuid4()),
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
            container=ContainerProfile(
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
                    pod_uuid=str(uuid.uuid4()),
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
                                pod_uuid=str(uuid.uuid4()),
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
                                pod_uuid=str(uuid.uuid4()),
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
        impact_id=123,
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

# Serialize to JSON (for example)
detection_finding_json = detection_finding.to_json()
print(detection_finding_json)
```


## Contributing
Contributions are welcome! Whether you're fixing a bug, adding new features, or improving the documentation, please feel free to make a pull request or open an issue.

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This package is built to support and encourage the adoption of the Open Cybersecurity Schema Framework (OCSF) and facilitate the handling of cybersecurity data in Python applications.

## Support
For support, questions, or feedback, please open an issue on the GitHub repository.
