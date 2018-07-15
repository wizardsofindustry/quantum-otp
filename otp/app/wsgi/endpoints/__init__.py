from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
