from enum import IntEnum


class ClassUID(IntEnum):
    """
    The unique identifier of a class. A Class describes the attributes available in an event.

    2003 ComplianceFinding: Compliance Finding events describe results of evaluations performed against resources, to check compliance with various Industry Frameworks or Security Standards such as NIST SP 800-53, CIS AWS Foundations Benchmark v1.4.0, ISO/IEC 27001 etc. Note: if the event producer is a security control, the security_control profile should be applied and its attacks information, if present, should be duplicated into the finding_info object.
    Note: If the Finding is an incident, i.e. requires incident workflow, also apply the incident profile or aggregate this finding into an Incident Finding.
    """

    ComplianceFinding = 2003

    """
    The unique identifier of a class. A Class describes the attributes available in an event.

    2004 DetectionFinding: A Detection Finding describes detections or alerts generated by security products using correlation engines, detection engines or other methodologies. Note: if the product is a security control, the security_control profile should be applied and its attacks information should be duplicated into the finding_info object. Note: If the Finding is an incident, i.e. requires incident workflow, also apply the incident profile or aggregate this finding into an Incident Finding.
    """
    DetectionFinding = 2004

    """
    The unique identifier of a class. A Class describes the attributes available in an event.

    2007 ApplicationSecurityPostureFinding: The Application Security Posture Finding event is a notification about any bug, defect, deficiency, exploit, vulnerability, weakness or any other issue with software and related systems
    """
    ApplicationSecurityPostureFinding = 2007
