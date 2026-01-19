from flask import Flask, request, Response
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

        text = response.text.strip()

        # Fix double-encoded JSON
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        text = text.encode('utf-8').decode('unicode_escape')

        # Return valid JSON response
        return Response(text, content_type="application/json")

    except Exception as e:
        return Response(json.dumps({"error": str(e)}), content_type="application/json", status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
