import ioc
from quantum.exceptions import DuplicateEntity
from sq.service import Service


class BasePinService(Service):
    repo = ioc.class_property('PinRepository')

    DuplicatePinCode = type('DuplicatePinCode', (DuplicateEntity,), {})

    def createpin(self, gsid, pin=None):
        raise NotImplementedError("Subclasses must override this method.")

    def verify(self, gsid, pin):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
