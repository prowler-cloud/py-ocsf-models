from enum import IntEnum


class DispositionID(IntEnum):
    """
    Describes the outcome or action taken by a security control, such as access control checks, malware detections or various types of policy violations.

    0	Unknown The disposition is unknown.
    1	Allowed Granted access or allowed the action to the protected resource.
    2	Blocked Denied access or blocked the action to the protected resource.
    3	Quarantined A suspicious file or other content was moved to a benign location.
    4	Isolated A session was isolated on the network or within a browser.
    5	Deleted A file or other content was deleted.
    6	Dropped The request was detected as a threat and resulted in the connection being dropped.
    7	Custom Action A custom action was executed such as running of a command script. Use the message attribute of the base class for details.
    8	Approved A request or submission was approved. For example, when a form was properly filled out and submitted. This is distinct from 1 'Allowed'.
    9	Restored A quarantined file or other content was restored to its original location.
    10	Exonerated A suspicious or risky entity was deemed to no longer be suspicious (re-scored).
    11	Corrected A corrupt file or configuration was corrected.
    12	Partially Corrected A corrupt file or configuration was partially corrected.
    13	Uncorrected A corrupt file or configuration was not corrected.
    14	Delayed An operation was delayed, for example if a restart was required to finish the operation.
    15	Detected Suspicious activity or a policy violation was detected without further action.
    16	No Action The outcome of an operation had no action taken.
    17	Logged The operation or action was logged without further action.
    18	Tagged A file or other entity was marked with extended attributes.
    19	Alert The request or activity was detected as a threat and resulted in a notification but request was not blocked.
    20	Count Counted the request or activity but did not determine whether to allow it or block it.
    21	Reset The request was detected as a threat and resulted in the connection being reset.
    22	Captcha Required the end user to solve a CAPTCHA puzzle to prove that a human being is sending the request.
    23	Challenge Ran a silent challenge that required the client session to verify that it's a browser, and not a bot.
    24	Access Revoked The requestor's access has been revoked due to security policy enforcements. Note: use the Host profile if the User or Actor requestor is not present in the event class.
    25	Rejected A request or submission was rejected. For example, when a form was improperly filled out and submitted. This is distinct from 2 'Blocked'.
    26	Unauthorized An attempt to access a resource was denied due to an authorization check that failed. This is a more specific disposition than 2 'Blocked' and can be complemented with the authorizations attribute for more detail.
    27	Error An error occurred during the processing of the activity or request. Use the message attribute of the base class for details.
    99	Other The disposition is not mapped. See the disposition attribute, which contains a data source specific value.
    """

    Unknown = 0
    Allowed = 1
    Blocked = 2
    Quarantined = 3
    Isolated = 4
    Deleted = 5
    Dropped = 6
    CustomAction = 7
    Approved = 8
    Restored = 9
    Exonerated = 10
    Corrected = 11
    PartiallyCorrected = 12
    Uncorrected = 13
    Delayed = 14
    Detected = 15
    NoAction = 16
    Logged = 17
    Tagged = 18
    Alert = 19
    Count = 20
    Reset = 21
    CaptchaRequired = 22
    ChallengeRan = 23
    AccessRevoked = 24
    Rejected = 25
    Unauthorized = 26
    Error = 27
    Other = 99
