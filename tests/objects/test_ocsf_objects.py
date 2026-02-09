"""Tests for the new OCSF 1.7.0 objects."""

import pytest
from pydantic import ValidationError

from py_ocsf_models.events.findings.severity_id import SeverityID
from py_ocsf_models.objects.account import Account
from py_ocsf_models.objects.actor import Actor
from py_ocsf_models.objects.authorization import AuthorizationResult
from py_ocsf_models.objects.cve import CVE
from py_ocsf_models.objects.firewall_rule import FirewallRule
from py_ocsf_models.objects.malware import Malware, MalwareClassificationID
from py_ocsf_models.objects.policy import Policy
from py_ocsf_models.objects.ticket import Ticket, TicketStatusID, TicketTypeID
from py_ocsf_models.objects.user import User


class TestActor:
    """Tests for the Actor object."""

    def test_actor_with_user(self) -> None:
        """Actor with user field populated."""
        user = User(
            account=Account(name="test-account", type_id=1, uid="acc-123"),
            name="john.doe",
            type_id=1,
            uid="user-123",
        )
        actor = Actor(user=user)
        assert actor.user is not None
        assert actor.user.name == "john.doe"

    def test_actor_with_app_name(self) -> None:
        """Actor with app_name field populated."""
        actor = Actor(app_name="MyApplication", app_uid="app-123")
        assert actor.app_name == "MyApplication"
        assert actor.app_uid == "app-123"

    def test_actor_empty(self) -> None:
        """Actor can be created with no fields (constraint checked at usage)."""
        actor = Actor()
        assert actor.user is None
        assert actor.app_name is None

    def test_actor_with_authorizations(self) -> None:
        """Actor with authorizations."""
        auth = AuthorizationResult(decision="allowed")
        actor = Actor(app_name="App", authorizations=[auth])
        assert len(actor.authorizations) == 1
        assert actor.authorizations[0].decision == "allowed"


class TestMalware:
    """Tests for the Malware object."""

    def test_malware_required_classification_ids(self) -> None:
        """Malware requires classification_ids list."""
        malware = Malware(
            classification_ids=[MalwareClassificationID.Ransomware],
            name="WannaCry",
        )
        assert malware.classification_ids[0] == MalwareClassificationID.Ransomware
        assert malware.name == "WannaCry"

    def test_malware_missing_classification_ids(self) -> None:
        """Malware without classification_ids raises ValidationError."""
        with pytest.raises(ValidationError):
            Malware(name="BadMalware")

    def test_malware_with_cves(self) -> None:
        """Malware with CVE references."""
        malware = Malware(
            classification_ids=[MalwareClassificationID.Trojan],
            cves=[CVE(uid="CVE-2021-44228")],
            name="Log4Shell Exploit",
        )
        assert len(malware.cves) == 1
        assert malware.cves[0].uid == "CVE-2021-44228"

    def test_malware_with_severity(self) -> None:
        """Malware with severity fields."""
        malware = Malware(
            classification_ids=[MalwareClassificationID.Ransomware],
            severity="Critical",
            severity_id=SeverityID.Critical,
        )
        assert malware.severity == "Critical"
        assert malware.severity_id == SeverityID.Critical

    def test_malware_classification_ids_multiple(self) -> None:
        """Malware with multiple classification IDs."""
        malware = Malware(
            classification_ids=[
                MalwareClassificationID.Trojan,
                MalwareClassificationID.Backdoor,
            ],
        )
        assert len(malware.classification_ids) == 2


