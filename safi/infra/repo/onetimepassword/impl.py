"""Declares :class:`OneTimePasswordRepository`."""
import sq.lib.timezone

from ...orm import OneTimePassword as OneTimePasswordDAO
from .base import BaseOneTimePasswordRepository


class OneTimePasswordRepository(BaseOneTimePasswordRepository):
    """Knows how to construct domain objects to and from the
    persistence layer.
    """
    columns = OneTimePasswordDAO.__mapper__.columns.keys()

    def get(self, gsid):
        """Return the OTP object specified by the query parameters."""
        return self.session.query(OneTimePasswordDAO)\
            .filter(OneTimePasswordDAO.gsid == gsid)\
            .one()

    def persist_dao(self, dao):
        """Persists a Data Access Object (DAO) to the persistent
        data store.
        """
        self.session.merge(dao)
        self.session.flush()
        return dao

    def persist_otp(self, persistable):
        """Persists a One-Time Password (OTP) object to the persistent data
        store.
        """
        dao = OneTimePasswordDAO(**persistable & self.columns)
        dao.secret = bytes.hex(self.cipher.encrypt(dao.secret.encode()))
        dao.generated = sq.lib.timezone.now()
        self.session.merge(dao)
        self.session.flush()
