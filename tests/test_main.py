from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_child_resource():
    response_auth = client.get("/dev/api/test")
    assert response_auth.status_code == 200
