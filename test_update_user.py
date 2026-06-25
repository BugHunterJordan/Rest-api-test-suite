"""
🧪 PUT Test: Update User 

What this test verifies:
✔ The API allows updating an existing user
✔ The update request is accepted successfully
✔ The returned data reflects the changes

In simple terms:
We are checking if we can change an existing user's information.
"""

import requests

def test_update_user(base_url):
    # New data we want to update the user with
    payload = {
        "name": "Jordan Updated",
        "email": "updated@test.com"
    }

    # Send update request for user with ID 1
    response = requests.put(f"{base_url}/users/1", json=payload)

    # Check update was successful
    assert response.status_code == 200

    # Convert response into readable format
    data = response.json()

    # Check updated values are correct
    assert data["name"] == "Jordan Updated"
    assert data["email"] == "updated@test.com"