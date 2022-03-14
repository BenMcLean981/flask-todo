"""Collection of different configuration objects for flask"""
import secrets


class Config:
    """Base configuration object"""

    SECRET_KEY = secrets.token_hex()
    PORT = 5000
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Configuration for development"""

    ENV = "development"
    SECRET_KEY = "SECRET_KEY"
    PORT = 5001
    DEBUG = True


class ProductionConfig(Config):
    """Configuration for production"""

    ENV = "production"


class TestConfig(Config):
    """Configuration for test"""

    ENV = "test"
    DEBUG = False  # we want our tests to reflect production
    TESTING = True
