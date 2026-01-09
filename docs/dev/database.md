# Database Structure and Models

This document details the database structure of the PyPlate application, including data models, relationships, and database operations.

## Overview

PyPlate uses SQLAlchemy 2.0 with async support for database operations. In development, it uses SQLite with the aiosqlite driver, while in production, it's designed to use PostgreSQL with the asyncpg driver.

## Entity-Relationship Diagram

The following diagram illustrates the database schema and relationships between entities:

```mermaid
erDiagram
    User {
        uuid id PK
        string email UK
        string username UK
        string full_name
        string hashed_password
        boolean is_active
        boolean is_superuser
        datetime created_at
        datetime updated_at
    }
    
    Book {
        uuid id PK
        string title
        string gutenberg_id UK
        string language
        date publication_date
        datetime created_at
        datetime updated_at
    }
    
    Author {
        uuid id PK
        string name
        string birth_year
        string death_year
        datetime created_at
        datetime updated_at
    }
    
    BookAuthor {
        uuid id PK
        uuid book_id FK
        uuid author_id FK
        datetime created_at
        datetime updated_at
    }
    
    Category {
        uuid id PK
        string name UK
        datetime created_at
        datetime updated_at
    }
    
    BookCategory {
        uuid id PK
        uuid book_id FK
        uuid category_id FK
        datetime created_at
        datetime updated_at
    }
    
    User ||--o{ Book : "favorites"
    Book }|--|| BookAuthor : "has"
    Author ||--o{ BookAuthor : "written_by"
    Book }|--o{ BookCategory : "belongs_to"
    Category ||--o{ BookCategory : "contains"
```

## Base Models

### TimestampMixin

Adds creation and update timestamp fields to models:

- `created_at`: DateTime when the record was created
- `updated_at`: DateTime when the record was last updated

### UUIDMixin

Adds a UUID primary key field to models:

- `id`: UUID primary key

## Data Models

### User Model

The User model represents application users for authentication and authorization.

**Fields:**
- `id` (UUID, PK): Primary key
- `email` (String, UK): User's email address (unique)
- `username` (String, UK): User's username (unique)
- `full_name` (String): User's full name
- `hashed_password` (String): Hashed password for authentication
- `is_active` (Boolean): Whether the user's account is active
- `is_superuser` (Boolean): Whether the user has superuser privileges
- `created_at` (DateTime): When the record was created
- `updated_at` (DateTime): When the record was last updated

### Planned Models for Project Gutenberg Dataset

#### Book Model

Represents a book in the Project Gutenberg dataset.

**Fields:**
- `id` (UUID, PK): Primary key
- `title` (String): Book title
- `gutenberg_id` (String, UK): Project Gutenberg ID (unique)
- `language` (String): Book language code
- `publication_date` (Date): Book publication date
- `created_at` (DateTime): When the record was created
- `updated_at` (DateTime): When the record was last updated

#### Author Model

Represents book authors.

**Fields:**
- `id` (UUID, PK): Primary key
- `name` (String): Author's name
- `birth_year` (String): Author's birth year
- `death_year` (String): Author's death year
- `created_at` (DateTime): When the record was created
- `updated_at` (DateTime): When the record was last updated

#### Category Model

Represents book categories/genres.

**Fields:**
- `id` (UUID, PK): Primary key
- `name` (String, UK): Category name (unique)
- `created_at` (DateTime): When the record was created
- `updated_at` (DateTime): When the record was last updated

#### Association Tables

- **BookAuthor**: Many-to-many relationship between Books and Authors
- **BookCategory**: Many-to-many relationship between Books and Categories

## Database Operations

### Repositories

The application uses the repository pattern to encapsulate database operations. Each model has a corresponding repository class that handles CRUD operations:

```python
class BaseRepository:
    """Base repository for common CRUD operations."""
    
    def __init__(self, model, db_session):
        self.model = model
        self.db_session = db_session
    
    async def create(self, obj_in):
        """Create a new record."""
        pass
    
    async def get(self, id):
        """Get a record by ID."""
        pass
    
    async def get_multi(self, skip=0, limit=100):
        """Get multiple records with pagination."""
        pass
    
    async def update(self, id, obj_in):
        """Update a record."""
        pass
    
    async def delete(self, id):
        """Delete a record."""
        pass
```

## Migration System

PyPlate uses Alembic for database migrations. Migrations are automatically generated based on model changes and can be applied using the `make migrate` command.

## Database Configuration

The database connection is configured in `app/db/session.py` and uses environment variables defined in the application settings (`app/core/config.py`).

### Database URL Configuration

```python
# Configured in app/core/config.py
SQLALCHEMY_DATABASE_URI = "sqlite+aiosqlite:///./gutenberg.db"  # Development
# SQLALCHEMY_DATABASE_URI = "postgresql+asyncpg://user:password@postgresserver/db"  # Production
```

### Session Factory

```python
# app/db/session.py
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=settings.DB_ECHO)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    """Dependency for database session."""
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
```

## Database Initialization

The database initialization process is handled in `app/db/init_db.py`. It includes:

1. Creating tables if they don't exist
2. Seeding the database with initial data (e.g., admin user, sample books)

## Best Practices

1. Always use async/await for database operations
2. Use the repository pattern for database access
3. Keep models as lean as possible
4. Use type annotations for better IDE support
5. Use transactions for operations that require multiple database changes
6. Implement soft delete where appropriate