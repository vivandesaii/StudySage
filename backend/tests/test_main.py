from fastapi.testclient import TestClient
from studysage.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}