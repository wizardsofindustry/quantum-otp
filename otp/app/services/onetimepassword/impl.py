"""Declares the :class:`OneTimePasswordService` service interface."""
import pyotp

from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):
    """Exposes an API to generate and verify One-Time Passwords (OTPs)."""Verified that the correct OTP was provided by the client, for the
        identified Subject.
        """
        secret = pyotp.random_base32()
        otp = self.kinds[kind](secret)
        uri = otp.provisioning_uri(nsid, issuer_name=issuer)
        return self.dto(link=uri)

    def verify(self, kind, gsid, code):
        """Verified that the correct OTP was provided by the client, for the
        identified Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")
