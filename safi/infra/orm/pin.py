""""Declares a Python object mapping to the ``pin`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class PIN(Relation):
    """Stores a Personal Identification Number (PIN) and tracks the failed
    attempts.
    """

    __tablename__ = 'pin'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        primary_key=True,
        nullable=False
    )

    #: The Personal Identification Number (PIN).
    pin = sqlalchemy.Column(
        sqlalchemy.String,
        name='pin',
        nullable=False
    )

    #: Maintains the number of failed attempts. The system may choose to
    #: block a PIN code if the number of failed attempts exceeds an
    #: arbitrary limit. This counter is reset on succesful PIN
    #: authentication.
    failed = sqlalchemy.Column(
        sqlalchemy.Integer,
        name='failed',
        nullable=False,
        default=0
    )

    #: Specifies the date/time at which the PIN was last used, in
    #: milliseconds since the UNIX epoch. This also registers failed
    #: attempts.
    last_used = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        name='last_used',
        nullable=False,
        default=0
    )


# pylint: skip-file
