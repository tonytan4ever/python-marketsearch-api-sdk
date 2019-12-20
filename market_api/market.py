import settings

class Market(object):

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = settings.BASE_URL