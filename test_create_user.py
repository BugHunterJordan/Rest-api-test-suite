"""
🧪 POST Test: Create User 

What this test verifies:
✔ The API can accept new user data
✔ The API responds successfully after creating a user
✔ The returned data matches what we sent

In simple terms:
We are checking if we can create a new user and get confirmation back.
"""

import requests

def test_create_user(base_url):
    # This is the new user data we are sending
    payload = {
        "name": "Jordan",
        "email": "jordan@test.com"
    }

    # Send request to create a user
    response = requests.post(f"{base_url}/users", json=payload)

    # Check if creation worked (200 or 201 = success)
    assert response.status_code in [200, 201]

    # Convert response into usable data
    data = response.json()

    # Check if the response matches what we sent
    assert data["name"] == "Jordan"
    assert data["email"] == "jordan@test.com"