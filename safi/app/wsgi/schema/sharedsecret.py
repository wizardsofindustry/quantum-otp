"""The validation schema for ``#/components/schema/SharedSecret`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class SharedSecret(sq.schema.Schema):

    #: The shared secret used to generate TOTP codes.
    secret = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: A link that is recognized by client OTP applications to import the
    #: shared secret.
    link = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: A base64-encoded PNG image that can be read by TOTP client
    #: applications.
    qrcode = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
