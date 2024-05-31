#!/usr/bin/python3
"""Set up a Flask application and run a development server.
Routes with Flask to respond to different endpoints.
Serve JSON data using Flask.
Handling and response formation in Flask.
Handle POST requests to add new data to the API.
"""


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route('/')
def home():
    return "¡Bienvenido a la API de Flask!"


@app.route('/data')
def get_users():
    return jsonify(users)


@app.route('/status')
def status():
    return (jsonify({"status": "OK"}))


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not found"}), 404)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Bad request, 'username' is required"}), 400
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = data
    return (jsonify({"message": "User added successfully",
                    "user": users[username]}), 201)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
