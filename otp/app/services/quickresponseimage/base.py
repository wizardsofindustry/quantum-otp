from sq.service import Service


class BaseQuickResponseImageService(Service):

    def generate(self, link):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
