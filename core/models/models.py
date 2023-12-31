"""Database Models."""


from db import Base
from sqlalchemy import Column, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class User(Base):
    """User table model.

    Args:
        Base: Base class for creating schemas.
    """

    __tablename__ = "users"

    email = Column(Text, primary_key=True)
    user_name = Column(Text)
    password = Column(Text)

    tasks = relationship("Tasks", back_populates="owner")


class Tasks(Base):
    """Tasks table model.

    Args:
        Base: Base class for creating schemas.
    """

    __tablename__ = "tasks"

    id = Column(Text, primary_key=True)
    title = Column(Text, primary_key=True)
    description = Column(Text, primary_key=True)
    completion_status = Column(Boolean, primary_key=True)
    owner_id = Column(Text, ForeignKey("users.email"))

    owner = relationship("User", back_populates="tasks")
