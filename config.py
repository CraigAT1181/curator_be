import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}