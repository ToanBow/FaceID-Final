from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2, numpy as np, pickle, os
import face_recognition

app = Flask(__name__)
CORS(app)

ENCODING_FILE = "encodings.pkl"

with open(ENCODING_FILE, "rb") as f:
    known_encodings, known_names = pickle.load(f)

@app.route("/api/recognize", methods=["POST"])
def recognize():
    if 'image' not in request.files:
        return jsonify({"error": "No image"}), 400

    file = request.files["image"].read()
    img_np = np.frombuffer(file, np.uint8)
    frame = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encs = face_recognition.face_encodings(rgb, boxes)

    results = []
    for enc in encs:
        dists = face_recognition.face_distance(known_encodings, enc)
        name = "Unknown"
        if len(dists) > 0 and min(dists) < 0.5:
            name = known_names[np.argmin(dists)]
        results.append(name)

    return jsonify({"names": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
