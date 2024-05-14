from marshmallow import fields

from pynamodb import attributes

from marshmallow_pynamodb import fields as custom_fields

PYNAMODB_TYPE_MAPPING = {
    attributes.NumberAttribute: fields.Number,
    attributes.JSONAttribute: fields.Raw,
    attributes.UnicodeAttribute: fields.String,
    attributes.BooleanAttribute: fields.Boolean,
    attributes.UTCDateTimeAttribute: fields.DateTime,
    attributes.MapAttribute: custom_fields.PynamoNested,
    attributes.ListAttribute: fields.List,
    attributes.NullAttribute: fields.Raw,
    attributes.UnicodeSetAttribute: custom_fields.UnicodeSet,
    attributes.NumberSetAttribute: custom_fields.NumberSet
}

try:
    import pynamodb_attributes
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.FloatAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.IntegerAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.IntegerSetAttribute] = custom_fields.NumberSet,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.IntegerDateAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.IntegerEnumAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.UnicodeDelimitedTupleAttribute] = fields.String,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.UnicodeEnumAttribute] = fields.String,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimedeltaAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimedeltaMsAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimedeltaUsAttribute] = fields.Number,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimestampAttribute] = fields.DateTime,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimestampMsAttribute] = fields.DateTime,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.TimestampUsAttribute] = fields.DateTime,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.UUIDAttribute] = fields.String,
    PYNAMODB_TYPE_MAPPING[pynamodb_attributes.UnicodeDatetimeAttribute] = fields.DateTime,
except ImportError:
    pass


def attribute2field(attribute):
    try:
        pynamodb_type = type(attribute)
        field = PYNAMODB_TYPE_MAPPING[pynamodb_type]
    except KeyError:
        pynamodb_type = type(pynamodb_type)
        field = PYNAMODB_TYPE_MAPPING[pynamodb_type]

    return field
