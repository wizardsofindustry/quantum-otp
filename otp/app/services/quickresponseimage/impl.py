from .base import BaseQuickResponseImageService


class QuickResponseImageService(BaseQuickResponseImageService):

    def generate(self):
        raise NotImplementedError("Subclasses must override this method.")
