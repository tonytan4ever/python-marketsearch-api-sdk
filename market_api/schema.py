
from marshmallow import Schema, fields


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
