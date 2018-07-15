from .base import BaseOneTimePasswordFinder


class OneTimePasswordFinder(BaseOneTimePasswordFinder):

    def get_for_subject(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")
