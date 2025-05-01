import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_webhook_post_success(mocker, client):
    # Mock subprocess.run to simulate successful commands
    mocker.patch('subprocess.run', return_value=None)

    # Send a POST request to the /webhook route
    response = client.post('/webhook')

    # Assert the response status code and message
    assert response.status_code == 200
    assert b"Repository updated and application deployed successfully!" in response.data

def test_webhook_post_failure(mocker, client):
    # Mock subprocess.run to simulate a command failure
    mocker.patch('subprocess.run', side_effect=Exception("Command failed"))

    # Send a POST request to the /webhook route
    response = client.post('/webhook')

    # Assert the response status code and error message
    assert response.status_code == 500
    assert b"Error during deployment" in response.data

def test_webhook_invalid_method(client):
    # Send a GET request to the /webhook route
    response = client.get('/webhook')

    # Assert the response status code and message
    assert response.status_code == 400
    assert b"Invalid request method" in response.data