import ioc
from sq.exceptions import AuthenticationFailed
from sq.exceptions import DuplicateEntity
from sq.service import Service


class BaseOneTimePasswordService(Service):
    cipher = ioc.class_property('LocalCipher')
    repo = ioc.class_property('OneTimePasswordRepository')
    factory = ioc.class_property('SubjectFactory')
    finder = ioc.class_property('FactorFinder')

    InvalidOneTimePassword = type('InvalidOneTimePassword', (AuthenticationFailed,), {})
    OneTimePasswordActive = type('OneTimePasswordActive', (DuplicateEntity,), {})

    def enable(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")

    def disable(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")

    def generate(self, kind, gsid, nsid, issuer, force=False):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
