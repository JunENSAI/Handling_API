from fastapi.testclient import TestClient
from simple_api import app

# Create the test client linked to our app
client = TestClient(app)

# --- TEST CASE 1: Basic Root Check ---
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

# --- TEST CASE 2: Create Item (Happy Path) ---
def test_create_item():
    payload = {"name": "Test Item", "price": 10}
    response = client.post("/items/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10

# --- TEST CASE 3: Validation Error (Sad Path) ---
def test_create_item_negative_price():
    payload = {"name": "Bad Item", "price": -5}
    response = client.post("/items/", json=payload)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Price cannot be negative"

# --- TEST CASE 4: Not Found Error ---
def test_read_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"