from .base import BaseOneTimePasswordRepository


class OneTimePasswordRepository(BaseOneTimePasswordRepository):

    def persist_otp(self, persistable):
        raise NotImplementedError("Subclasses must override this method.")
