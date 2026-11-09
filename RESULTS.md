# API lab results 
  
## Part 0 
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Large Hawaii
- Step 0.12, results of the three runs without a session (optional): 
- Step 0.16, blocks of "how many of the three tools are excluded": there are exactly four valid equivalence blocks based on the total available tools (Knife, Scissors, Pizza cutter).
  
## Defect report 
- Title: - Request: POST /api/pizza
- Expected result: Status code 400 (Bad Request) and a JSON error message explaining that no pizza can satisfy the request.
- Actual result: Status code 500 (Internal Server Error) with an empty response body.
- Severity: this request help to test the status 400 and 500 status that can be effect in the project 2.
  
## Part A 
- Step A4, status codes when the other user reads, changes and deletes: 
* **Read attempt status code:** 403
* **Update attempt status code:** 403
* **Delete attempt status code:** 403
  
## Part B 
1. (1) Network and infrastructure issues (e.g., misconfigured load balancers, DNS resolution, connection timeouts). (2) Integration failures between real components (e.g., the API failing to connect to the actual database, or mismatched data schemas that stubs ignored).Unit tests with stubs are deterministic and run extremely fast. They isolate the specific business logic being tested without failing due to external network blips or database outages, making debugging much easier.
2. Using a shared public token causes test flakiness due to shared state. If multiple students (or parallel test threads) run tests simultaneously, one test might delete or modify data that another test is relying on. And it can't use with project because in the project it generate unique of the test.
3. Because the cookie have own in the across the request
4. -- The block where all 3 tools were excluded (`["Knife", "Pizza cutter", "Scissors"]`).

-- A 400 with a message tells the client application exactly what they did wrong (e.g., "Cannot exclude all tools") so the developer can fix the input. A 500 with an empty body is opaque—it usually means the server crashed unexpectedly, leaving the client application stuck with no way to handle the error gracefully.

--`@pytest.mark.xfail` keeps the test in the test suite so the defect is documented and continually executed. If we deleted it, we would forget the bug exists. By using `strict=True`, the test suite will explicitly fail (alert us) the moment the developers fix the API, reminding us to remove the xfail mark.
5. 9 test by base test covering all base blocks + (2 non-base for C1) + (3 non-base for C2) + (1 non-base for C3) + (2 non-base for C4). (1 + 2 + 3 + 1 + 2 = 9).

Multiply the number of blocks in each characteristic: 3 (C1) × 4 (C2) × 2 (C3) × 3 (C4) = 72.
6. 404 (Not Found) or 403 (Forbidden).403 Forbidden is standard for "You don't have permission to view/edit this." However, returning 404 Not Found is also an expected and secure practice (preventing Insecure Direct Object Reference / IDOR).No. Returning 404 is often intentional security design. It prevents a malicious user from guessing rating IDs and confirming they exist. As long as the API does not return 200/204 (which would allow the breach), it is functioning securely.
7. The API returns `200 OK` and allows the request, returning data (an empty list of ratings, or the general ratings list).Yes, this is a severe Broken Authentication defect. The API is validating the *format* (length) of the token but failing to validate if the token is actually assigned to a real, logged-in user in the database.An attacker could generate random 16-character tokens to bypass login screens, steal personal user data (ratings, orders), and potentially overwrite or delete resources belonging to others.
8. 
**Better in API tests:** Validating exact boundary edge cases, testing invalid JSON payloads, checking specific HTTP status codes, and executing hundreds of tests in seconds without UI rendering overhead.
* **Only possible in Web Page tests:** Checking that visual elements render correctly on different screen sizes (CSS/HTML), verifying that a specific button is physically clickable by a user, and ensuring the frontend JavaScript correctly connects to the backend.