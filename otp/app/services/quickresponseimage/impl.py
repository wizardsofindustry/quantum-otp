"""Declares the :class:`QuickResponseImageService` service object."""
import io

import qrcode

from .base import BaseQuickResponseImageService


class QuickResponseImageService(BaseQuickResponseImageService):
    """Provides an interface to generate QR-codes from OTP shared
    secrets.
    """
    accept = [
        "image/png"
    ]

    def generate(self, link):
        """Generates a QR-code holding `link`."""
        buf = io.BytesIO()
        img = qrcode.make(link)
        img.save(buf, format='PNG')
        return buf.getvalue()
