import ioc
from sq.persistence import Repository


class BasePinRepository(Repository):
    session = ioc.class_property('DatabaseSessionFactory')

    def persist_pin(self, persistable):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
