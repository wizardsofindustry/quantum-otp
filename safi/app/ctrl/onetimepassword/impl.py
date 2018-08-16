"""Contains the concrete implementation of :class:`BaseOneTimePasswordCtrl`."""
import base64

from .base import BaseOneTimePasswordCtrl


class OneTimePasswordCtrl(BaseOneTimePasswordCtrl):
    """Handles ``GET``, ``POST`` and ``PUT`` requests to the OTP
    endpoint.
    """

    async def post(self, request, *args, **kwargs):
        """Generate a new One-Time Password for the :class`Subject`
        identified in the request URI.

        Returns:
            :class:`~sq.interfaces.http.response.Response`
        """
        return self._render(request, 201,
            self.otp.generate('totp', **request.payload))

    def _render(self, request, status, content):
        # If the client does not provide the Accept header, werkzeug
        # assumes that any content type will do. This will lead to the
        # below code always being executed. To prevent this, we set the
        # Accept header to our default content type.
        mimetype = self.default_mimetype #pylint: disable=no-member
        png = self.image.generate(content.link)
        body = None
        if 'Accept' in request.headers:
            mimetype = request.accept_mimetypes.best_match(self.image.accept)
            if mimetype is not None:
                # The client has requested to receive the OTP link
                # as a QR image.
                body = png
                content = None
                assert isinstance(body, bytes)

        # If the body variable was not set at this point, the client
        # wants to receive a datastructure instead of a PNG image.
        if body is None:
            content.qrcode = bytes.decode(base64.b64encode(png))
        assert bool(body) ^ bool(content)
        return self.render_to_response(ctx=content, body=body, #pylint: disable=unexpected-keyword-arg
            content_type=mimetype, status_code=status)
