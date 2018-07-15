from .base import BaseQuickResponseImageService


class QuickResponseImageService(BaseQuickResponseImageService):
    accept = [
        "image/png"
    ]

    def generate(self):
        raise NotImplementedError("Subclasses must override this method.")
