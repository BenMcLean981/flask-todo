"""Models relating to task"""

from typing import TYPE_CHECKING


from ..database import (
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

    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    user: "User" = relationship("User", back_populates="tasks", lazy=False)  # type: ignore

    def __repr__(self) -> str:
        return f"Task: id={self.task_id}, title={self.title}"
