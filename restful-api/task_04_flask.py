#!/usr/bin/python3
"""Set up a Flask application and run a development server.
Routes with Flask to respond to different endpoints.
Serve JSON data using Flask.
Handling and response formation in Flask.
Handle POST requests to add new data to the API.
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return jsonify({"status": "OK"})


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    user_to_add = request.get_json()
    username = user_to_add.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_to_add
    return jsonify({"message": "User added", "user": user_to_add}), 201


if __name__ == "__main__":
    app.run(debug=True)
