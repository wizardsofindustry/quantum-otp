import ioc
from sq.persistence import Repository


class BasePinRepository(Repository):
    session = ioc.class_property('DatabaseSessionFactory')

    def get(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")

    def exists(self, gsid):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_pin(self, persistable):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
