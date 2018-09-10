"""Declares :class:`SubjectFinder`."""
import sqlalchemy

from ...orm import OneTimePassword
from ...orm import PIN
from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):
    """Provides an API to retrieve information on **Factors** in relation to a
    specific **Subject**.
    """

    def available_challenges(self, gsid):
        """Returns a Data Transfer Object (DTO) containing the factors that are
        available for interim authentication challenges against the Subject
        identified by string `gsid`.
        """
        otp = sqlalchemy.select([sqlalchemy.literal('otp').label('type')])\
            .where(OneTimePassword.gsid == gsid)\
            .where(OneTimePassword.enabled.is_(True))
        pin = sqlalchemy.select([sqlalchemy.literal('pin').label('type')])\
            .where(PIN.gsid == gsid)

        q = otp.union(pin)
        return [row.type for row in self.session.query(q)]
