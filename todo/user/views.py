"""User blueprint for anything related to the user"""

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user

from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)
from todo.user.forms import SignInForm, SignUpForm

from .models import User
from ..database import db

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def view_user(user_id: int):
    """Simple user viewing page."""

    user = User.query.filter_by(user_id=user_id).first()

    return render_template("user.html", user=user)


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
        user: User = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("Sign-in unsuccessful, no user with e-mail.", "danger")
            return render_template("sign-in.html", form=form)
        elif not check_password_hash(user.password_hash, form.password.data):
            flash("Sign-in unsuccessful, password incorrect!", "danger")
            return render_template("sign-in.html", form=form)
        else:
            login_user(user, remember=form.remember.data)
            return redirect(url_for("user.view_user", user_id=user.user_id))
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
        email = form.email.data
        password = form.password.data
        # bcrypt is an alternative that is supposedly more
        # secure, but not necessary for this project
        password_hash = generate_password_hash(password)

        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            flash(
                "Sign-up unsuccessful, user with that e-mail already exists.",
                "danger",
            )
            return render_template("sign-up.html", form=form)
        else:
            user = User(email=email, password_hash=password_hash)  # type: ignore
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=form.remember.data)
            return redirect(url_for("user.view_user", user_id=user.user_id))
    else:
        return render_template("sign-up.html", form=form)
