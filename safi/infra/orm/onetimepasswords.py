""""Declares a Python object mapping to the ``onetimepasswords`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class OneTimePassword(Relation):
    """Stores AES-256 GCM encypted shared secrets for Subjects maintained
    by a Quantum system.
    """

    __tablename__ = 'onetimepasswords'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        primary_key=True,
        nullable=False
    )

    #: Specifies the Natural Subject Identifier (GSID), naturaly
    #: identififying the Subject. This identifier is used for display
    #: purposes in client applications only.
    nsid = sqlalchemy.Column(
        sqlalchemy.String,
        name='nsid',
        nullable=False
    )

    #: The date/time at which the One-Time Password (OTP) was generated,
    #: in milliseconds since the UNIX epoch.
    generated = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        name='generated',
        nullable=False
    )

    #: Declares the type of OTP. Allowed values are C(ounter) or
    #: T(ime-based).
    kind = sqlalchemy.Column(
        sqlalchemy.String,
        name='kind',
        nullable=False,
        default='T'
    )

    #: A hex representation of the AES-256 encrypted shared secret.
    secret = sqlalchemy.Column(
        sqlalchemy.String,
        name='secret',
        nullable=False
    )

    #: For counter-based OTPs, the current counter value. For time-based
    #: OTPs, the interval.
    counter = sqlalchemy.Column(
        sqlalchemy.Integer,
        name='counter',
        nullable=False
    )

    #: A human-readable description of the OTP issuer.
    issuer = sqlalchemy.Column(
        sqlalchemy.String,
        name='issuer',
        nullable=False
    )

    #: Indicates if the TOTP is enabled for this **Subject**.
    enabled = sqlalchemy.Column(
        sqlalchemy.String,
        name='enabled',
        nullable=False,
        default=False
    )


# pylint: skip-file
