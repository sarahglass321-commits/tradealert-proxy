from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/tradealert")
def tradealert():
    params = {
        "cmd": request.args.get("cmd", "top"),
        "output": request.args.get("output", "json"),
        "symbol": request.args.get("symbol"),
        "where": request.args.get("where"),
        "apikey": "c3Ur9P4izmE9Ig"
    }

    try:
        r = requests.get("https://quant.trade-alert.com", params=params, timeout=10)
        try:
            return jsonify(r.json())
        except ValueError:
            return {"error": "Response not valid JSON", "text": r.text}, r.status_code
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
