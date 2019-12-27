import requests

from market_api.market import MarketAPIBase
from market_api.schema import GetVinHistoryOutputSchema

class MarketAPI(MarketAPIBase):

    def get_vin_history(self, vin):
        """
        Pull online listing history for a VIN from Marketcheck's historical
        database that hosts data extracted from over 900M VDP pages since Jan
        2013 till date and growing at a rate of about 30-40M unique listings
        a month from all over the web. This API will return only recent 50
        records/listings for a VIN. Results are sorted on status_date
        """
        api_url = "/history/{vin}".format(vin=vin)
        request_url = '{base_url}{api_url}'.format(
            base_url=self.base_url,
            api_url=api_url
        )
        response = requests.request("GET",
                                    request_url,
                                    headers=self.headers,
                                    params=self.get_querystring())
        schema = GetVinHistoryOutputSchema(many=True)
        result = schema.dump(response.json())
        return result

