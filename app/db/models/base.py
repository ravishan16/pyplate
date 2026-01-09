"""
Base model class for SQLAlchemy models.

This module provides a base class for all SQLAlchemy models with common functionality.
"""
import uuid
from typing import Any

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql.schema import MetaData

# SQLAlchemy recommended naming convention for constraints
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)


@as_declarative(metadata=metadata)
class Base:
    """
    Base class for all SQLAlchemy models.

    This class provides:
    - Automatic table naming based on class name
    - Common timestamp columns (created_at, updated_at)
    - Utility methods for serialization
    """

    id: Any
    __name__: str

    @declared_attr  # type: ignore[arg-type]
    def __tablename__(cls) -> str:
        """Generate table name automatically from class name."""
        return cls.__name__.lower()


class TimestampMixin:
    """Mixin to add timestamp columns to a model."""

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )


class UUIDMixin:
    """Mixin to add UUID primary key to a model."""

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
