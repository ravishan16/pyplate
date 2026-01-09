FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set working directory
WORKDIR /app

# Install system dependencies required for building Python packages with C extensions
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc6-dev make python3-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Copy poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --only main --no-root

# Copy the application code
COPY app/ ./app/

# Create a non-root user and switch to it for security
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
