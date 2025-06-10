# Placeholder for Backend Developer task
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_video():
    # TODO: Handle video upload, save to disk
    # Save mock metrics to SQLite
    return jsonify({"video_id": 1, "status": "uploaded"})

@app.route("/metrics/<int:video_id>", methods=["GET"])
def get_metrics(video_id):
    # TODO: Query SQLite, return metrics
    return jsonify({"video_id": video_id, "arm_angle": 75.2})

if __name__ == "__main__":
    app.run(debug=True)
