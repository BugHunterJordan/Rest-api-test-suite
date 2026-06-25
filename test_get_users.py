"""
🧪 GET Test: Read Users

What this test verifies:
✔ The API can successfully return a list of users
✔ The response is not empty
✔ The request works without errors

In simple terms:
We are checking that we can fetch users from the system and actually get data back.
"""

import requests

def test_get_users(base_url):
    # Send a request to get all users from the API
    response = requests.get(f"{base_url}/users")

    # Check that the API responded successfully (200 = OK)
    assert response.status_code == 200

    # Turn the response into readable Python data (list/dictionary)
    data = response.json()

    # Check that we actually got users back (not empty)
    assert isinstance(data, list)
    assert len(data) > 0