import pytest

def test_other_user_cannot_read_rating(api, other_auth, rating):
    rating_id = rating["id"]
    res = api.get(f"/api/ratings/{rating_id}", headers=other_auth)
    
    # Store the actual status code this returns to put into RESULTS.md (e.g., 403 or 404)
    assert 400 <= res.status_code <= 499

def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    rating_id = rating["id"]
    original_stars = rating["stars"]
    
    res = api.put(f"/api/ratings/{rating_id}", json={"stars": 5}, headers=other_auth)
    assert 400 <= res.status_code <= 499
    
    # Ensure the original owner's rating remains unchanged
    read_res = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert read_res.json()["stars"] == original_stars

def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    rating_id = rating["id"]
    
    res = api.delete(f"/api/ratings/{rating_id}", headers=other_auth)
    assert 400 <= res.status_code <= 499
    
    # Ensure the rating still exists for the original owner
    read_res = api.get(f"/api/ratings/{rating_id}", headers=auth)
    assert read_res.status_code == 200