"""Contains the concrete implementation of :class:`BaseOneTimePasswordCtrl`."""
from .base import BaseOneTimePasswordCtrl


class OneTimePasswordCtrl(BaseOneTimePasswordCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")

    async def put(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
