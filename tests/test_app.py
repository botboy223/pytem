import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_addition(client):
    response = client.post("/", data={"num1": "3", "num2": "5", "operation": "add"})
    assert b"Result: 8.0" in response.data

def test_division_by_zero(client):
    response = client.post("/", data={"num1": "5", "num2": "0", "operation": "divide"})
    assert b"Error: Invalid input or division by zero" in response.data
