import os
import unittest

import time
from market_api.market_api import MarketAPI


class MarketAppPagenationTestCase(unittest.TestCase):

    def test_get_vin_history_with_pagination(self):
        
        token = os.getenv('API_TOKEN')
        client = MarketAPI(token)

        vins = {"1FTEW1EF1FFA67753":6,}

        for vin,page_limit in vins.items():
            for count in range(1,page_limit+1):
                time.sleep(3)
                api_response = client.get_vin_history(vin=vin, page=count)
                last_seen_at_ary = []
                
                assert len(api_response) != 0
            
                if count != page_limit:
                    assert len(api_response) == 50
        