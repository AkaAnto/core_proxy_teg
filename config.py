import os
from dotenv import dotenv_values
basedir = os.path.abspath(os.path.dirname(__file__))

env_vars = dotenv_values(".env")


class Config(object):
    DEBUG = env_vars['DEBUG']
    TESTING = env_vars['TESTING']
    CSRF_ENABLED = True
    SECRET_KEY = env_vars['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = env_vars['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_SETTINGS = env_vars['APP_SETTINGS']

    @staticmethod
    def show_config():
        config_messagge = "Debug=%s - Testing=%s" % (Config.DEBUG, Config.TESTING)
        print("Config loaded", config_messagge)


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True