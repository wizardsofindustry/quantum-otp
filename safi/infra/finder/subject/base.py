from sq.readmodel import Finder
from sq.exceptions import ObjectDoesNotExist


class BaseSubjectFinder(Finder):

    NoChallengesFound = type('NoChallengesFound', (ObjectDoesNotExist,), {})

    def available_challenges(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
