from .base import BaseOneTimePasswordFinder


class OneTimePasswordFinder(BaseOneTimePasswordFinder):

    def get_for_subject(self, gsid):
        """Returns the shared secret for the Subject identified by `gsid`."""
        raise NotImplementedError("Subclasses must override this method.")
