import os
import unittest
from unittest.mock import MagicMock

from market_api.market_api import MarketAPI
from market_api.schema import GetVinHistoryOutputSchema
import json

test_vin_non_validate_response = ""
file = open("tests/mock.json", mode="r")
data = file.read()
file.close()
json_data = json.loads(data)


class MarketAppPagenationTestCase(unittest.TestCase):

    def test_get_vin_history_with_pagination(self):

        token = os.getenv('API_TOKEN')
        client = MarketAPI(token)

        vins = {"1FTEW1EF1FFA67753": 6, }

        for vin, page_limit in vins.items():
            for count in range(1, page_limit+1):
                client.get_vin_history = MagicMock(return_value=json_data)
                api_response = client.get_vin_history(vin=vin, page=count)

                assert len(api_response) != 0

                if count != page_limit:
                    assert len(api_response) == 50


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)
