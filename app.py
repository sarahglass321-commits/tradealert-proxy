from flask import Flask, request, jsonify
import requests

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

        # Try to safely parse JSON (if valid), else return as text
        try:
            data = response.json()
        except ValueError:
            data = {"raw_response": response.text}

        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
