from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

# File Path Setup : picking video file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "..", "lot_status.json")

@app.route("/data")
def data():
    print("DATA ROUTE HIT")   # 👈 ADD THIS

    if os.path.exists(video_path):
        print("FILE FOUND")   # 👈 ADD THIS
        with open(video_path, "r") as f:
            return jsonify(json.load(f))

    print("FILE NOT FOUND")   # 👈 ADD THIS
    return jsonify({"available": 0, "total": 0, "spot_statuses": []})

if __name__ == "__main__":
    app.run(debug=True)