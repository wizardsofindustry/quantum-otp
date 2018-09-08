"""Declares the :class`PinService`."""
import hmac
import secrets

from quantum.lib import timezone

from .base import BasePinService


random = secrets.SystemRandom()


class PinService(BasePinService):
    """Exposes the API to create, update and unblock PIN."""

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
        """Return a boolean indicating if the PIN `pin` for the **Subject**
        identified by `gsid` is correct.
        """
        dao = self.repo.get(gsid)
        if dao is None:
            return False

        # TODO: Do not hard code this
        if dao.failed >= 3:
            return False

        dao.last_used = timezone.now()
        result = hmac.compare_digest(dao.pin, str(pin))
        dao.failed = (dao.failed + 1) if not result else 0

        # TODO: Quick hacky fix -- repo should recognize DAO
        dao.storage_class = 'pin'

        self.repo.persist(dao)
        return result
