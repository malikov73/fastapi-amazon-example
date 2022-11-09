from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, root_path='/dev')


def test_child_resource():
    response_auth = client.get("/api/test")
    assert response_auth.status_code == 200
