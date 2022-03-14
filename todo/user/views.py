"""User blueprint for anything related to the user"""

from flask import Blueprint, render_template

from todo.user.models import User
from todo.database import db

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def view_user(user_id: int):
    """Simple user viewing page."""

    user = db.session.query(User).filter_by(user_id=user_id).first()

    return render_template("user.html", user=user)
