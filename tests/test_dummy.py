"""
Example unit test
"""

from fastapi.testclient import TestClient
from asgi import app

client = TestClient(app)


def test_home():
    """
    GIVEN a FastAPI app
    WHEN the user requests the home endpoint
    THEN the response should have a 200 status code and a "Hello World" message.
    """
    response = client.get("/")
    assert response.status_code
    assert response.json()
