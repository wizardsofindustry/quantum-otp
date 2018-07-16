"""Contains the concrete implementation of :class:`BasePinCtrl`."""
from .base import BasePinCtrl


class PinCtrl(BasePinCtrl):
    """Provide a handler for ``POST`` requests, containing a partial
    **Subject** (only its `gsid`) and generatie a Personal Identification
    Number (PIN) for the specified **Subject**.
    """

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
