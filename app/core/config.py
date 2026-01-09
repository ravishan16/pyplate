"""
Settings configuration for the application using Pydantic's BaseSettings
"""
import json
import os
from typing import List, Optional

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file
load_dotenv()

# Define a TypeAdapter for validating a list of AnyHttpUrl
ListOfAnyHttpUrlAdapter = TypeAdapter(List[AnyHttpUrl])


class Settings(BaseSettings):
    # Project settings
    PROJECT_NAME: str = "PyPlate"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "A modern Python API template using FastAPI."
    API_V1_STR: str = "/api/v1"

    # Database settings
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv(
        "DATABASE_URL", "sqlite+aiosqlite:///./test.db"
    )

    # Authentication settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # API Key settings
    API_KEY_HEADER: str = "X-API-Key"
    # Example API key (replace with secure generation/storage)
    STATIC_API_KEY: Optional[str] = os.getenv("STATIC_API_KEY")

    # Pydantic settings configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",  # Keep ignoring extra env vars
    )


# Instantiate settings WITHOUT CORS fields
settings = Settings()


# --- Manual CORS Handling ---
def parse_and_validate_cors_origins(env_value: Optional[str]) -> List[AnyHttpUrl]:
    """Parses and validates CORS origins from an environment variable string."""
    if env_value is None or not env_value.strip():
        return []

    origins: List[str] = []
    input_str = env_value.strip()

    # Parsing logic (same as before)
    if input_str.startswith("[") and input_str.endswith("]"):
        try:
            parsed_json = json.loads(input_str)
            if isinstance(parsed_json, list):
                origins = [str(item) for item in parsed_json]
            else:
                origins = [o.strip() for o in input_str.split(",") if o.strip()]
        except json.JSONDecodeError:
            origins = [o.strip() for o in input_str.split(",") if o.strip()]
    else:
        origins = [o.strip() for o in input_str.split(",") if o.strip()]

    # Validation logic
    try:
        return ListOfAnyHttpUrlAdapter.validate_python(origins)
    except Exception as e:
        error_msg = (
            f"Invalid URL found in BACKEND_CORS_ORIGINS ('{env_value}'). "
            f"Parsed as {origins}. Error: {e}"
        )
        raise ValueError(error_msg)


# Manually load, parse, and validate the environment variable
raw_cors_origins = os.getenv("BACKEND_CORS_ORIGINS")
validated_cors_origins: List[AnyHttpUrl] = parse_and_validate_cors_origins(
    raw_cors_origins
)
# --- End Manual CORS Handling ---
