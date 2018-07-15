from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint
from .onetimepassword import OneTimePasswordEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
    OneTimePasswordEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
