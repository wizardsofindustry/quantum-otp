"""Contains the concrete implementation of :class:`BaseSubjectChallengeCtrl`."""
from .base import BaseSubjectChallengeCtrl


class SubjectChallengeCtrl(BaseSubjectChallengeCtrl):

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
