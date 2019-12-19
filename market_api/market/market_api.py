import requests

BASE_URL = "http://api.marketcheck.com"
API_URL = "/v1/history/2FMGK5D81EBD14330"

class MarketAPI(object):

    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_VIN_history(self):

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

        response = requests.request("GET", BASE_URL + API_URL,  headers=headers, params=querystring)
        return response.json()
