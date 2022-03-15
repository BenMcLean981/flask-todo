"""Models relating to task"""

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from flask_login import current_user


from ..database import (
    db,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Model,
    String,
    Text,
    Date,
    relationship,
)

if TYPE_CHECKING:
    from todo.user.models import User


class Task(Model):
    """Todo model representing a task todo"""

    task_id = Column(Integer, primary_key=True)
    title = Column(String(320), index=True, nullable=False)
    description = Column(Text, nullable=True)

    created = Column(DateTime, nullable=False)
    due = Column(Date, nullable=True)

    completed = Column(Boolean, nullable=False, default=False)

    user_id = Column(
        Integer, ForeignKey("user.user_id"), nullable=False, index=True
    )
    user: "User" = relationship("User", back_populates="tasks", lazy=False)  # type: ignore

    def __repr__(self) -> str:
        return f"Task: id={self.task_id}, title={self.title}"

    @staticmethod
    def complete(task_id: int) -> "Task":
        """Complete task with given id in the database"""
        task = Task.query.filter_by(task_id=task_id).first()
        if task is None:
            raise ValueError("No such task in database with task_id={task_id}")

        task.completed = True
        task.completed_at = datetime.utcnow()
        db.session.commit()

        return task

    @staticmethod
    def delete(task_id: int) -> "Task":
        """Delete task with given id in the database"""
        task = Task.query.filter_by(task_id=task_id).first()
        if task is None:
            raise ValueError("No such task in database with task_id={task_id}")

        db.session.delete(task)
        db.session.commit()

        return task

    @staticmethod
    def create(
        title: str, description: str, due: Union[datetime, None] = None
    ) -> "Task":
        """Task factory"""
        new_task = Task(
            title=title,
            description=description,
            created=datetime.utcnow(),
            user_id=current_user.user_id,
            due=due,
        )
        db.session.add(new_task)
        db.session.commit()

        return new_task

    @staticmethod
    def get_all() -> List["Task"]:
        """Helper to return all tasks"""
        return Task.query.filter_by(user_id=current_user.user_id).all()
