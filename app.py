from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/tradealert', methods=['GET'])
def tradealert():
    base_url = "https://quant.trade-alert.com/"
    params = {
        "cmd": request.args.get("cmd", "top"),
        "apikey": "c3Ur9P4izmE9Ig",
        "output": request.args.get("output", "json"),
        "symbol": request.args.get("symbol"),
        "where": request.args.get("where")
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()

        # Clean and fix escaped JSON
        text = response.text.strip()
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]  # remove outer quotes
        text = text.replace('\\"', '"').replace('\\\\', '\\')

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = {"raw_text": text}

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
