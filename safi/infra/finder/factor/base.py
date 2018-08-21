import ioc
from sq.readmodel import Finder


class BaseFactorFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')
    cipher = ioc.class_property('LocalCipher')

    def get(self, gsid, using):
        raise NotImplementedError("Subclasses must override this method.")

    def has_active_otp(self, kind, gsid):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
