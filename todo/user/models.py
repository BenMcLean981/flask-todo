"""Set of models for the user blueprint"""
from typing import TYPE_CHECKING, List, Union
from flask_login import UserMixin

from werkzeug.security import check_password_hash, generate_password_hash

from ..database import (
    db,
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

    def authenticate(self, password: str) -> bool:
        """Authentication helper."""
        return check_password_hash(self.password_hash, password)

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

    def get_num_completed(self) -> int:
        """Helper to get the number of tasks the user has completed."""
        return sum([1 for t in self.tasks if t.completed])

    @staticmethod
    def get_by_email(email: str) -> Union["User", None]:
        """Simple helper to return the"""
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(email: str, password: str) -> "User":
        """Create user factory method."""
        # bcrypt is an alternative that is supposedly more
        # secure, but not necessary for this project
        password_hash = generate_password_hash(password)

        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            raise ValueError("User with that e-mail already exists!")
        else:
            user = User(email=email, password_hash=password_hash)  # type: ignore
            db.session.add(user)
            db.session.commit()
            return user
