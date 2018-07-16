import sqlalchemy
from sqlalchemy.sql import expression

from ...orm import OneTimePassword
from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def available_challenges(self, gsid):
        """Returns a Data Transfer Object (DTO) containing the factors that are
        available for interim authentication challenges against the Subject
        identified by string `gsid`.
        """
        Q1 = sqlalchemy.select([sqlalchemy.literal('otp').label('type')])\
            .where(OneTimePassword.gsid == gsid)\
            .alias('otp')

        return self.dto(factors=[row.type for row in self.session.query(Q1)])
