from fastapi.testclient import TestClient

from studysage.main import app

client = TestClient(app)


def test_create_document_valid():
    """Valid title and description -> 201, and the body matches what you sent."""
    payload = {"title": "Math Notes", "description": "Calculus 101"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 201
    assert response.json() == payload


def test_create_document_title_only():
    """Title only, no description -> 201"""
    payload = {"title": "Comp Sci Notes"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 201
    assert response.json() == {"title": "Comp Sci Notes", "description": None}


def test_create_document_missing_title():
    """Missing title -> 422."""
    payload = {"description": "Where is the title?"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 422


def test_create_document_empty_title_bonus():
    """Bonus: empty-string title -> 422."""
    payload = {"title": "", "description": "Empty title string"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 422
