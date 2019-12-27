import os

from unittest import TestCase, mock

from market_api.market_api import MarketAPI


class MarketAppTestCase(TestCase):

    def test_get_vin_history(self):

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

        with mock.patch('market_api.market_api.MarketAPI.get_vin_history', return_value=vin_history):
            token = os.getenv('API_TOKEN')
            client = MarketAPI(token)

            response = client.get_vin_history('2FMGK5D81EBD14330')
            self.assertListEqual(list(response[0].keys()), [
                'id',
                'price',
                'miles',
                'data_source',
                'vdp_url',
                'seller_type',
                'inventory_type',
                'trim_r',
                'last_seen_at',
                'last_seen_at_date',
                'scraped_at',
                'scraped_at_date',
                'first_seen_at',
                'first_seen_at_date',
                'source',
                'seller_name',
                'city',
                'state',
                'zip',
                'status_date',
            ])
            self.assertTrue(len(response) > 0)
