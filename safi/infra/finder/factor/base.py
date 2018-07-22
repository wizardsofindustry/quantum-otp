import ioc
from sq.readmodel import Finder


class BaseFactorFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')
    cipher = ioc.class_property('LocalCipher')

    def get(self, factor):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
