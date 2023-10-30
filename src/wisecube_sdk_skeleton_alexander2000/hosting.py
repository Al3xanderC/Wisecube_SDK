from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    payload = request.data
    headers = request.headers

    response_data = {
        "payload": payload.decode('utf-8'),
        "headers": dict(headers)
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)
