"""Contains the concrete implementation of :class:`BaseOneTimePasswordCtrl`."""
from .base import BaseOneTimePasswordCtrl


class OneTimePasswordCtrl(BaseOneTimePasswordCtrl):
    """Handles ``GET``, ``POST`` and ``PUT`` requests to the OTP
    endpoint.
    """

    async def post(self, request, kind, gsid, *args, **kwargs): #pylint: disable=arguments-differ
        """Generate a new One-Time Password for the Subject
        identified in the request URI.

        Args:
            kind (string): specifies the type of OTP (``HOTP`` or ``TOTP``).
            gsid (string): identifies the :class:`Subject`.

        Returns:
            :class:`~sq.interfaces.http.response.Response`
        """
        content = self.otp.generate(kind, gsid)
        mimetype = request.accept_mimetypes(self.image.accept)
        if mimetype is not None:
            # The client has requested to receive the OTP link
            # as a QR image.
            content = self.image.generate(content.link)
            assert isinstance(content, bytes)
        return self.render_to_response(content, mimetype=mimetype,
            status=201)

    async def put(self, request, kind, gsid, *args, **kwargs): #pylint: disable=arguments-differ
        raise NotImplementedError("Subclasses must override this method.")

    async def get(self, request, kind, gsid, *args, **kwargs): #pylint: disable=arguments-differ
        raise NotImplementedError("Subclasses must override this method.")
