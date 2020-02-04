import requests

from marshmallow import ValidationError

from market_api.market import MarketAPIBase
from market_api.schema import GetVinHistoryOutputSchema, VinInputSchema
from market_api.object import VinHistoryOutput


class MarketAPI(MarketAPIBase):

    def get_vin_history(self, vin, page=1):
        """
        Pull online listing history for a VIN from Marketcheck's historical
        database that hosts data extracted from over 900M VDP pages since Jan
        2013 till date and growing at a rate of about 30-40M unique listings
        a month from all over the web. This API will return only recent 50
        records/listings for a VIN. Results are sorted on status_date
        """
        try:
            VinInputSchema().load({"vin": vin})
        except ValidationError:
            return 'Vin is not valid: {}'.format(
                vin
            )

        api_url = "/history/{vin}".format(vin=vin)
        request_url = '{base_url}{api_url}'.format(
            base_url=self.base_url,
            api_url=api_url
        )
        req_query = self.get_querystring()
        req_query['page'] = page
        response = requests.request("GET",
                                    request_url,
                                    headers=self.headers,
                                    params=req_query)

        schema = GetVinHistoryOutputSchema()
        result = []
        for history in response.json():
            result_entry = schema.load(history)
            result.append(result_entry)
        return result
