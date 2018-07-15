"""Contains the base class for :class:`VerificationCtrl`."""
import ioc
from sq.ctrl import EndpointCtrl

class BaseVerificationCtrl(EndpointCtrl):
    """Generated by SG to serve as an abstract base class for:

        otp.app.ctrl.VerificationCtrl

    This class encapsulates external dependencies (such as the inversion-of-control
    requirements) and specifies the interface for the concrete implementation.
    """
    otp = ioc.class_property('OneTimePasswordService')

    async def post(self, request, *args, **kwargs):
        """This method specifies the signature for :meth:`VerificationCtrl.post()`
        and should be implemented in the following file:

            ./otp/ctrl/verification/impl.py
        """
        raise NotImplementedError("Subclasses must override this method.")


#pylint: skip-file
# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
