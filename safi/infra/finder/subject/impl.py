from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def available_challenges(self, gsid):
        """Returns a Data Transfer Object (DTO) containing the factors that are
        available for interim authentication challenges against the Subject
        identified by string `gsid`.
        """
        raise NotImplementedError("Subclasses must override this method.")
