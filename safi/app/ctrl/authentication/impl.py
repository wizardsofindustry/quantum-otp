"""Contains the concrete implementation of :class:`BaseAuthenticationCtrl`."""
from .base import BaseAuthenticationCtrl


class AuthenticationCtrl(BaseAuthenticationCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
