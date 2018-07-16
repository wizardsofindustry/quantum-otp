import ioc
from sq.persistence import Repository


class BaseOneTimePasswordRepository(Repository):
    cipher = ioc.class_property('LocalCipher')
    session = ioc.class_property('DatabaseSessionFactory')

    def persist_otp(self, persistable):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
