"""Contains the concrete implementation of :class:`BaseSubjectChallengeCtrl`."""
from .base import BaseSubjectChallengeCtrl


class SubjectChallengeCtrl(BaseSubjectChallengeCtrl):
    """Provide handler for ``GET`` requests, returning the **Factors**
    that the **Subject** identified in the request URI  may use for
    interim authentication challenges.
    """

    async def get(self, request, gsid, *args, **kwargs): #pylint: disable=arguments-differ
        """Serialize a **SubjectInterimFactors** Data Transfer Object (DTO)
        and return it to the client by including it as the response payload.
        """
        return self.render_to_response(
            ctx=self.subject.available_challenges(gsid))
