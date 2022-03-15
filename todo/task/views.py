"""Set of views for the tasks module"""

from typing import Union

from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    url_for,
)
from flask_login import current_user

from todo.task.forms import NewTaskForm

from .models import Task

task_blueprint = Blueprint("task", __name__, template_folder="templates")


def ensure_login() -> Union[None, Response]:
    """
    Helper to ensure the user is logged in
    otherwise send them to the login screen
    """
    if not current_user.is_authenticated:
        flash("You must be logged in to see this page.", "danger")
        return redirect(url_for("user.view_sign_in"))


def get_task_view(form: NewTaskForm = NewTaskForm()) -> str:
    """Helper to return common view to PUT and GET methods"""
    tasks = Task.get_all()
    # alternatively we could query for complete and incomplete respectively.
    # but I believe doing one query and then a filter will be quicker

    incomplete_tasks = [t for t in tasks if not t.completed]
    completed_tasks = [t for t in tasks if t.completed]

    return render_template(
        "task_list.html",
        incomplete_tasks=incomplete_tasks,
        completed_tasks=completed_tasks,
        form=form,
    )


@task_blueprint.route("/task", methods=["GET"])
def view_task_list():
    """View all tasks, and create tasks as required"""
    send_to_login = ensure_login()
    if send_to_login:
        return send_to_login
    else:
        return get_task_view()


@task_blueprint.route("/task", methods=["POST"])
def create_task():
    """Creates a task based on form input"""
    send_to_login = ensure_login()
    if send_to_login:
        return send_to_login
    else:
        form = NewTaskForm()
        if form.validate_on_submit():
            Task.create(form.title.data, form.description.data)

        return get_task_view(form)


@task_blueprint.route("/task/complete/<int:task_id>", methods=["GET"])
def complete_task(task_id: int):
    """Modify task_id to have completed attribute set to True"""
    send_to_login = ensure_login()
    if send_to_login:
        return send_to_login
    else:
        task = Task.complete(task_id)

        flash(f'Good job! You completed "{task.title}"', "success")
        return redirect(url_for("task.view_task_list"))


@task_blueprint.route("/task/delete/<int:task_id>", methods=["GET"])
def delete_task(task_id: int):
    """Remove task with associated ID from the database."""
    send_to_login = ensure_login()
    if send_to_login:
        return send_to_login
    else:
        old_task = Task.delete(task_id)

        flash(f'You deleted "{old_task.title}"', "info")
        return redirect(url_for("task.view_task_list"))
