import ioc
from sq.service import Service


class BaseAuthenticationService(Service):
    factors = ioc.class_property('FactorFinder')
    otp = ioc.class_property('OneTimePasswordService')
    pin = ioc.class_property('PinService')

    SubjectDoesNotExist = type('SubjectDoesNotExist', (Exception,), {})
    InvalidFactor = type('InvalidFactor', (Exception,), {})
    SubjectIsBlocked = type('SubjectIsBlocked', (Exception,), {})

    def authenticate(self, gsid, factors):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
