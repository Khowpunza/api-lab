import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

# Base choice: 3 stars as a whole number, a real pizza, the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id

# C1: a number of stars below 1 or above 5 is refused with a message.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

# C2: Type of stars - decimal
def test_stars_decimal(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3.5}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json() # TODO: Replace with exact error string from curl

# C2: Type of stars - text
def test_stars_text(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": "3"}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json() # TODO: Replace with exact error string from curl

# C2: Type of stars - missing
def test_stars_missing(api, auth, pizza_id):
    new = {"pizza_id": pizza_id} # Missing stars field entirely
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json() # TODO: Replace with exact error string from curl

# C3: Pizza does not exist
def test_pizza_does_not_exist(api, auth):
    new = {"pizza_id": 999999999, "stars": 3}
    res = api.post("/api/ratings", json=new, headers=auth)
    assert res.status_code == 400 # QuickPizza might also use 404 here
    assert "error" in res.json() # TODO: Replace with exact error string from curl

# C4: Token missing
def test_token_missing(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new) # No headers passed
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}

# C4: Token wrong length
def test_token_wrong_length(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    res = api.post("/api/ratings", json=new, headers={"Authorization": "token short"})
    assert res.status_code == 401
    assert "error" in res.json() # TODO: Replace with exact error string from curl