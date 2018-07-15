"""Declares the :class:`OneTimePasswordService` service interface."""
import pyotp

from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):
    """Exposes an API to generate and verify One-Time Passwords (OTPs)."""
    kinds = {
        'totp': pyotp.TOTP,
        'hotp': pyotp.HOTP
    }

    def generate(self, kind, gsid, ident=None, issuer=None):
        """Generates a new One-Time Password (OTP) for the identified Subject."""
        secret = pyotp.random_base32()
        otp = self.kinds[kind](secret)
        uri = otp.provisioning_uri(ident or "boo@foo.bar", issuer_name="Wizards of Industry")
        return self.dto(link=uri)

    def verify(self, kind, gsid, code):
        """Verified that the correct OTP was provided by the client, for the
        identified Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")
