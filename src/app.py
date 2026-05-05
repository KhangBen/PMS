from flask import Flask, render_template, jsonify, request
import json
import os
import time

app = Flask(__name__)

@app.route("/")
def list_view():
    return render_template("list.html")

@app.route("/map")
def map_view():
    lot = request.args.get("lot", "main")  # default = main
    return render_template("map.html", lot=lot)

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

    # fallback (offline system)
    return jsonify({
        "available": 0,
        "total": 41,
        "spot_statuses": [False] * 41,
        "system_active": False,
        "last_updated": time.time()
    })

if __name__ == "__main__":
    app.run(debug=True)