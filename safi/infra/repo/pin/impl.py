from .base import BasePinRepository


class PinRepository(BasePinRepository):

    def persist_pin(self, persistable):
        raise NotImplementedError("Subclasses must override this method.")
