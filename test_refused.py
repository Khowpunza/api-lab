import uuid
import requests

BASE_URL = "https://quickpizza.grafana.com"


def test_duplicate_username():
    session = requests.Session()
    username = f"user_{uuid.uuid4().hex[:8]}"
    password = "Password123!"

    # Create initial user
    res1 = session.post(
        f"{BASE_URL}/api/users", json={"username": username, "password": password}
    )
    assert res1.status_code in (200, 201)

    # Attempt to create second user with the same username
    res2 = session.post(
        f"{BASE_URL}/api/users", json={"username": username, "password": password}
    )

    # Verify status code and error response
    assert res2.status_code == 400
    assert res2.json() == {"error": "username already taken"}


def test_wrong_password():
    session = requests.Session()
    username = f"user_{uuid.uuid4().hex[:8]}"
    correct_password = "Password123!"
    wrong_password = "WrongPassword123!"

    # Create user with correct password
    res1 = session.post(
        f"{BASE_URL}/api/users",
        json={"username": username, "password": correct_password},
    )
    assert res1.status_code in (200, 201)

    # Attempt login with incorrect password using the correct token endpoint
    res2 = session.post(
        f"{BASE_URL}/api/users/token/login",
        json={"username": username, "password": wrong_password},
    )

    # Verify status code and error response
    assert res2.status_code == 401
    assert res2.json() == {"error": "authentication failed"}


def test_empty_username():
    # Attempt to create user with an empty username string
    res = requests.post(
        f"{BASE_URL}/api/users", json={"username": "", "password": "Password123!"}
    )

    # Verify status code and error response
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}