"""Declares :class:`AuthenticationService`."""
import pyotp

from .base import BaseAuthenticationService


class AuthenticationService(BaseAuthenticationService):
    """Exposes an interface to authenticate **Subjects** using the
    provided **Factors**.
    """

    # TODO: All the logic in the _authenticate_* methods must
    # be moved to the domain model when the compiler implements
    # that.

    def authenticate(self, gsid, factors):
        """Authenticate the **Subject** identified by string `gsid` using
        a list of **Factor** instances `factors`. The :meth:`authenticate()`
        method raises an exception on any authentication failure; a return
        without exceptions indicates that the authentication was succesful.
        """
        failed_factors = []
        for dto in factors:
            func = self._get_method(dto)
            try:
                func(dto | {'gsid': gsid})
            except self.InvalidFactor as e:
                failed_factors.append(e.args[0])

        if failed_factors:
            raise self.InvalidFactor(failed_factors)

        # If the code reaches this point, the Subject is
        # succesfully authenticated.

    def _authenticate_otp(self, dto):
        secret = self.factors.get(dto.gsid, dto.using)
        if secret is None:
            raise self.SubjectDoesNotExist([dto.gsid], 'Subject')
        totp = pyotp.TOTP(secret)
        if int(totp.now()) != dto.factor:
            raise self.InvalidFactor(dto.using)

    def _get_method(self, factor):
        assert factor.using in ('otp',)
        return getattr(self, f'_authenticate_{factor.using}')
