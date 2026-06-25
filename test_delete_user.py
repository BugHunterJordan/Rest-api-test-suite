"""
🧪 DELETE Test: Remove User

What this test verifies:
✔ The API allows deleting a user
✔ The delete request is accepted
✔ The API responds with a success status

In simple terms:
We are checking if we can remove a user from the system.
"""

import requests

def test_delete_user(base_url):
    # Send request to delete user with ID 1
    response = requests.delete(f"{base_url}/users/1")

    # Check delete was successful (200 or 204 = success/no content)
    assert response.status_code in [200, 204]