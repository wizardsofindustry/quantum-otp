"""Contains the concrete implementation of :class:`BaseVerificationCtrl`."""
from .base import BaseVerificationCtrl


class VerificationCtrl(BaseVerificationCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
