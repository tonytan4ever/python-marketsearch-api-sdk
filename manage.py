# coding=utf-8
import csv
from os.path import dirname, join, realpath
from flask.cli import FlaskGroup

from market_api import create_app


app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()
