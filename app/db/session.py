"""
Database session management.

This module provides SQLAlchemy session management with async support
for the FastAPI application.
"""
# Configure logging
import logging
from typing import AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool
from sqlalchemy.sql import text  # Import text

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create async engine based on configuration
engine: Optional[AsyncEngine] = None

if settings.SQLALCHEMY_DATABASE_URI:
    connect_args = {}

    # Apply SQLite-specific configuration
    if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
        connect_args = {"check_same_thread": False}

    engine = create_async_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        echo=False,  # Set to True for SQL query logging
        future=True,
        connect_args=connect_args,
        poolclass=NullPool
        if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite")
        else None,
    )

# Create session factory
async_session_factory: Optional[async_sessionmaker[AsyncSession]] = None
if engine:
    async_session_factory = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )


async def connect_to_db() -> None:
    """Connect the engine (if not already connected)."""
    # Engine connection is typically managed implicitly by session usage,
    # but this provides an explicit connection point if needed.
    if engine:
        try:
            # Perform a simple connection test
            async with engine.connect() as connection:
                await connection.execute(text("SELECT 1"))
            logger.info("Database connection successful.")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise
    else:
        logger.error("Database engine not initialized.")
        raise RuntimeError("Database engine not initialized.")


async def close_db_connection() -> None:
    """Dispose of the database engine."""
    global engine
    if engine:
        logger.info("Closing database connection...")
        await engine.dispose()
        engine = None  # Ensure engine is marked as None after disposal
        logger.info("Database connection closed.")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency for getting async database sessions.

    Usage:
        @app.get("/items/")
        async def get_items(db: AsyncSession = Depends(get_db)):
            items = await crud.get_items(db)
            return items
    """
    # Add check for initialized factory
    if async_session_factory is None:
        raise RuntimeError(
            "Database session factory is not initialized. Ensure DB is configured."
        )

    async with async_session_factory() as session:
        try:
            yield session
            # Removed commit/rollback here - let the endpoint handle transactions
        except Exception:
            # Rollback in case of exception within the endpoint
            await session.rollback()
            raise
        finally:
            await session.close()
