# coding=utf-8
from flask_testing import TestCase

from market_api import create_app


class BaseTestCase(TestCase):
    """
    Base class for any resource-related test requiring the flask app
    """
    def create_app(self):
        return create_app('market_api.config.TestConfig')

