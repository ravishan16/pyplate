# PyPlate FastAPI - Project Gutenberg API

[![Test](https://github.com/ravishan16/pyplate/actions/workflows/test.yml/badge.svg)](https://github.com/ravishan16/pyplate/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Modern FastAPI application that provides a REST API for accessing and managing Project Gutenberg books.

> **Note**: This project is currently being modernized from a Flask-based API to FastAPI. See the [Modernization Plan](#modernization-plan) for more details.

## Features (Coming Soon)

- RESTful API for Project Gutenberg books data
- JWT and API key authentication
- Automatic API documentation with OpenAPI/Swagger
- Docker and Docker Compose for easy deployment
- SQLAlchemy 2.0 ORM with async support
- PostgreSQL for production, SQLite for development/testing
- Admin interface for managing books and authors
- User interface for browsing and searching books

## Project Goals

This project aims to modernize the original PyPlate application by:

- Migrating from Flask to the high-performance FastAPI framework.
- Implementing a robust API for the Project Gutenberg dataset.
- Adopting modern Python development practices (Poetry, SQLAlchemy 2.0 async, Pydantic).
- Establishing a containerized development and deployment workflow using Docker.
- Ensuring code quality through comprehensive testing and CI/CD with GitHub Actions.
- Adding features like JWT/API Key authentication and eventually user/admin interfaces.

## Quick Start

### Local Development

Follow these steps to set up and run the application locally:

1.  **Setup Environment**:
    ```bash
    # Create Conda environment (if you haven't already)
    conda create -n fastapi-modernization python=3.13
    conda activate fastapi-modernization

    # Install Poetry (if you haven't already)
    conda install -c conda-forge poetry

    # Install project dependencies
    make setup
    ```

2.  **Initialize Database**:
    ```bash
    # Run database migrations (Alembic setup pending in Phase 2)
    # make migrate

    # Seed the database with initial data (Script pending in Phase 2)
    # make init-db
    ```
    *Note: Database migration and seeding steps will be fully functional in Phase 2.*

3.  **Run Application**:
    ```bash
    # Start the FastAPI development server
    make run
    ```

4.  **Access API**:
    - The API will be available at: `http://localhost:8000`
    - Check the status: `http://localhost:8000/api/v1/status`
    - Explore the API documentation (Swagger UI): `http://localhost:8000/api/v1/docs`

### Using Docker

```bash
# Clone the repository
git clone https://github.com/ravishan16/pyplate.git
cd pyplate

# Build and start the application container
make docker-run
```
*Note: The Docker container uses Python 3.11 due to `asyncpg` compatibility.*

Access the API and documentation as described in the local development section.

## Modernization Plan

This project is being modernized from a Flask-based API to FastAPI with a Project Gutenberg dataset. The modernization is being implemented in the following phases:

### Phase 1: Project Setup & Infrastructure ✅
- Clean up legacy files
- Set up new project structure with FastAPI conventions
- Create development environment with Poetry and Conda
- Create initial FastAPI application with configuration
- Set up GitHub Actions CI/CD pipeline
- Configure testing framework (pytest)
- Set up Docker and Docker Compose for local development
- Update documentation for local setup and running

### Phase 2: Database Models & Gutenberg Dataset 🔄
- Design SQLAlchemy models for Gutenberg data (Books, Authors, Genres, etc.)
- Set up database migrations with Alembic
- Create Pydantic schemas for data validation
- Implement script to seed database with Gutenberg dataset
- Set up SQLite for development/testing and PostgreSQL for production

### Phase 3: API Core Features 📅
- Implement JWT and API key authentication
- Create CRUD operation base classes
- Set up error handling and response standardization
- Configure logging
- Implement basic search functionality

### Phase 4: API Endpoints & Documentation 📅
- Implement comprehensive REST endpoints for Gutenberg data
- Set up automatic API documentation with Swagger/ReDoc
- Add pagination, filtering, and sorting
- Implement advanced search capabilities
- Create user documentation for API consumers

### Phase 5: Testing & Quality Assurance 📅
- Implement comprehensive test suite (unit, integration, API)
- Set up test coverage reporting and linting
- Create CI/CD pipeline for automated testing
- Implement data validation and sanitization
- Set up security scanning

### Phase 6: Admin Interface & User Interface 📅
- Create simple admin panel to manage books and authors
- Implement user interface for browsing and searching books
- Add bookmarking and user collection features
- Implement basic analytics
- Add links to the original Gutenberg resources

## Documentation

For complete documentation (coming soon), visit [Project Documentation](https://ravishan16.github.io/pyplate/).

- [User Guide](https://ravishan16.github.io/pyplate/user/getting-started/)
- [Developer Guide](https://ravishan16.github.io/pyplate/dev/setup/)
- [API Reference](https://ravishan16.github.io/pyplate/api/overview/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.