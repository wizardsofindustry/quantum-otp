import sq.lib.timezone

from ...orm import OneTimePassword as OneTimePasswordDAO
from .base import BaseOneTimePasswordRepository


class OneTimePasswordRepository(BaseOneTimePasswordRepository):
    columns = OneTimePasswordDAO.__mapper__.columns.keys()

    def persist_otp(self, persistable):
        """Persists a One-Time Password (OTP) object to the persistent data
        store.
        """
        dao = OneTimePasswordDAO(**persistable & self.columns)
        dao.secret = bytes.hex(self.cipher.encrypt(dao.secret.encode()))
        dao.generated = sq.lib.timezone.now()
        self.session.add(dao)
        self.session.flush()
