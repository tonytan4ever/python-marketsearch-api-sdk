import os

from unittest import TestCase, mock

from market_api.market_api import MarketAPI
from market_api.schema import GetVinHistoryOutputSchema
import time

class MarketAppTestCase(TestCase):

    def test_get_vin_history(self):

        schema = GetVinHistoryOutputSchema()
        vin_history = [
            {
                'id': '2FMGK5D81EBD14330-c44611d6-764b-406e-85bd-752d5f3b24f8',
                'price': 21800,
                'miles': 75514,
                'data_source': 'mc',
                'vdp_url': 'https://www.lithia.com/used/Ford/2014-Ford-Flex-medford-or-1f945c690a0e0aea23fb4458c35c15ac.htm',
                'seller_type': 'dealer',
                'inventory_type': 'used',
                'trim_r': 'Limited',
                'last_seen_at': 1525905680,
                'last_seen_at_date': '2018-05-09T22:41:20.000Z',
                'scraped_at': 1525888700,
                'scraped_at_date': '2018-05-09T17:58:20.000Z',
                'first_seen_at': 1525888700,
                'first_seen_at_date': '2018-05-09T17:58:20.000Z',
                'source': 'www.lithia.com',
                'seller_name': 'lithia auto stores',
                'city': 'Lodi',
                'state': 'CA',
                'zip': '95240',
                'status_date': 1525905680
            },
            {
                'id': '2FMGK5D81EBD14330-86c2309b-4bb9-4f30-a17a-20e5e197c04a',
                'price': 21800,
                'miles': 75514,
                'data_source': 'mc',
                'vdp_url': 'https://www.lumeiauto.com/used/Ford/2014-Ford-Flex-1f945c690a0e0aea23fb4458c35c15ac.htm',
                'seller_type': 'dealer',
                'inventory_type': 'used',
                'trim_r': 'Limited',
                'last_seen_at': 1525877052,
                'last_seen_at_date': '2018-05-09T14:44:12.000Z',
                'scraped_at': 1525458641,
                'scraped_at_date': '2018-05-04T18:30:41.000Z',
                'first_seen_at': 1525458641,
                'first_seen_at_date': '2018-05-04T18:30:41.000Z',
                'source': 'www.lumeiauto.com',
                'seller_name': 'lumei auto',
                'city': 'Pasadena',
                'state': 'CA',
                'zip': '91101',
                'status_date': 1525877052
            }
        ]
        vin_history = [
            schema.load(history) for history in vin_history
        ]

        with mock.patch('market_api.market_api.MarketAPI.get_vin_history', return_value=vin_history):
            token = os.getenv('API_TOKEN')
            client = MarketAPI(token)
            vin = '2FMGK5D81EBD14330'
            response = client.get_vin_history(vin)
            first_vin_history = response[0]
            self.assertEqual(
                first_vin_history.id, vin_history[0].id
            )
            self.assertEqual(
                first_vin_history.price, vin_history[0].price
            )
            self.assertTrue(len(response) > 0)

    def test_vin_non_validate(self):
        token = os.getenv('API_TOKEN')
        client = MarketAPI(token)
        vin = '2FMGK5D81EBD1433'
        response = client.get_vin_history(vin)
        self.assertEqual(response, 'Vin is not valid: {}'.format(vin))
        
        
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
