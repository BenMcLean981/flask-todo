from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignInForm(FlaskForm):
    """Form to be used to sign in users"""

    email = StringField(
        "E-Mail",
        validators=[DataRequired(), Length(min=0, max=320), Email()],
    )
    password = StringField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class SignUpForm(FlaskForm):
    """Form to be used to sign up users"""

    email = StringField(
        "E-Mail",
        validators=[DataRequired(), Length(min=0, max=320), Email()],
    )
    password = StringField("Password", validators=[DataRequired()])
    confirm_password = StringField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign Up")
