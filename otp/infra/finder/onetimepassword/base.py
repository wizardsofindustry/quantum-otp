import ioc
from sq.readmodel import Finder
from sq.exceptions import ObjectDoesNotExist


class BaseOneTimePasswordFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')
    cipher = ioc.class_property('LocalCipher')

    SubjectDoesNotExist = type('SubjectDoesNotExist', (ObjectDoesNotExist,), {})

    def get_for_subject(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
