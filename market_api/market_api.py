import requests

from marshmallow import ValidationError

from market_api.market import MarketAPIBase
from market_api.schema import GetVinHistoryOutputSchema, VinInputSchema
from market_api.object import VinHistoryOutput


class MarketAPI(MarketAPIBase):

    def get_vin_history(self, vin):
        """
        Pull online listing history for a VIN from Marketcheck's historical
        database that hosts data extracted from over 900M VDP pages since Jan
        2013 till date and growing at a rate of about 30-40M unique listings
        a month from all over the web. This API will return only recent 50
        records/listings for a VIN. Results are sorted on status_date
        """
        try:
            vin_schema = VinInputSchema().load({"vin": vin})
        except ValidationError:
            return 'Vin is not valid: {}'.format(
                vin
            )

        api_url = "/history/{vin}".format(vin=vin)
        request_url = '{base_url}{api_url}'.format(
            base_url=self.base_url,
            api_url=api_url
        )
        response = requests.request("GET",
                                    request_url,
                                    headers=self.headers,
                                    params=self.get_querystring())
        outputs = []
        for history in response.json():
            vin_history = VinHistoryOutput(
                id=history['id'],
                price=history['price'] if 'price' in history else None,
                miles=history['miles'],
                data_source=history['data_source'],
                vdp_url=history['vdp_url'],
                seller_type=history['seller_type'],
                inventory_type=history['inventory_type'],
                trim_r=history['trim_r'],
                last_seen_at=history['last_seen_at'],
                last_seen_at_date=history['last_seen_at_date'],
                scraped_at=history['scraped_at'],
                scraped_at_date=history['scraped_at_date'],
                first_seen_at=history['first_seen_at'],
                first_seen_at_date=history['first_seen_at_date'],
                source=history['source'],
                seller_name=history['seller_name'],
                city=history['city'],
                state=history['state'],
                zip=history['zip'],
                status_date=history['status_date']
            )
            outputs.append(vin_history)

        schema = GetVinHistoryOutputSchema(many=True)
        result = schema.dump(outputs)
        return result

