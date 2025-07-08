import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERNAME = "2cYS43oV1US3OelcXJY4Oxbv"
PASSWORD = "6lSMkoJtwuEna7RRb3Q5GhnN"

@app.route('/races')
def get_races():
    response = requests.get(
        "https://api.theracingapi.com/races",
        auth=(USERNAME, PASSWORD)
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
