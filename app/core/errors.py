"""
Core error handling for the FastAPI application.

This module provides exception classes, error response models, and
exception handlers for consistent error responses across the API.
"""
from typing import Any, Dict, List, Optional, Union

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class ErrorResponse(BaseModel):
    """Standard error response model."""

    status: str = "error"
    message: str
    details: Optional[Union[List[Dict[str, Any]], Dict[str, Any], str]] = None


class AppException(Exception):
    """Base exception class for application-specific exceptions."""

    status_code: int = 500
    detail: str = "An unexpected error occurred."

    def __init__(
        self,
        detail: Optional[str] = None,
        status_code: Optional[int] = None,
    ):
        if detail is not None:
            self.detail = detail
        if status_code is not None:
            self.status_code = status_code
        super().__init__(self.detail)


class NotFoundError(AppException):
    """Exception raised when a resource is not found."""

    status_code = 404
    detail = "Resource not found."


class ValidationError(AppException):
    """Exception raised when validation fails."""

    status_code = 400
    detail = "Validation error."


class AuthenticationError(AppException):
    """Exception raised when authentication fails."""

    status_code = 401
    detail = "Authentication failed."


class AuthorizationError(AppException):
    """Exception raised when authorization fails."""

    status_code = 403
    detail = "Not authorized to perform this action."


class DatabaseError(AppException):
    """Exception raised when a database operation fails."""

    status_code = 500
    detail = "Database operation failed."


class ConflictError(AppException):
    """Exception raised when there's a conflict with existing data."""

    status_code = 409
    detail = "Conflict with existing data."


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    """Handle application-specific exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.detail},
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle validation errors from request data."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": "error",
            "message": "Validation error",
            "details": exc.errors(),
        },
    )


async def sqlalchemy_exception_handler(
    request: Request, exc: SQLAlchemyError
) -> JSONResponse:
    """Handle SQLAlchemy errors."""
    status_code = 500
    message = "Database error"

    if isinstance(exc, IntegrityError):
        status_code = 409
        message = "Database integrity error"

    return JSONResponse(
        status_code=status_code,
        content={"status": "error", "message": message},
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle any unhandled exceptions."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


def setup_exception_handlers(app: FastAPI) -> None:
    """Register all exception handlers with the FastAPI application."""
    app.add_exception_handler(
        AppException,
        app_exception_handler,  # type: ignore[arg-type]
    )
    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,  # type: ignore[arg-type]
    )
    app.add_exception_handler(
        SQLAlchemyError,
        sqlalchemy_exception_handler,  # type: ignore[arg-type]
    )
    app.add_exception_handler(
        Exception,
        generic_exception_handler,  # type: ignore[arg-type]
    )
