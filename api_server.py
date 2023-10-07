from flask import Flask, request, jsonify
from crypto_prices import print_stats
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/stats", methods=["POST"])
def crypto_api():
    data = request.get_json()

    if "name" not in data:
        return jsonify({"error": "Missing name parameter"}), 400

    name = data["name"]
    result = print_stats(name)

    return result

if __name__ == "__main__":
    app.run(port=5000)