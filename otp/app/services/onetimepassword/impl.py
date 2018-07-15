from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):

    def generate(self, kind, gsid):
        """Generates a new One-Time Password (OTP) for the identified Subject."""
        raise NotImplementedError("Subclasses must override this method.")

    def verify(self, kind, gsid, code):
        """Verified that the correct OTP was provided by the client, for the
        identified Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")
