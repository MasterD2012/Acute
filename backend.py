from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# In-memory database (use a real database in production)
users = {}
uploads_folder = "uploads"
os.makedirs(uploads_folder, exist_ok=True)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users:
        return jsonify({"message": "Username already exists!"}), 400
    users[username] = password
    return jsonify({"message": "Sign-up successful!"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        return jsonify({"message": f"Welcome back, {username}!"}), 200
    return jsonify({"message": "Invalid username or password!"}), 401

@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username")
    if username not in users:
        return jsonify({"message": "User not found!"}), 404
    if "file" not in request.files:
        return jsonify({"message": "No file uploaded!"}), 400
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(uploads_folder, filename))
    return jsonify({"message": f"File '{filename}' uploaded successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
