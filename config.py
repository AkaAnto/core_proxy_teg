import os
from dotenv import dotenv_values
basedir = os.path.abspath(os.path.dirname(__file__))

env_vars = dotenv_values(".env")
is_prod = os.getenv('USE_PRODUCTION', False)
if is_prod:
    env_vars['USE_DATABASE'] = os.getenv('USE_DATABASE', None)


def load_database_config():
    database_vars = {}
    selected_database = [env_vars['USE_DATABASE']]
    if 'oracle' in selected_database:
        database_vars = dotenv_values(".env.oracle")
    if 'mysql' in selected_database:
        database_vars = dotenv_values(".env.mysql")
    if 'postgres' in selected_database:
        database_vars = dotenv_values(".env.postgres")
    if 'sqlserver' in selected_database:
        database_vars = dotenv_values(".env.sqlserver")
    if is_prod:
        database_vars['DATABASE_URL'] = os.getenv('DATABASE_URL', None)
    return database_vars


database_vars = load_database_config()


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = env_vars['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = database_vars['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_SETTINGS = env_vars['APP_SETTINGS']

    @staticmethod
    def show_config():
        config_message = "Debug=%s - Testing=%s Datbase Engine=%s" % (Config.DEBUG, Config.TESTING. Config.SQLALCHEMY_DATABASE_URI)
        print("Config loaded", config_message)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True