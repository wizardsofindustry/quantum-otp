"""The validation schema for ``#/components/schema/SharedSecret`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class SharedSecret(sq.schema.Schema):

    #: A link that is recognized by client OTP applications to import the
    #: shared secret.
    link = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
