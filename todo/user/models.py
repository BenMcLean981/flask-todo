"""Set of models for the user blueprint"""
from todo.database import Column, Integer, Model, String, Text


class User(Model):
    """User model"""

    user_id = Column(Integer, primary_key=True)
    email = Column(String(320), nullable=False)
    # supposedly 320 is the maximum length of an e-mail address

    password_hash = Column(Text, nullable=False)

    def __repr__(self):
        return f"User: id={self.user_id}, e-mail={self.email}"
