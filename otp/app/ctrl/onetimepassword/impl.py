"""Contains the concrete implementation of :class:`BaseOneTimePasswordCtrl`."""
from .base import BaseOneTimePasswordCtrl


class OneTimePasswordCtrl(BaseOneTimePasswordCtrl):
    """Handles ``GET``, ``POST`` and ``PUT`` requests to the OTP
    endpoint.
    """

    async def post(self, request, kind, gsid): #pylint: disable=arguments-differ
        """Generate a new One-Time Password for the :class`Subject`
        identified in the request URI.

        Args:
            kind (string): specifies the type of OTP (``HOTP`` or ``TOTP``).
            gsid (string): identifies the :class:`Subject`.

        Returns:
            :class:`~sq.interfaces.http.response.Response`
        """
        return self.render(request, 201, self.otp.generate(kind, gsid))

    async def put(self, request, kind, gsid, *args, **kwargs): #pylint: disable=arguments-differ
        raise NotImplementedError("Subclasses must override this method.")

    async def get(self, request, kind, gsid): #pylint: disable=arguments-differ
        """Returns the shared secret for the :class:`Subject`
        identified in the request URI.

        Args:
            kind (string): specifies the type of OTP (``HOTP`` or ``TOTP``).
            gsid (string): identifies the :class:`Subject`.

        Returns:
            :class:`~sq.interfaces.http.response.Response`
        """
        return self.render(request, self.finder.get_shared_secret(kind, gsid), 200)

    def render(self, request, status, content, *args, **kwargs):
        # If the client does not provide the Accept header, werkzeufg
        # assumes that any content type will do. This will lead to the
        # below code always being executed. To prevent this, we set the
        # Accept header to our default content type.
        mimetype = self.default_mimetype
        if 'Accept' in request.headers:
            mimetype = request.accept_mimetypes.best_match(self.image.accept)
        if mimetype is not None:
            # The client has requested to receive the OTP link
            # as a QR image.
            content = self.image.generate(content.link)
            assert isinstance(content, bytes)
        return self.render_to_response(content,
            content_type=mimetype, status_code=status)
