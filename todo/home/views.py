"""Home blueprint with base page."""
from flask import Blueprint, render_template

home_blueprint = Blueprint("home", __name__, template_folder="templates")


@home_blueprint.route("/")
def view_home():
    """Base view"""
    return render_template("home.html")
