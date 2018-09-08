"""Declares :class:`PinRepository`."""
import sqlalchemy

from .base import BasePinRepository

from ...orm import PIN


class PinRepository(BasePinRepository):

    def exists(self, gsid):
        """Return a boolean indicating if a PIN exists for the **Subject**
        identified by `gsid`.
        """
        q = sqlalchemy.exists()\
            .where(PIN.gsid == gsid)
        return self.session.query(q).scalar()

    def persist_pin(self, persistable):
      """Persists a persistable object representing a Personal Identification
      Number (PIN) to the persistent storage backend.
      """
      if not isinstance(persistable, PIN):
        pin = PIN(
          gsid=persistable.gsid,
          pin=persistable.pin
        )
      else:
        pin = persistable
      return self.session.merge(pin)
