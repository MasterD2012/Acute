from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for demonstration
users = {"user1": "password1"}
playlists = {"user1": ["My Playlist", "Workout Jams"]}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful", "playlists": playlists.get(username, [])}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/add_playlist", methods=["POST"])
def add_playlist():
    data = request.json
    username = data.get("username")
    playlist_name = data.get("playlist")
    if username in users:
        playlists[username].append(playlist_name)
        return jsonify({"message": "Playlist added successfully"}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
