"""User blueprint for anything related to the user"""

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user


from todo.user.forms import SignInForm, SignUpForm

from .models import User
from ..database import db

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/user/sign-in", methods=["GET"])
def view_sign_in():
    """Form page to handle signing in"""
    form = SignInForm()

    return render_template("sign-in.html", form=form)


@user_blueprint.route("/user/sign-in", methods=["POST"])
def sign_in():
    """Handle sign-in form submission"""
    form = SignInForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is None:
            flash("Sign-in unsuccessful, no user with e-mail.", "danger")
            return render_template("sign-in.html", form=form)
        elif not user.authenticate(form.password.data):
            flash("Sign-in unsuccessful, password incorrect!", "danger")
            return render_template("sign-in.html", form=form)
        else:
            login_user(user, remember=form.remember.data)
            return redirect(
                url_for(
                    "task.view_task_list",
                )
            )
    else:
        return render_template("sign-in.html", form=form)


@user_blueprint.route("/user/sign-up", methods=["GET"])
def view_sign_up():
    """Form page to show signing up"""
    form = SignUpForm()
    return render_template("sign-up.html", form=form)


@user_blueprint.route("/user/sign-up", methods=["POST"])
def sign_up():
    """Handle sign-up form submission"""
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            user = User.create_user(form.email.data, form.password.data)
            login_user(user, remember=form.remember.data)
            return redirect(url_for("task.view_task_list"))
        except ValueError:
            flash(
                "Sign-up unsuccessful, user with that e-mail already exists.",
                "danger",
            )
            return render_template("sign-up.html", form=form)

    else:
        return render_template("sign-up.html", form=form)


@user_blueprint.route("/user/sign-out", methods=["GET"])
def sign_out():
    """Handle user sign-out."""
    logout_user()
    return redirect(url_for("home.view_home"))
