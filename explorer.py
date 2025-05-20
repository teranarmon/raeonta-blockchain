from flask import render_template, jsonify
from app import app
import json
import os

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chain")
def chain():
    path = os.path.join(os.path.dirname(__file__), "data/blockchain.json")
    try:
        with open(path, "r") as f:
            blockchain = json.load(f)
        return jsonify(blockchain)
    except:
        return jsonify({"error": "Blockchain tidak tersedia"})
