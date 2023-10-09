from flask import Flask, request, jsonify
from crypto_stats import calculate_stats
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/stats", methods=["POST"])
def crypto_api():
    data = request.get_json()

    if "name" not in data or data["name"] =="":
        return jsonify({"error": "Missing name parameter"}), 400

    name = data["name"]
    result = calculate_stats(name)

    return result

if __name__ == "__main__":
    app.run(port=5000)