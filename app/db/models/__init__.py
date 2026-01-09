"""
Models package initialization.

Import all models here to ensure they are registered with SQLAlchemy.
"""
from app.db.models.base import Base
from app.db.models.user import User

__all__ = ["Base", "User"]
