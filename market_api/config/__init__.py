# coding=utf-8
import os


class BaseConfig:
    TESTING = False
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'Development'


class TestConfig(BaseConfig):
    DEBUG = True
    ENV = 'Test'
    TESTING = True
