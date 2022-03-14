"""Models relating to task"""

from ..database import Boolean, Column, DateTime, Integer, Model, String, Text, Date


class Task(Model):
    """Todo model representing a task todo"""

    task_id = Column(Integer, primary_key=True)
    title = Column(String(320), index=True, nullable=False)
    description = Column(Text, nullable=True)

    created = Column(DateTime, nullable=False)
    due = Column(Date, nullable=True)

    completed = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"Task: id={self.task_id}, title={self.title}"
