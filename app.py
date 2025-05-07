from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy/getTotalTradeReal', methods=['POST'])
def proxy_total_trade_real():
    try:
        # Payload gốc
        payload = request.get_json()

        # Gọi đến API thật
        response = requests.post(
            url="https://stocktraders.vn/service/data/getTotalTradeReal",
            headers={"Content-Type": "application/json"},
            json=payload
        )

        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5007)
