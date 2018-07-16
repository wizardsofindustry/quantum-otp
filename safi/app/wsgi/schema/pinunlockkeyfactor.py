"""The validation schema for ``#/components/schema/PinUnlockKeyFactor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class PinUnlockKeyFactor(sq.schema.Schema):
    """Describes a PIN Unlock Key (PUK) factor for the Subject identified
    by `gsid`.
    """

    #: The PIN Unlock Key (PUK) that the Subject may provide to unlock a
    #: blocked Personal Identification Number (PIN).
    factor = sq.schema.fields.Integer(
        required=True,
        allow_none=False
    )


#pylint: skip-file
