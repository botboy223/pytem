# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test if the hello world route works."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
