from .base import BaseOneTimePasswordRepository


class OneTimePasswordRepository(BaseOneTimePasswordRepository):

    def persist_otp(self, persistable):
        """Persists a One-Time Password (OTP) object to the persistent data
        store.
        """
        raise NotImplementedError("Subclasses must override this method.")
