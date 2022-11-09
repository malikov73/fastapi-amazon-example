from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_child_resource():
    response_auth = client.get("/api/test")
    assert response_auth.status_code == 200
