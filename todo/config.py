"""Collection of different configuration objects for flask"""
import secrets


class Config:
    """Base configuration object"""

    SECRET_KEY = secrets.token_hex()
    PORT = 5000
    DEBUG = False
    TESTING = False
    DATABASE_PATH = "../todo.sqlite"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """Getter for database uri"""
        return "sqlite:///" + self.DATABASE_PATH


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

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """Getter for database uri"""
        return "sqlite:///:memory:"
