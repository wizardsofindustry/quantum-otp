from .base import BasePinService


class PinService(BasePinService):

    def createpin(self, gsid, pin=None):
        raise NotImplementedError("Subclasses must override this method.")

    def verify(self, gsid, pin):
        raise NotImplementedError("Subclasses must override this method.")
