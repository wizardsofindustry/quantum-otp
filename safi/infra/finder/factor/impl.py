"""Declares :class:`FactorFinder`."""
from ...orm import OneTimePassword
from .base import BaseFactorFinder


class FactorFinder(BaseFactorFinder):
    """Exposes an interface to lookup factors and their
    underlying secrets.
    """
    valid_factors = ('otp',)

    def get(self, gsid, using): 
        """Return a **Factor** of the type specified by string `using`
        for the **Subject** identified by the Global Subject Identifier
        (GSID) string `gsid`.
        """
        ciphertext = self.session.query(OneTimePassword.secret)\
            .filter(OneTimePassword.gsid == gsid)\
            .scalar()
        return self.cipher.decrypt(bytes.fromhex(ciphertext))\
            if ciphertext is not None else None
