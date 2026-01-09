# Configuration

Application settings are managed using Pydantic's `BaseSettings` in `app/core/config.py`. Settings can be defined directly in the `Settings` class or loaded from environment variables or a `.env` file.

## Loading Settings

Settings are loaded in the following order of precedence:

1.  Environment variables.
2.  Variables defined in a `.env` file located in the project root.
3.  Default values defined in the `Settings` class in `app/core/config.py`.

## Available Settings

Here are the currently defined settings:

### Project Information

-   `PROJECT_NAME`: The name of the project (Default: "PyPlate FastAPI").
-   `PROJECT_DESCRIPTION`: A short description of the project (Default: "Modern API for Project Gutenberg books dataset").
-   `PROJECT_VERSION`: The current version of the application (Default: "0.1.0").

### API Configuration

-   `API_V1_STR`: The prefix for API version 1 routes (Default: "/api/v1").

### CORS (Cross-Origin Resource Sharing)

-   `BACKEND_CORS_ORIGINS`: A list of allowed origins for CORS requests. Can be set via environment variable as a comma-separated string of URLs (e.g., `"http://localhost:3000,https://your-frontend.com"`). Defaults to an empty list `[]`.

### Authentication (JWT)

These settings are used for JWT token generation and validation (implementation pending in Phase 3).

-   `SECRET_KEY`: The secret key used to sign JWT tokens. **Crucial for security.** Should be overridden via environment variable in production. (Default: "your-secret-key-change-in-production" - **CHANGE THIS**).
-   `ALGORITHM`: The algorithm used for JWT signing (Default: "HS256").
-   `ACCESS_TOKEN_EXPIRE_MINUTES`: The lifetime of an access token in minutes (Default: 10080, which is 7 days).

### Database

-   `SQLALCHEMY_DATABASE_URI`: The connection string for the database. Uses `aiosqlite` for async SQLite access by default. Can be overridden via environment variable to connect to PostgreSQL (e.g., `postgresql+asyncpg://user:password@host:port/dbname`). (Default: "sqlite+aiosqlite:///./books.db").

## Example `.env` File

Create a `.env` file in the project root to override default settings:

```dotenv
# .env

# Project Info (Optional - defaults are usually fine)
# PROJECT_NAME="My Gutenberg API"

# CORS - Allow frontend running on localhost:3000
BACKEND_CORS_ORIGINS=http://localhost:3000

# Authentication - **REQUIRED for Production**
SECRET_KEY=a_very_strong_and_random_secret_key_32_bytes_long
# ALGORITHM=HS256 # Default is usually fine
# ACCESS_TOKEN_EXPIRE_MINUTES=60 # e.g., 1 hour

# Database - Example for PostgreSQL
# SQLALCHEMY_DATABASE_URI=postgresql+asyncpg://user:password@localhost:5432/books_db # Example uses books_db

# Default SQLite
# SQLALCHEMY_DATABASE_URI=sqlite+aiosqlite:///./books.db
```

Refer to `app/core/config.py` for the most up-to-date list of settings and their default values.
