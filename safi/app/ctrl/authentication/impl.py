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
        """Parse and deserialize the request body and authenticate
        the specified **Subject** based on the factors enclosed in
        the entity.
        """
        status = 401
        ctx = {'state': "FAILURE"}
        try:
            self.auth.authenticate(request.payload.gsid,
                request.payload.factors)
            status = 200
            ctx['state'] = 'SUCCESS'
        except self.auth.SubjectDoesNotExist:
            status = 404
        except self.auth.InvalidFactor as e:
            status = 401
            ctx['failed'] = e.args[0]
        return self.render_to_response(ctx=ctx, status_code=status)
