"""Module for application factory"""
from flask import Flask

from todo.config import Config, ProductionConfig


def create_app(config_object: Config = ProductionConfig()) -> Flask:
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config_object)

    _register_extensions(app)
    _register_blueprints(app)
    _register_jinja_filters(app)

    return app


def _register_extensions(app: Flask) -> None:
    """Register any extensions such as the database"""


def _register_blueprints(app: Flask) -> None:
    """Register each blueprint"""


def _register_jinja_filters(app: Flask) -> None:
    """Register jinja filters for templates"""
