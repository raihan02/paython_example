from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    device_token = data.get('device_token')
    youtube_url = data.get('https://www.youtube.com/watch?v=l2hA8g1cNvQ')
    user_id = data.get('id')

    if not device_token or not youtube_url or not user_id:
        return jsonify({"error": "Invalid input data"}), 400

    response = requests.post(
        'https://api.topmediai.com/v1/cover',
        headers={
            'accept': 'application/json',
            'x-api-key': 'f2eaeb62394949de809bdb31e7707c58',
        },
        files={
            'singer_id': (None, '63'),
            'youtube_url': (None, youtube_url),
            'tran': (None, '0'),
            'file': ('', b'')
        }
    )

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to process request"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
