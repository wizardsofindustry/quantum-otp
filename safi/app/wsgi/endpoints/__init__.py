from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint
from .pin import PinEndpoint
from .onetimepassword import OneTimePasswordEndpoint
from .verification import VerificationEndpoint
from .subjectchallenges import SubjectChallengesEndpoint
from .authentication import AuthenticationEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
    PinEndpoint.as_rule(),
    OneTimePasswordEndpoint.as_rule(),
    VerificationEndpoint.as_rule(),
    SubjectChallengesEndpoint.as_rule(),
    AuthenticationEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
