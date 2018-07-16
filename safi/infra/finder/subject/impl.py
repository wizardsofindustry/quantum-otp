from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def available_challenges(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")
