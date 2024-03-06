from datetime import datetime
from typing import Optional

# FIXME(circular-dependency)
# from py_ocsf_models.objects.user import User
from pydantic import BaseModel, EmailStr

from py_ocsf_models.objects.geolocation import GeoLocation


class LDAPPerson(BaseModel):
    """
    The LDAPPerson class encapsulates detailed information about an individual within an LDAP or Active Directory system. It is designed to model both the professional and personal attributes of a person, including their role, contact information, and organizational context.

    Attributes:
    - Cost Center (cost_center) [Optional]: Associated cost center for budgeting and financial analysis.
    - Created Time (created_time) [Optional]: Timestamp of when the user account was created.
    - Deleted Time (deleted_time) [Optional]: Timestamp indicating when the user was deleted, useful in AD environments.
    - Email Addresses (email_addrs) [Optional]: list of additional email addresses.
    - Employee ID (employee_uid) [Optional]: Unique identifier assigned by the organization.
    - Geo Location (location) [Optional]: Usual work location of the user.
    - Given Name (given_name) [Optional]: First name of the user.
    - Hire Time (hire_time) [Optional]: Timestamp when the user was hired.
    - Job Title (job_title) [Optional]: Official job title.
    - LDAP Common Name (ldap_cn) [Optional]: Full name as per LDAP cn attribute.
    - LDAP Distinguished Name (ldap_dn) [Optional]: Unique DN in the LDAP directory.
    - Labels (labels) [Optional]: Array of labels or tags associated with the user.
    - Last Login (last_login_time) [Optional]: Last login timestamp.
    - Leave Time (leave_time) [Optional]: When the user left or will leave the organization.
    - Manager (manager) [Optional]: Direct manager, supports org hierarchy.
    - Modified Time (modified_time) [Optional]: Last modification timestamp of the user entry.
    - Office Location (office_location) [Optional]: Primary office location, not necessarily a specific address.
    - Surname (surname) [Optional]: Family or last name.
    """

    cost_center: Optional[str]
    created_time: Optional[datetime]
    deleted_time: Optional[datetime]
    email_addrs: Optional[list[EmailStr]]
    employee_uid: Optional[str]
    location: Optional[GeoLocation]
    given_name: Optional[str]
    hire_time: Optional[datetime]
    job_title: Optional[str]
    ldap_cn: Optional[str]
    ldap_dn: Optional[str]
    labels: Optional[list[str]]
    last_login_time: Optional[datetime]
    leave_time: Optional[datetime]
    # FIXME(circular-dependency)
    # manager: Optional[User]
    modified_time: Optional[datetime]
    office_location: Optional[str]
    surname: Optional[str]
