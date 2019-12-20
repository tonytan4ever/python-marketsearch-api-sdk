import requests

from market_api.market import Market

API_URL = "/v1/history/2FMGK5D81EBD14330"

class MarketAPI(Market):

    def get_VIN_history(self):
        """
        Pull online listing history for a VIN from Marketcheck's historical database that
        hosts data extracted from over 900M VDP pages since Jan 2013 till date and growing
        at a rate of about 30-40M unique listings a month from all over the web.
        This API will return only recent 50 records/listings for a VIN. Results are sorted on status_date
        """
        api_token = self.api_key
        querystring = {
                        "api_key": api_token,
                        }

        headers = {
            'Host': "marketcheck-prod.apigee.net",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", self.base_url + API_URL,  headers=headers, params=querystring)
        return response.json()
