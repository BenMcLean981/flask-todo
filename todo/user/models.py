"""Set of models for the user blueprint"""
from typing import TYPE_CHECKING, List

from ..database import Column, Integer, Model, String, Text, relationship

if TYPE_CHECKING:
    from ..task.models import Task


class User(Model):
    """User model"""

    user_id = Column(Integer, primary_key=True)
    email = Column(String(320), nullable=False)
    # supposedly 320 is the maximum length of an e-mail address

    password_hash = Column(Text, nullable=False)
    tasks: List["Task"] = relationship("Task", order_by="Task.task_id", back_populates="user", lazy=False)  # type: ignore

    def __repr__(self):
        return f"User: id={self.user_id}, e-mail={self.email}"
