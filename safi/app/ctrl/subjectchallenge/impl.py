"""Contains the concrete implementation of :class:`BaseSubjectChallengeCtrl`."""
from .base import BaseSubjectChallengeCtrl


class SubjectChallengeCtrl(BaseSubjectChallengeCtrl):

    async def get(self, request, gsid, *args, **kwargs):
        dto = {'challenges': self.subject.available_challenges(gsid)}
        return self.render_to_response(dto)
