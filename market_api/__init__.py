# coding=utf-8
import json
import logging
from logging import config as logging_config
import os

from flask import Flask
from .api import API


LOGGER = logging.getLogger(__name__)

def create_app(app_settings=None):

    app = Flask(
        __name__
    )

    app_settings = app_settings or \
        os.getenv('APP_SETTINGS') or \
        'market_api.config.TestConfig'

    LOGGER.info('creating app using settings %s', app_settings)
    app.config.from_object(app_settings)

    API.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app}

    @app.errorhandler(Exception)
    def handle_exception(e):
        LOGGER.exception(e)

    return app
