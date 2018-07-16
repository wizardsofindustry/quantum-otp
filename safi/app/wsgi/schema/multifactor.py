"""The validation schema for ``#/components/schema/MultiFactor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema

from .factor import Factor


class MultiFactor(sq.schema.Schema):
    """Specifies a set of authentication Factors in order to establish the
    identity of a Subject.
    """

    #: A Global Subject Identifier (GSID) specifying the Subject to which
    #: this Factor is applicable.
    gsid = sq.schema.fields.UUID(
        required=True,
        allow_none=False
    )

    #: The Factors to use in establishing the identity of the Subject
    #: specified by `gsid`. The `gsid` member on individual Factor
    #: instances is ignored.
    factors = sq.schema.fields.Nested(
        nested=Factor(many=True, exclude=['gsid']),
        required=True,
        allow_none=False
    )


#pylint: skip-file
