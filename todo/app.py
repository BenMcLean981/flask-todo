"""Module for application factory"""
from flask import Flask

from todo.database import db
from todo.config import Config, ProductionConfig

from todo.home.views import home_blueprint
from todo.user.views import user_blueprint
from todo.task.views import task_blueprint


def create_app(config_object: Config = ProductionConfig()) -> Flask:
    """Application factory"""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_object)

    _register_blueprints(app)
    _register_database(app)
    _register_jinja_filters(app)

    return app


def _register_database(app: Flask) -> None:
    """Register any extensions such as the database"""
    db.init_app(app)

    with app.app_context():
        db.create_all()


def _register_blueprints(app: Flask) -> None:
    """Register each blueprint"""

    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)


def _register_jinja_filters(app: Flask) -> None:
    """Register jinja filters for templates"""
