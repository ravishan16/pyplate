from fastapi.testclient import TestClient


def test_get_status(client: TestClient) -> None:
    """
    Test the /status health check endpoint.
    """
    response = client.get("/api/v1/status")  # No trailing slash
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
