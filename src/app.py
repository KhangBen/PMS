from flask import Flask, render_template, jsonify
import json
import os
import time

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

# JSON file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "..", "lot_status.json")

@app.route("/data")
def data():
    print("DATA ROUTE HIT") 

    if os.path.exists(JSON_PATH):
        print("FILE FOUND") 
        with open(JSON_PATH, "r") as f:
            return jsonify(json.load(f))

    # fallbacl (offline system)
    return jsonify({
        "available": 0,
        "total": 41,
        "spot_statuses": [False] * 41,
        "system_active": False,
        "last_updated": time.time()
    })

if __name__ == "__main__":
    app.run(debug=True)