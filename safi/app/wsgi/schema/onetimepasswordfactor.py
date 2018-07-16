"""The validation schema for ``#/components/schema/OneTimePasswordFactor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class OneTimePasswordFactor(sq.schema.Schema):
    """Describes a One-Time Password (OTP) factor for the Subject
    identified by `gsid`.
    """

    #: The One-Time Password (OTP) generated by the client application
    #: based on the shared secret.
    factor = sq.schema.fields.Integer(
        required=True,
        allow_none=False
    )


#pylint: skip-file