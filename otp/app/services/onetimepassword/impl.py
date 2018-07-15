from .base import BaseOneTimePasswordService


class OneTimePasswordService(BaseOneTimePasswordService):

    def generate(self, kind, gsid):
        raise NotImplementedError("Subclasses must override this method.")

    def verify(self, kind, gsid, code):
        raise NotImplementedError("Subclasses must override this method.")
