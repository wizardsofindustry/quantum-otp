import io

import qrcode

from .base import BaseQuickResponseImageService


class QuickResponseImageService(BaseQuickResponseImageService):
    accept = [
        "image/png"
    ]

    def generate(self, link):
        """Generates a QR-code holding `link`."""
        buf = io.BytesIO()
        qr = qrcode.make(link)
        qr.save(buf, format='PNG')
        return buf.getvalue()
