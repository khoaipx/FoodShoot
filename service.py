from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64

import constants
import utils

app = Flask(__name__)
cors = CORS(app)
utils.create_dir(constants.UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = constants.UPLOAD_FOLDER


@app.route("/upload", methods=["POST"])
def upload():
    base64_img = None
    img_file = None

    img_path = os.path.join(constants.UPLOAD_FOLDER, utils.generate_random_string())

    if request.files is None and request.json is None:
        return jsonify({'error': 'InvalidImage', 'message': 'Failed to retrieve image from `image`.'})

    if request.files is not None:
        img_file = request.files.get('image', None)  # image file

    if request.json is not None:
        base64_img = request.json.get('image', None)  # image base64

    if base64_img is not None:
        with open(img_path, "wb") as fh:
            fh.write(base64.decodestring(base64_img.encode()))

    if img_file is not None:
        img_file.save(img_path)

    print('Img save to: {}'.format(img_path))

    try:
        # parser = importlib.import_module('services.' + service, 'services')
        # solved = parser.predictCaptcha(captchaFilePath)
        # print('Solved: {}'.format(solved))
        # print('Remove file: {}'.format(img_path))
        # os.remove(img_path)

        return jsonify({'result': "success", "image": img_path})
    except Exception as e:
        return jsonify({'result': 'failed', 'message': str(e)})


@app.route("/get")
def get():
    message = request.args.get("data")
    return "<h1>MESSAGE (GET): " + message + "!!!</h1>"


@app.route("/post", methods=['POST'])
def post():
    req = request.get_json()
    message = req['data']
    return jsonify({"result": "Success", "message": message})


@app.route("/")
def hello():
    return "<h1>GET successfully!!!</h1>"


def main():
    host = os.environ.get('IP', constants.SERVICE_IP)
    port = int(os.environ.get('PORT', constants.SERVICE_PORT))
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()