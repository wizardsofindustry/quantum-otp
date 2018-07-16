import ioc
from sq.readmodel import Finder
from sq.exceptions import ObjectDoesNotExist


class BaseSubjectFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')

    NoChallengesFound = type('NoChallengesFound', (ObjectDoesNotExist,), {})

    def available_challenges(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
