"""Contains the concrete implementation of :class:`BasePinCtrl`."""
from .base import BasePinCtrl


class PinCtrl(BasePinCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
