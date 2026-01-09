# Makefile for PyPlate FastAPI Modernization

# Load .env file - Use `export $(cat .env | xargs)` if `include .env` doesn't work
-include .env
export

# Default Conda environment name if not set in .env
CONDA_ENV_NAME ?= fastapi-modernization

.PHONY: setup test lint run build docker-run docs clean init-db migrate validate-ci check-conda-env

# Variables
PYTHON = python
APP_NAME = app
DOCKER_IMAGE = pyplate-fastapi
DOCKER_TAG = latest

# Check if the correct Conda environment is active
check-conda-env:
	@if [ "$$CONDA_DEFAULT_ENV" = "$(CONDA_ENV_NAME)" ]; then \
		echo "Correct Conda environment ('$(CONDA_ENV_NAME)') is active."; \
	else \
		echo "Checking if Conda environment '$(CONDA_ENV_NAME)' exists..."; \
		conda env list | grep "^$(CONDA_ENV_NAME) " > /dev/null; \
		if [ $$? -eq 0 ]; then \
			echo "Error: Conda environment '$(CONDA_ENV_NAME)' exists but is not active."; \
			echo "Please activate it first: conda activate $(CONDA_ENV_NAME)"; \
		else \
			echo "Error: Conda environment '$(CONDA_ENV_NAME)' does not exist."; \
			echo "Please create it using the instructions in the README or copilot-instructions.md"; \
		fi; \
		exit 1; \
	fi

# Setup development environment
setup: check-conda-env
	poetry install
	pre-commit install

# Initialize database
init-db: check-conda-env
	poetry run python -m $(APP_NAME).db.init_db

# Run database migrations
migrate: check-conda-env
	poetry run alembic upgrade head

# Generate new migration
migration: check-conda-env
	poetry run alembic revision --autogenerate -m "$(message)"

# Run tests
test: check-conda-env
	poetry run pytest app/tests/ --cov=$(APP_NAME) --cov-report=term-missing --cov-report=xml

# Run linting
lint: check-conda-env
	poetry run black $(APP_NAME) 
	poetry run isort $(APP_NAME)
	poetry run flake8 --max-line-length=88 --extend-ignore=E203 $(APP_NAME) # Explicitly set config
	poetry run mypy $(APP_NAME)

# Run the application locally
run: check-conda-env
	poetry run uvicorn $(APP_NAME).main:app --reload

# Build Docker container
# No conda check needed here as it runs in its own environment
docker-build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run Docker container
# No conda check needed here
docker-run:
	docker run -p 8000:8000 --name $(DOCKER_IMAGE) $(DOCKER_IMAGE):$(DOCKER_TAG)

# Generate documentation
docs: check-conda-env
	poetry run mkdocs build

# Start documentation server
docs-serve: check-conda-env
	poetry run mkdocs serve

# Validate GitHub Actions workflow files
# No conda check needed here
validate-ci:
	[ -x "$(command -v actionlint)" ] || (echo "Installing actionlint..." && go install github.com/rhysd/actionlint/cmd/actionlint@latest)
	actionlint .github/workflows/*.yml

# Check project status - runs tests, lint, and validates CI
check: check-conda-env lint test validate-ci

# Clean build artifacts
# No conda check needed here
clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf .mypy_cache
	rm -rf site
	rm -f $(APP_NAME)/*.db # Use wildcard to remove any .db file in app/
	rm -f ./*.db # Use wildcard to remove any .db file in root
	find . -type d -name __pycache__ -exec rm -rf {} +