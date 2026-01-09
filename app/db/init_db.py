"""
Database initialization script for PyPlate FastAPI.

This script initializes the database by creating all tables and can seed
initial data if required.

Usage:
    python -m app.db.init_db
"""
import asyncio
import logging

from app.db.models.base import metadata  # Import metadata directly
from app.db.session import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init_db() -> None:
    """Initialize the database, creating tables and seeding initial data."""
    logger.info("Initializing database...")
    db_engine = engine

    if db_engine is None:
        raise ValueError("Database engine is not configured")

    logger.info("Creating database tables")

    # Create tables
    async with db_engine.begin() as conn:
        # Use the imported metadata object directly
        await conn.run_sync(metadata.create_all)

    logger.info("Database tables created")


async def main() -> None:
    """
    Main entry point for database initialization.
    """
    await init_db()
    # await seed_db() # Commented out until Phase 2 (requires crud, schemas)


# Comment out seed_db function for now
# async def seed_db() -> None:
#     """
#     Seed the database with initial data.
#
#     This function will populate the database with any required initial data,
#     such as admin users or default settings.
#     """
#     from app.db.crud import create_user # Depends on Phase 2
#     from app.db.models.user import UserCreate # Depends on Phase 2
#     from app.db.session import async_session # Check usage with sessionmaker
#
#     logger.info("Seeding database with initial data")
#
#     # Create default user
#     async with async_session() as session:
#         logger.info("Creating initial user...")
#         user_in = UserCreate(
#             email="admin@example.com", password="password", is_superuser=True
#         )
#         await create_user(session, user_in)
#
#     logger.info("Database seeding complete")


if __name__ == "__main__":
    asyncio.run(main())
