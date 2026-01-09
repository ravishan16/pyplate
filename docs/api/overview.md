# API Overview

This page provides an overview of the PyPlate FastAPI endpoints and functionality.

!!! note "Current API Status"
    The API is currently in Phase 1 of development with limited endpoints available.
    The documentation below reflects both current and planned API endpoints.

## Accessing the API

The API can be accessed in two ways:

### Local Development
```bash
# Run locally with hot reloading
make run

# Access at http://localhost:8000
```

### Docker Container
```bash
# Build and run with Docker
make docker-build
make docker-run

# Access at http://localhost:8000
```

## API Documentation

Interactive API documentation is available when the application is running:

- **Swagger UI**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
- **ReDoc**: [http://localhost:8000/api/v1/redoc](http://localhost:8000/api/v1/redoc)
- **OpenAPI JSON**: [http://localhost:8000/api/v1/openapi.json](http://localhost:8000/api/v1/openapi.json)

## API Versioning

All endpoints are versioned to ensure backward compatibility:

```
/api/v1/...
```

## Currently Available Endpoints

### Health Checks

```
GET /               # Root health check
GET /api/v1/status  # API status check
```

Both endpoints return a status indicating the API is operational.

## Planned Endpoints (Coming in Phase 2)

### Authentication

The API will support two authentication methods:

1. **API Key Authentication** - For service-to-service communication
2. **JWT Authentication** - For user authentication

### Books API

The Books API will provide access to the Project Gutenberg books dataset.

```
GET /api/v1/books                  # List books
GET /api/v1/books/{book_id}        # Get book details
GET /api/v1/books/search           # Search books
```

### Authors API

The Authors API will provide information about authors in the Project Gutenberg dataset.

```
GET /api/v1/authors                # List authors
GET /api/v1/authors/{author_id}    # Get author details
GET /api/v1/authors/{author_id}/books # Get books by author
```

## Standard Response Format

All API responses follow a standard format:

For successful requests:

```json
{
  "status": "success",
  "data": {
    // Response data
  },
  "message": null
}
```

For errors:

```json
{
  "status": "error",
  "data": null,
  "message": "Error description"
}
```

## Error Codes

| HTTP Status | Description |
|-------------|-------------|
| 200         | Success     |
| 201         | Created     |
| 400         | Bad Request |
| 401         | Unauthorized |
| 403         | Forbidden   |
| 404         | Not Found   |
| 500         | Internal Server Error |

## Future Features

The following features are planned for future releases:

- Rate limiting
- Caching
- Advanced search functionality
- User management
- Data export options