"""
PyPlate FastAPI - Main Application Entry Point
"""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import api_router
from app.api.v1.endpoints import api_router

# Import settings and validated_cors_origins
from app.core.config import settings, validated_cors_origins
from app.core.errors import setup_exception_handlers
from app.db.session import close_db_connection, connect_to_db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    # Create a base FastAPI instance with standard config
    app_instance = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        # Don't use f-strings with API_V1_STR to avoid path construction issues
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Set up CORS middleware using validated_cors_origins
    if validated_cors_origins:
        app_instance.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in validated_cors_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Set up custom exception handlers
    setup_exception_handlers(app_instance)

    # Include API router with proper prefix
    # Make sure prefix always starts with a forward slash
    api_prefix = (
        settings.API_V1_STR
        if settings.API_V1_STR.startswith("/")
        else f"/{settings.API_V1_STR}"
    )
    app_instance.include_router(api_router, prefix=api_prefix)

    # Register startup and shutdown event handlers
    # Note: We're keeping the on_event approach for now since we're running into compatibility issues
    # with the lifespan context manager in testing
    @app_instance.on_event("startup")
    async def startup_event_handler():
        """Connect to database on startup."""
        logger.info("Starting up application...")
        await connect_to_db()

    @app_instance.on_event("shutdown")
    async def shutdown_event_handler():
        """Disconnect from database on shutdown."""
        logger.info("Shutting down application...")
        await close_db_connection()

    # Add root health check endpoint
    @app_instance.get("/", tags=["Health"])
    async def health_check() -> dict[str, str]:
        """Root endpoint for health checks."""
        return {"status": "healthy"}

    return app_instance


# Create app instance for production use
# In tests, we'll use the create_app() function directly to get a fresh instance
app = create_app() if __name__ != "__main__" else None

# When the module is run directly (as the main program), create the app
if __name__ == "__main__":
    app = create_app()
