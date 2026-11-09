import pytest

# Test the blocks for 0, 1, and 2 excluded tools
@pytest.mark.parametrize("excluded", [
    [],                            # Block: 0 tools excluded
    ["Knife"],                     # Block: 1 tool excluded
    ["Scissors"],                  # Block: 1 tool excluded
    ["Knife", "Pizza cutter"]      # Block: 2 tools excluded
])
def test_excluded_tool_is_not_used(api, auth, excluded): 
    body = {"excludedTools": excluded} 
    res = api.post("/api/pizza", json=body, headers=auth) 
    assert res.status_code == 200 
    assert res.json()["pizza"]["tool"] not in excluded

# Test the block for 3 (all) tools excluded, which currently triggers a defect
@pytest.mark.xfail(reason="Defect 1: API returns 500 instead of 400 when all tools are excluded", strict=True)
def test_all_tools_excluded_returns_400(api, auth):
    body = {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
    res = api.post("/api/pizza", json=body, headers=auth)
    
    # The product owner expects 400 Bad Request, but the API actually returns 500
    assert res.status_code == 400
    assert "error" in res.json()