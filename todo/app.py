"""Module for application factory"""
from typing import Union
from flask import Flask
from flask_login import LoginManager

from todo.database import db
from todo.config import Config, ProductionConfig

from todo.home.views import home_blueprint
from todo.user.models import User
from todo.user.views import user_blueprint
from todo.task.views import task_blueprint


def create_app(config_object: Config = ProductionConfig()) -> Flask:
    """Application factory"""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_object)

    _register_blueprints(app)
    _register_database(app)
    _register_login_manager(app)

    return app


def _register_database(app: Flask) -> None:
    """Register any extensions such as the database"""
    db.init_app(app)

    with app.app_context():
        db.create_all()


def _register_login_manager(app: Flask) -> None:
    """Register the login manager"""
    login_manager = LoginManager()
    login_manager.login_view = "user.view_sign_in"
    login_manager.init_app(app)

    @login_manager.user_loader
    def _load_user(user_id: str) -> Union[User, None]:
        return User.query.get(int(user_id))


def _register_blueprints(app: Flask) -> None:
    """Register each blueprint"""

    app.register_blueprint(home_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)
