"""Declares the :class:`OneTimePasswordService` service interface."""
import pyotp

from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):
    """Exposes an API to generate and verify One-Time Passwords (OTPs)."""

    def enable(self, gsid):
        """Disables the TOTP for the **Subject** identified by
        `gsid`.
        """
        dao = self.repo.get(gsid)
        dao.enabled = True
        self.repo.persist_dao(dao)

    def disable(self, gsid):
        """Disables the TOTP for the **Subject** identified by
        `gsid`.
        """
        dao = self.repo.get(gsid)
        dao.enabled = False
        self.repo.persist_dao(dao)

    def generate(self, kind, gsid, nsid, issuer, force=False):
        """Generates a new One-Time Password (OTP) for the identified Subject."""
        assert kind == 'totp', "HOTP support is deprecated."
        if self.finder.has_active_otp(kind, gsid) and not force:
            raise self.OneTimePasswordActive()
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
        return self.dto(link=uri, secret=secret)
