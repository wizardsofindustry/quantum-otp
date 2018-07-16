"""The validation schema for ``#/components/schema/PasswordFactor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class PasswordFactor(sq.schema.Schema):
    """Describes a generic password factor for the Subject identified by
    `gsid`.
    """

    #: The shared secret between the client and the SAFI service.
    factor = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
