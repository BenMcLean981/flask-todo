"""Set of views for the tasks module"""

from flask import Blueprint, render_template

from .models import Task
from ..database import db

task_blueprint = Blueprint("task", __name__, template_folder="templates")


@task_blueprint.route("/task/<int:task_id>", methods=["GET"])
def view_task(task_id: int):
    """View to show an individual task"""

    task = db.session.query(Task).filter_by(task_id=task_id).first()

    return render_template("task.html", task=task)
