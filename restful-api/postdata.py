#!/usr/bin/python3


import requests

data = {
        "username": "Maria",
        "name": "Mary",
        "age": 35,
        "city": "San Francisco"}

resp = requests.post('http://localhost:5000/add_user', json=data)
print (resp)

host='localhost', port=5000, 