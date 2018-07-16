"""The validation schema for ``#/components/schema/Factor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema

from .onetimepasswordfactor import OneTimePasswordFactor
from .personalidentificationnumberfactor import PersonalIdentificationNumberFactor


class Factor(sq.schema.Schema):
    """Describes the authentication Factor specified by `using` for the
    Subject identified by `gsid`.
    """

    #: A Global Subject Identifier (GSID) specifying the Subject to which
    #: this Factor is applicable.
    gsid = sq.schema.fields.UUID(
        required=True,
        allow_none=False
    )

    #: Specifies the type of authentication factor that is contained in
    #: the Factor object.
    using = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    __oneof__ = [
        OneTimePasswordFactor,
        PersonalIdentificationNumberFactor
    ]


#pylint: skip-file
