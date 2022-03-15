"""Set of forms for the task module."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NewTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3)])
    description = TextAreaField("Description")
    submit = SubmitField("Create Task")
