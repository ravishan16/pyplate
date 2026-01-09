# Getting Started

This guide will help you get started with using the PyPlate FastAPI service.

!!! note "Current Development Status"
    The PyPlate FastAPI project is currently in **Phase 1** of development with a focus on infrastructure setup.
    Limited endpoints are available while we work on implementing the full feature set.

## Running the API

You can run the API using either local development mode or Docker.

### Option 1: Local Development

```bash
# Create the Conda environment
conda create -n fastapi-modernization python=3.13

# Activate the environment
conda activate fastapi-modernization

# Install Poetry
conda install -c conda-forge poetry

# Install dependencies
make setup

# Run the API locally
make run
```

### Option 2: Docker (Recommended)

```bash
# Build the Docker image
make docker-build

# Run the Docker container
make docker-run
```

The API will be available at `http://localhost:8000`.

## Accessing the API Documentation

Interactive API documentation is available when the application is running:

- **Swagger UI**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
- **ReDoc**: [http://localhost:8000/api/v1/redoc](http://localhost:8000/api/v1/redoc)
- **OpenAPI JSON**: [http://localhost:8000/api/v1/openapi.json](http://localhost:8000/api/v1/openapi.json)

## Currently Available Endpoints

In the current phase, only the following endpoints are available:

### Health Check

```bash
# Root health check
curl http://localhost:8000/

# API status check
curl http://localhost:8000/api/v1/status
```

Both endpoints return a status indicating whether the API is operational.

## API Versioning

All API endpoints are versioned to ensure backward compatibility as the API evolves:

```
/api/v1/...
```

## Planned Features (Coming in Phase 2)

The following features are planned for the next phase of development:

### Authentication

The API will support two authentication methods:

1. **API Key Authentication** - For service-to-service communication
2. **JWT Authentication** - For user authentication

### Books API

```bash
# List books
curl http://localhost:8000/api/v1/books

# Search books
curl http://localhost:8000/api/v1/books/search?query=Sherlock

# Get book details
curl http://localhost:8000/api/v1/books/123
```

### Authors API

```bash
# List authors
curl http://localhost:8000/api/v1/authors

# Get author details
curl http://localhost:8000/api/v1/authors/45

# Get books by author
curl http://localhost:8000/api/v1/authors/45/books
```

## Standard Response Format

All API responses follow a standard JSON format:

```json
{
  "status": "success",
  "data": {
    // The requested data
  },
  "message": null
}
```

For errors:

```json
{
  "status": "error",
  "data": null,
  "message": "Error message describing the issue"
}
```

## Pagination (Coming Soon)

List endpoints will support pagination with the following query parameters:

- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10, max: 100)

Example:

```
GET /api/v1/books?page=2&limit=20
```

## Development Roadmap

For more information about the project's development status and roadmap, please refer to the [CHECKPOINT.md](https://github.com/ravishan16/pyplate/blob/main/CHECKPOINT.md) file in the repository.