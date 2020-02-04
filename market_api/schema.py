import re

from marshmallow import Schema, ValidationError, fields, post_load
from market_api.object import VinHistoryOutput


def validate_vin(vin):
    if re.match(r'^[A-HJ-NPR-Za-hj-npr-z\d]{17}', vin):
        return True
    else:
        raise ValidationError("Vin is not valid!")


class GetVinHistoryOutputSchema(Schema):
    id = fields.String(required=True)
    price = fields.Integer()
    miles = fields.Integer(required=True)
    data_source = fields.String(required=True)
    vdp_url = fields.String(required=True)
    seller_type = fields.String(required=True)
    inventory_type = fields.String(required=True)
    trim_r = fields.String(required=True)
    last_seen_at = fields.Integer(required=True)
    last_seen_at_date = fields.String(required=True)
    scraped_at = fields.Integer(required=True)
    scraped_at_date = fields.String(required=True)
    first_seen_at = fields.Integer(required=True)
    first_seen_at_date = fields.String(required=True)
    source = fields.String(required=True)
    seller_name = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip = fields.String(required=True)
    status_date = fields.Integer(required=True)

    @post_load
    def make_history_entry(self, data, **kwargs):
        return VinHistoryOutput(**data)


class VinInputSchema(Schema):
    vin = fields.String(required=True, validate=validate_vin)
