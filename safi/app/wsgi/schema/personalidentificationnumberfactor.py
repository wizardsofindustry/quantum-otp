"""The validation schema for ``#/components/schema/PersonalIdentificationNumberFactor`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class PersonalIdentificationNumberFactor(sq.schema.Schema):
    """Describes a Personal Identification Number (PIN) factor for the
    Subject identified by `gsid`.
    """

    #: The Personal Identification Number (PIN) provisioned to the
    #: Subject.
    factor = sq.schema.fields.Integer(
        required=True,
        allow_none=False
    )


#pylint: skip-file
