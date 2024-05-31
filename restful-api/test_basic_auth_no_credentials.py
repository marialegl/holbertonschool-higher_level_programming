#!/usr/bin/python3

import requests

url = "http://127.0.0.1:5000/basic-protected"
response = requests.get(url)

assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
print("Test passed: /basic-protected without credentials returns 401 Unauthorized")