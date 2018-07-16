"""Contains the concrete implementation of :class:`BaseAuthenticationCtrl`."""
from .base import BaseAuthenticationCtrl


class AuthenticationCtrl(BaseAuthenticationCtrl):
    """Provide a handler for ``POST`` requests, parsing **Factors** from
    the request body and notify the client of a succesful authentication
    throuh the HTTP status code of the response; ``200`` for succesful
    authentication using the provided **Factors**, ``401`` or ``403``
    for failure.
    """

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
