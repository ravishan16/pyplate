# Development Setup

This guide will help you set up your development environment for working on the PyPlate FastAPI project.

## Prerequisites

- Python 3.13+
- Conda (recommended for environment management)
- Docker and Docker Compose (for containerized development)
- Git

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/ravishan16/pyplate.git
cd pyplate
```

### 2. Create a Conda Environment

```bash
conda create -n fastapi-modernization python=3.13
conda activate fastapi-modernization
```

### 3. Install Poetry

```bash
conda install -c conda-forge poetry
```

### 4. Install Dependencies

```bash
make setup
```

This command will:
- Install all required dependencies using Poetry
- Set up pre-commit hooks for code quality

### 5. Run Tests

```bash
make test
```

### 6. Run the Application Locally

```bash
make run
```

The application will be available at http://localhost:8000.
API documentation will be available at http://localhost:8000/api/v1/docs.

## Development Workflow

1. Create a new branch for your feature or bug fix
2. Make your changes
3. Run tests and linting: `make test` and `make lint`
4. Commit your changes
5. Push to your branch
6. Create a pull request

## Project Structure

The project follows a clean, modular structure:

```
app/
│
├── api/                    # API endpoints
│   ├── v1/                 # API version 1
│   │   ├── endpoints/      # Route handlers
│   │   └── models/         # Pydantic models (schemas)
│
├── core/                   # Core functionality
│   ├── auth.py             # Authentication logic
│   ├── config.py           # Application configuration
│   └── errors.py           # Error handling
│
├── db/                     # Database
│   ├── migrations/         # Alembic migrations
│   ├── models/             # SQLAlchemy models
│   └── repositories/       # Database operations
│
├── services/               # Business logic
│   ├── books.py            # Book service
│   └── authors.py          # Author service
│
├── tests/                  # Tests
│   ├── api/                # API tests
│   ├── db/                 # Database tests
│   └── services/           # Service tests
│
├── utils/                  # Utilities
│   
├── main.py                 # Application entry point
```

## Environment Variables

The application uses environment variables for configuration. You can set these in a `.env` file in the project root:

```
# API settings
PROJECT_NAME=PyPlate FastAPI
API_V1_STR=/api/v1

# Security
SECRET_KEY=your-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 days

# Database
SQLALCHEMY_DATABASE_URI=sqlite:///./gutenberg.db
# For PostgreSQL:
# POSTGRES_SERVER=localhost
# POSTGRES_USER=postgres
# POSTGRES_PASSWORD=password
# POSTGRES_DB=gutenberg
# POSTGRES_PORT=5432

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```

## Documentation

To build the documentation site:

```bash
make docs
```

To serve the documentation locally:

```bash
make docs-serve
```

The documentation will be available at http://localhost:8000.