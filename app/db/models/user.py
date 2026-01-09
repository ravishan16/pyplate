"""
User model for authentication and user management.
"""
from sqlalchemy import Boolean, Column, String

from app.db.models.base import Base, TimestampMixin, UUIDMixin


class User(Base, UUIDMixin, TimestampMixin):
    """
    User model for authentication.

    Attributes:
        id (str): UUID primary key
        email (str): User's email address (unique)
        username (str): User's username (unique)
        full_name (str): User's full name
        hashed_password (str): Hashed user password
        is_active (bool): Whether the user account is active
        is_superuser (bool): Whether the user has superuser privileges
        created_at (datetime): When the user was created
        updated_at (datetime): When the user was last updated
    """

    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        """String representation of the user."""
        return f"<User {self.username}>"
