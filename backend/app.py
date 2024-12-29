from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
SONGS_FILE = 'songs.json'
USERS_FILE = 'users.json'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize files if they don't exist
for file, default in [(SONGS_FILE, {"songs": [], "trending": [], "popular": []}),
                      (USERS_FILE, {"users": [], "playlists": {}})]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump(default, f)

@app.route('/api/homepage', methods=['GET'])
def homepage():
    with open(SONGS_FILE, 'r') as f:
        data = json.load(f)
    return jsonify({
        "totalSongs": len(data["songs"]),
        "trending": data["trending"],
        "popular": data["popular"]
    })

# Add user authentication, playlist management, and upload features here
if __name__ == '__main__':
    app.run(debug=True)