import os
import unittest

from market_api.market_api import MarketAPI


class MarketAppTestCase(unittest.TestCase):

    def test_get_vin_history(self):
        token = os.getenv('API_TOKEN')
        client = MarketAPI(token)
        response = client.get_vin_history('2FMGK5D81EBD14330')
        self.assertListEqual(list(response[0].keys()), [
            'id',
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
