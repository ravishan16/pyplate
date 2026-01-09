"""
Test configuration and fixtures for pytest.
"""
from typing import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import create_app


@pytest.fixture(scope="session")
def app() -> FastAPI:
    """Create a FastAPI app for testing."""
    return create_app()


@pytest.fixture(scope="session")
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    """Create a test client for testing."""
    with TestClient(app, base_url="http://testserver") as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create an async client for testing."""
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
