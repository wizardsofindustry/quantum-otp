import ioc
from sq.exceptions import AuthenticationFailed
from sq.service import Service


class BaseOneTimePasswordService(Service):
    cipher = ioc.class_property('LocalCipher')
    repo = ioc.class_property('OneTimePasswordRepository')
    factory = ioc.class_property('SubjectFactory')
    finder = ioc.class_property('OneTimePasswordFinder')

    InvalidOneTimePassword = type('InvalidOneTimePassword', (AuthenticationFailed,), {})

    def generate(self, kind, gsid, nsid, issuer):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
