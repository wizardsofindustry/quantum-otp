"""Declares the :class:`OneTimePasswordService` service interface."""
import pyotp

from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):
    """Exposes an API to generate and verify One-Time Passwords (OTPs)."""

    def generate(self, kind, gsid, nsid, issuer):
        """Generates a new One-Time Password (OTP) for the identified Subject."""
        if kind not in ('totp', 'hotp'):
            raise ValueError(f'Invalid OTP type: {kind}')
        secret = pyotp.random_base32()
        otp = getattr(pyotp, kind.upper())(secret)
        uri = otp.provisioning_uri(nsid, issuer_name=issuer)
        dto = self.dto(
            storage_class='otp',
            kind=kind,
            gsid=gsid,
            nsid=nsid,
            issuer=issuer,
            secret=secret,
            counter=getattr(otp, 'interval', 0) # initialize counter at 0 if HOTP
        )
        self.repo.persist(dto)
        return self.dto(link=uri)

    def verify(self, kind, gsid, code):
        """Verified that the correct OTP was provided by the client, for the
        identified Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")
