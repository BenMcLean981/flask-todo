"""Set of models for the user blueprint"""
from typing import TYPE_CHECKING, List
from flask_login import UserMixin

from ..database import (
    Column,
    Integer,
    Model,
    String,
    Text,
    relationship,
)


if TYPE_CHECKING:
    from ..task.models import Task


class User(UserMixin, Model):
    """User model"""

    user_id = Column(Integer, primary_key=True)
    email = Column(String(320), nullable=False, unique=True)
    # supposedly 320 is the maximum length of an e-mail address

    password_hash = Column(Text, nullable=False)
    tasks: List["Task"] = relationship(
        "Task", order_by="Task.task_id", back_populates="user", lazy=False
    )

    def __repr__(self):
        return f"User: id={self.user_id}, e-mail={self.email}"

    def get_id(self) -> int:
        """
        Getter for UserMixin

        I don't like to use id because it is
        a builtin function, so instead I choose
        property names like user_id or task_id.
        As a consequence, UserMixin which expects
        an "id" property must be told how to get it
        """
        return self.user_id
