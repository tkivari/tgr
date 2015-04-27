class Config(object):
  DEBUG = False
  TESTING = False

class ProductionConfig(Config):


class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  TESTING = True