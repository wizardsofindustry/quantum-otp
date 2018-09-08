"""Declares the :class`PinService`."""
import secrets

from .base import BasePinService


random = secrets.SystemRandom()


class PinService(BasePinService):

    def createpin(self, gsid, pin=None):
      """Create a new PIN for the **Subject** identified by `gsid`. If
      `pin` is ``None``, then a code is automatically generated.
      """
      if self.repo.exists(gsid):
        raise self.DuplicatePinCode()
      if pin is None:
        pin = random.randint(10000, 99999)
      self.repo.persist(self.dto(storage_class='pin', gsid=gsid, pin=pin))
      return self.dto(pin=pin)

    def verify(self, gsid, pin):
        raise NotImplementedError("Subclasses must override this method.")
