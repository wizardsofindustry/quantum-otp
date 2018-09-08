"""Declares :class:`PinRepository`."""
from .base import BasePinRepository

from ...orm import PIN


class PinRepository(BasePinRepository):

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
