# REST API Automation Test Suite (Python + Pytest)

## Overview
This project is a Python + Pytest-based REST API automation test suite designed to validate CRUD operations (GET, POST, PUT, DELETE) against a public REST API.

The goal of this project is to demonstrate practical QA automation skills including API testing, assertions, and test structuring using Pytest.

---

## Tech Stack
- Python 3
- Pytest
- Requests

---

## API Used
https://jsonplaceholder.typicode.com/

---

## What This Project Tests

### GET Users
- Validates API returns a list of users
- Confirms response status is 200
- Ensures response body is not empty

### POST Create User
- Validates user creation request
- Confirms API response returns correct data

### PUT Update User
- Validates updating an existing user
- Confirms response reflects updated data

### DELETE User
- Validates user deletion request
- Confirms successful response status

---
How to Run Tests
pytest -v

Key QA Concepts Practiced
REST API testing
CRUD operations validation
Status code assertions
JSON response validation
Pytest test structure
Fixtures (conftest.py)

Purpose
This project was built to practice real-world QA automation skills and demonstrate API testing capability for junior QA roles.
