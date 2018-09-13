from flask import Flask, request, jsonify
from flask_cors import CORS
import os

import constants

app = Flask(__name__)
cors = CORS(app)


@app.route("/upload")
def upload():
    message = request.args.get("data")
    return "<h1>MESSAGE (GET): " + message + "!!!</h1>"


@app.route("/push", methods=['POST'])
def push():
    req = request.get_json()
    message = req['data']
    return "<h1>MESSAGE (POST): " + message + "!!!</h1>"


@app.route("/")
def hello():
    return "<h1>GET successfully!!!</h1>"


def main():
    host = os.environ.get('IP', constants.SERVICE_IP)
    port = int(os.environ.get('PORT', constants.SERVICE_PORT))
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()