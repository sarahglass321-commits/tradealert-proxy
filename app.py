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
    r = requests.get("https://quant.trade-alert.com", params=params, timeout=10)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
