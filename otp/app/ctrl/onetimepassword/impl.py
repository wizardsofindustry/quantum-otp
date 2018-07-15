"""Contains the concrete implementation of :class:`BaseOneTimePasswordCtrl`."""
from sq.exceptions import EndpointDoesNotExist

from .base import BaseOneTimePasswordCtrl


class OneTimePasswordCtrl(BaseOneTimePasswordCtrl):
    """Handles ``GET``, ``POST`` and ``PUT`` requests to the OTP
    endpoint.
    """

    async def post(self, request, *args, **kwargs):
        """Generate a new One-Time Password for the :class`Subject`
        identified in the request URI.

        Args:
            kind (string): specifies the type of OTP (``HOTP`` or ``TOTP``).

        Returns:
            :class:`~sq.interfaces.http.response.Response`
        """
        if kwargs.get('kind') not in ('totp', 'hotp'):
            raise EndpointDoesNotExist(url=request.path)
        return self._render(request, 201,
            self.otp.generate(kwargs['kind'], **request.payload))

    def _render(self, request, status, content):
        # If the client does not provide the Accept header, werkzeufg
        # assumes that any content type will do. This will lead to the
        # below code always being executed. To prevent this, we set the
        # Accept header to our default content type.
        mimetype = self.default_mimetype #pylint: disable=no-member
        body = None
        if 'Accept' in request.headers:
            mimetype = request.accept_mimetypes.best_match(self.image.accept)
            if mimetype is not None:
                # The client has requested to receive the OTP link
                # as a QR image.
                body = self.image.generate(content.link)
                content = None
                assert isinstance(body, bytes)
        assert bool(body) ^ bool(content)
        return self.render_to_response(ctx=content, body=body, #pylint: disable=unexpected-keyword-arg
            content_type=mimetype, status_code=status)