class TestTicket:
    """Tests for the Ticket object."""

    def test_ticket_with_uid(self) -> None:
        """Ticket with uid populated."""
        ticket = Ticket(uid="JIRA-1234", title="Security Issue")
        assert ticket.uid == "JIRA-1234"
        assert ticket.title == "Security Issue"

    def test_ticket_with_src_url(self) -> None:
        """Ticket with src_url populated."""
        ticket = Ticket(src_url="https://jira.example.com/JIRA-1234")
        assert ticket.src_url == "https://jira.example.com/JIRA-1234"

    def test_ticket_with_status(self) -> None:
        """Ticket with status fields."""
        ticket = Ticket(
            uid="TICKET-123",
            status="In Progress",
            status_id=TicketStatusID.InProgress,
        )
        assert ticket.status == "In Progress"
        assert ticket.status_id == TicketStatusID.InProgress

    def test_ticket_with_type(self) -> None:
        """Ticket with type fields."""
        ticket = Ticket(
            uid="TICKET-123",
            type="Internal",
            type_id=TicketTypeID.Internal,
        )
        assert ticket.type == "Internal"
        assert ticket.type_id == TicketTypeID.Internal

    def test_ticket_empty(self) -> None:
        """Ticket can be created empty (constraint checked at usage)."""
        ticket = Ticket()
        assert ticket.uid is None
        assert ticket.src_url is None


class TestFirewallRule:
    """Tests for the FirewallRule object."""

    def test_firewall_rule_with_name(self) -> None:
        """FirewallRule with name populated."""
        rule = FirewallRule(name="Block SSH", category="network")
        assert rule.name == "Block SSH"
        assert rule.category == "network"

    def test_firewall_rule_with_uid(self) -> None:
        """FirewallRule with uid populated."""
        rule = FirewallRule(uid="rule-12345", desc="Deny all outbound")
        assert rule.uid == "rule-12345"
        assert rule.desc == "Deny all outbound"

    def test_firewall_rule_with_match_details(self) -> None:
        """FirewallRule with match details."""
        rule = FirewallRule(
            name="SQL Injection Block",
            match_details=["SELECT", "UNION", "DROP TABLE"],
            match_location="query_string",
        )
        assert len(rule.match_details) == 3
        assert rule.match_location == "query_string"

    def test_firewall_rule_empty(self) -> None:
        """FirewallRule can be created empty (constraint checked at usage)."""
        rule = FirewallRule()
        assert rule.name is None
        assert rule.uid is None


class TestAuthorizationResult:
    """Tests for the AuthorizationResult object."""

    def test_authorization_result_with_decision(self) -> None:
        """AuthorizationResult with decision field."""
        auth = AuthorizationResult(decision="allowed")
        assert auth.decision == "allowed"

    def test_authorization_result_with_policy(self) -> None:
        """AuthorizationResult with policy."""
        policy = Policy(name="AdminPolicy", uid="policy-123")
        auth = AuthorizationResult(decision="denied", policy=policy)
        assert auth.decision == "denied"
        assert auth.policy.name == "AdminPolicy"

    def test_authorization_result_empty(self) -> None:
        """AuthorizationResult can be created empty."""
        auth = AuthorizationResult()
        assert auth.decision is None
        assert auth.policy is None


class TestMalwareClassificationID:
    """Tests for the MalwareClassificationID enum."""

    def test_classification_values(self) -> None:
        """Verify key classification values."""
        assert MalwareClassificationID.Unknown == 0
        assert MalwareClassificationID.Ransomware == 10
        assert MalwareClassificationID.Trojan == 18
        assert MalwareClassificationID.Virus == 19
        assert MalwareClassificationID.Worm == 22
        assert MalwareClassificationID.Other == 99

    def test_classification_gap_at_12(self) -> None:
        """Value 12 is intentionally skipped in OCSF schema."""
        values = [e.value for e in MalwareClassificationID]
        assert 12 not in values


class TestTicketEnums:
    """Tests for Ticket-related enums."""

    def test_ticket_status_values(self) -> None:
        """Verify TicketStatusID values."""
        assert TicketStatusID.Unknown == 0
        assert TicketStatusID.New == 1
        assert TicketStatusID.InProgress == 2
        assert TicketStatusID.Closed == 5
        assert TicketStatusID.Other == 99

    def test_ticket_type_values(self) -> None:
        """Verify TicketTypeID values."""
        assert TicketTypeID.Unknown == 0
        assert TicketTypeID.Internal == 1
        assert TicketTypeID.External == 2
        assert TicketTypeID.Other == 99
