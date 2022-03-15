"""Set of views for the tasks module"""

from datetime import datetime
from os import abort

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

from todo.task.forms import NewTaskForm

from .models import Task
from ..database import db

task_blueprint = Blueprint("task", __name__, template_folder="templates")


@task_blueprint.route("/task", methods=["GET", "POST"])
def view_task_list():
    """View all tasks"""

    if not current_user.is_authenticated:
        flash("You must be logged in to see this page.", "danger")
        return redirect(url_for("user.view_sign_in"))

    # we don't paginate because users shouldn't have THAT
    # many tasks

    form = NewTaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            created=datetime.utcnow(),
            user_id=current_user.user_id,
        )
        db.session.add(new_task)
        db.session.commit()

    incomplete_tasks = Task.query.filter_by(
        user_id=current_user.user_id, completed=False
    ).all()
    return render_template(
        "task_list.html", incomplete_tasks=incomplete_tasks, form=form
    )


@task_blueprint.route("/task/complete/<int:task_id>", methods=["GET"])
def complete_task(task_id: int):
    task = Task.query.filter_by(task_id=task_id).first()
    if task is None:
        abort("Task does not exist!")

    task.completed = True
    flash(f'Good job! You completed "{task.title}"')

    return redirect(url_for("task.view_task_list"))
