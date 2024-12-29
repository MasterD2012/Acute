from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
SONGS_FILE = 'songs.json'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
if not os.path.exists(SONGS_FILE):
    with open(SONGS_FILE, 'w') as f:
        json.dump({"songs": [], "trending": [], "popular": []}, f)

@app.route('/api/homepage', methods=['GET'])
def homepage():
    with open(SONGS_FILE, 'r') as f:
        data = json.load(f)
    return jsonify({
        "totalSongs": len(data["songs"]),
        "trending": data["trending"],
        "popular": data["popular"]
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    with open(SONGS_FILE, 'r+') as f:
        data = json.load(f)
        data["songs"].append(file.filename)
        f.seek(0)
        json.dump(data, f, indent=4)
    return jsonify({'message': 'File uploaded successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)