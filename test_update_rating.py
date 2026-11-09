import pytest

@pytest.mark.parametrize("stars, expected_status", [
    (0, 400),
    (1, 200),
    (5, 200),
    (6, 400)
])
def test_update_rating_boundary(api, auth, rating, stars, expected_status):
    rating_id = rating["id"]
    original_stars = rating["stars"]
    
    # Attempt to update the rating
    update_data = {"stars": stars}
    res = api.put(f"/api/ratings/{rating_id}", json=update_data, headers=auth)
    
    assert res.status_code == expected_status
    
    # Read the rating back to confirm changes (or lack thereof)
    read_res = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert read_res.status_code == 200
    
    if expected_status == 200:
        assert read_res.json()["stars"] == stars
    else:
        assert read_res.json()["stars"] == original_stars