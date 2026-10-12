
from flask import Flask, request, jsonify
from pathlib import Path
from datetime import datetime, timezone
import re

app = Flask(__name__)
DATA_FILE = Path("simulation_log.txt")


@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json(silent=True) or {}

    cardholder = str(data.get("cardholder", "")).strip()
    demo_reference = str(data.get("demo_reference", "")).strip()
    demo_expiry = str(data.get("demo_expiry", "")).strip()
    demo_code = str(data.get("demo_code", "")).strip()

    if not all([cardholder, demo_reference, demo_expiry, demo_code]):
        return jsonify({"message": "Please complete all demo fields."}), 400

    # Accept only explicitly fictional training values.
    if not re.fullmatch(r"DEMO-[0-9]{4}", demo_reference):
        return jsonify({
            "message": "Use a demo reference such as DEMO-1234."
        }), 400

    if not re.fullmatch(r"DEMO", demo_code):
        return jsonify({
            "message": "Use DEMO as the sample security code."
        }), 400

    if not re.fullmatch(r"[A-Za-z ]{1,60}", cardholder):
        return jsonify({
            "message": "Use a fictional name containing letters only."
        }), 400

    if not re.fullmatch(r"(0[1-9]|1[0-2])/[0-9]{2}", demo_expiry):
        return jsonify({
            "message": "Use a sample expiry date such as 12/30."
        }), 400

    timestamp = datetime.now(timezone.utc).isoformat()

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"{timestamp} | Simulation submitted | "
            f"Reference: {demo_reference}\n"
        )

    return jsonify({
        "message": "Training submission recorded. No real card data was collected."
    }), 200


if __name__ == "__main__":
    DATA_FILE.touch(exist_ok=True)
    app.run(host="127.0.0.1", port=8000, debug=False)

