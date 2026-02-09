from typing import Any, Optional

from pydantic import BaseModel

from py_ocsf_models.objects.authorization import AuthorizationResult
from py_ocsf_models.objects.user import User


class Actor(BaseModel):
    """
    The Actor object describes the user, role, application, service, or process
    that initiated or performed a specific activity.

    Constraint: At least one of app_name, app_uid, process, session, user must be present.

    Attributes:
    - App Name (app_name) [Optional]: The name of the application.
    - App UID (app_uid) [Optional]: The unique identifier of the application.
    - Authorizations (authorizations) [Optional]: The authorization results.
    - Identity Provider (idp) [Optional]: The identity provider details.
    - Process (process) [Optional]: The process that performed the activity.
    - Session (session) [Optional]: The user session.
    - User (user) [Recommended]: The user that performed the activity.

    Note: idp, process, and session are typed as Any since those objects
    are not yet implemented in this library. They can be added later.
    """

    app_name: Optional[str] = None
    app_uid: Optional[str] = None
    authorizations: Optional[list["AuthorizationResult"]] = None
    idp: Optional[Any] = None  # IdentityProvider - not yet implemented
    process: Optional[Any] = None  # Process - not yet implemented
    session: Optional[Any] = None  # Session - not yet implemented
    user: Optional[User] = None
