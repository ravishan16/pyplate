"""
API endpoints package for version 1 of the API.
"""
from fastapi import APIRouter

from .status import router as status_router

api_router = APIRouter()

# Include routers from endpoint modules
api_router.include_router(status_router, prefix="/status", tags=["Status"])

# Add other endpoint routers here as they are created
# e.g., api_router.include_router(users_router, prefix="/users", tags=["Users"])
