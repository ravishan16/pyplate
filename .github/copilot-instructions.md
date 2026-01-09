# GitHub Copilot Instructions for PyPlate Modernization

This file contains instructions for GitHub Copilot to assist with the modernization of PyPlate from Flask to FastAPI.

## Project Overview

PyPlate is being modernized from a Flask-based API to a FastAPI application with the following key features:
- Project Gutenberg books dataset for demonstration
- JWT and API key authentication
- SQLite for development/testing and PostgreSQL for production
- Docker and Docker Compose for containerization
- Comprehensive testing suite with pytest
- GitHub Actions for CI/CD

## Project Status

Before making any changes, check the current status of the modernization in the [CHECKPOINT.md](/CHECKPOINT.md) file, which contains detailed information about:
- Completed tasks
- Pending tasks
- Current project structure
- Next steps

## Acceptance Criteria for Each Phase

For a phase to be considered complete, it must meet these criteria:

1. **Local Execution**
   - Application must run locally without errors (`make run`)
   - All required services must start properly

2. **Tests Pass**
   - All unit tests must pass (`make test`)
   - Test coverage must meet the minimum threshold (80%)
   - All linting checks must pass (`make lint`)

3. **API Functionality**
   - APIs must be testable through Swagger UI
   - All documented endpoints must work as expected

4. **CI/CD Pipeline**
   - GitHub Actions workflows must successfully complete
   - Docker image must build successfully

5. **Documentation**
   - CHECKPOINT.md must be updated with completed tasks
   - New features must be documented
   - Next phase must be outlined

## Phase Implementation Process

1. **Planning**:
   - Review the current state in CHECKPOINT.md
   - Define tasks for the current phase
   - Get confirmation from the user before starting

2. **Implementation**:
   - Follow coding guidelines (see below)
   - Use `make` commands for standardized operations
   - Update documentation as you implement features

3. **Testing**:
   - Run `make check` to verify all tests pass
   - Test API endpoints manually through Swagger UI

4. **Finalization**:
   - Update CHECKPOINT.md with completed tasks
   - Push changes and create pull request
   - Ensure GitHub Actions workflow runs successfully

## Important Note

Always check with the user before making substantial changes to the codebase. Specifically:
- Present your plan before implementing it
- Ask for confirmation before deleting or significantly modifying existing files
- Provide reasoning for architectural decisions
- Offer alternatives when appropriate

## Branch Information

Development is taking place in the branch: `3-modernize-flask-api-to-fastapi-with-project-gutenberg-dataset`

## Environment Management

Use Conda for environment management with the following setup:
```bash
# Create the Conda environment
conda create -n fastapi-modernization python=3.13

# Activate the environment
conda activate fastapi-modernization

# Install Poetry for dependency management within the Conda environment
conda install -c conda-forge poetry

# Use Poetry for package management
poetry install
```

## Getting the Application Running

1. **Setup Environment**:
```bash
# Create and activate the conda environment
conda create -n fastapi-modernization python=3.13
conda activate fastapi-modernization

# Install Poetry
conda install -c conda-forge poetry

# Install dependencies
make setup
```

2. **Initialize Database**:
```bash
# Run migrations to set up the database schema
make migrate

# Seed the database with initial data (if implemented)
make init-db
```

3. **Run Application**:
```bash
# Start the FastAPI application
make run
```

4. **Access API Documentation**:
   - Open a browser and navigate to http://localhost:8000/api/v1/docs

## Coding Guidelines

1. Use async/await for database operations and API endpoints
2. Follow type hinting for all function parameters and return values
3. Use Pydantic for data validation and serialization
4. Implement dependency injection for services and repositories
5. Write comprehensive tests for all features
6. Document all functions and classes with docstrings
7. Use SQLAlchemy 2.0-style models

## Modernization Goals

1. Replace Flask with FastAPI
2. Replace setup.py/requirements.txt with Poetry
3. Upgrade SQLAlchemy to modern version with async support
4. Implement Project Gutenberg dataset models and seed scripts
5. Add JWT and API key authentication
6. Create comprehensive API documentation
7. Set up GitHub Actions for CI/CD
8. Implement admin and user interfaces in later phases

## Testing Requirements

1. All features must have unit tests
2. Integration tests for database operations
3. API tests for all endpoints
4. Test coverage must be >80%
5. Tests must run in CI/CD pipeline before merge

## Documentation Requirements

1. API documentation using OpenAPI/Swagger
2. Tutorial-style documentation for API users
3. Developer documentation for contributors
4. Detailed README with badges and setup instructions

When assisting, prioritize modern Python practices, security, and performance optimization.