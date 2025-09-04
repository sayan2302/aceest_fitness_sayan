import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Reset workouts before every test
        app.config["WORKOUTS"].clear()
        yield client


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_workout_success(client):
    response = client.post("/add", data={"workout": "Running", "duration": "30"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"added successfully" in response.data


def test_add_workout_missing_fields(client):
    response = client.post("/add", data={"workout": "", "duration": "30"}, follow_redirects=True)
    assert b"required" in response.data


def test_add_workout_invalid_duration(client):
    response = client.post("/add", data={"workout": "Pushups", "duration": "abc"}, follow_redirects=True)
    assert b"Invalid duration" in response.data


def test_add_workout_negative_duration(client):
    response = client.post("/add", data={"workout": "Pushups", "duration": "-5"}, follow_redirects=True)
    assert b"Invalid duration" in response.data


def test_delete_workout_success(client):
    client.post("/add", data={"workout": "Running", "duration": "30"})
    response = client.get("/delete/0", follow_redirects=True)
    assert b"deleted successfully" in response.data
    assert b"Running" not in response.data


def test_delete_workout_success(client):
    client.post("/add", data={"workout": "Running", "duration": "30"})
    response = client.get("/delete/0", follow_redirects=True)
    assert b"deleted successfully" in response.data
    assert b"<tbody>\n                \n            </tbody>" in response.data
