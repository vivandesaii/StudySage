def test_create_document_valid(client):
    """Create -> 201 with an id and created_at timestamp."""
    payload = {"title": "Math Notes", "description": "Calculus 101"}
    response = client.post("/documents", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert isinstance(data["id"], int)
    assert "created_at" in data


def test_get_document_by_id_success(client):
    """Get by id -> 200 with the correct document data."""
    # 1. Create a document first
    create_payload = {"title": "Physics Notes", "description": "Quantum Mechanics"}
    create_res = client.post("/documents", json=create_payload)
    doc_id = create_res.json()["id"]

    # 2. Fetch it by ID
    response = client.get(f"/documents/{doc_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == doc_id
    assert data["title"] == "Physics Notes"
    assert data["description"] == "Quantum Mechanics"


def test_get_document_by_id_not_found(client):
    """Get a missing id -> 404."""
    response = client.get("/documents/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Document with this id does not exist."


def test_list_documents(client):
    """List returns all documents you created."""
    client.post("/documents", json={"title": "Doc Alpha", "description": "First doc"})
    client.post("/documents", json={"title": "Doc Beta", "description": "Second doc"})

    response = client.get("/documents")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2

    titles = [doc["title"] for doc in data]
    assert "Doc Alpha" in titles
    assert "Doc Beta" in titles


def test_create_document_missing_title(client):
    """Missing title -> 422 validation error."""
    payload = {"description": "Where is the title?"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 422


def test_create_document_empty_title_bonus(client):
    """Empty-string title -> 422 validation error."""
    payload = {"title": "", "description": "Empty title string"}
    response = client.post("/documents", json=payload)
    assert response.status_code == 422
