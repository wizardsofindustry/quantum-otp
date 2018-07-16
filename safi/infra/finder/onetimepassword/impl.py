"""Declares :class:`OneTimePasswordFinder`."""
import pyotp

from ...orm import OneTimePassword as OneTimePasswordDAO
from .base import BaseOneTimePasswordFinder


class OneTimePasswordFinder(BaseOneTimePasswordFinder):
    """Provides an interface to abstract queries related to One-Time
    Passwords (OTPs).
    """

    def get_for_subject(self, gsid):
        """Returns the shared secret for the Subject identified by `gsid`."""
        dao = self.session.query(OneTimePasswordDAO)\
            .filter(OneTimePasswordDAO.gsid == gsid)\
            .first()
        if dao is None:
            raise self.SubjectDoesNotExist([str(gsid)], name='Subject')
        secret = self.cipher.decrypt(bytes.fromhex(dao.secret))
        return getattr(pyotp, dao.kind.upper())(secret)
