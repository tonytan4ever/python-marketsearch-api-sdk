import settings


class MarketAPIBase(object):

    def __init__(self, api_token=None):
        self.api_token = api_token
        self.base_url = settings.BASE_URL

    @property
    def headers(self):
        return {
            'Host': "marketcheck-prod.apigee.net",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

    def get_querystring(self):
        return {
            "api_key": self.api_token,
        }
