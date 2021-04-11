from flask import Flask, request, jsonify, redirect, url_for, flash
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

import os
from image_identifier import getDetectedObjects

app = Flask(__name__)
api = Api(app=app)


def allowed_file(filename):
    allowed_extensions = set(['jpg', 'jpeg', 'png'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


class Home(Resource):
    def get(self):
        return jsonify({"message": 'Welcome to Object Recognition API!'})


class ImageReceiver(Resource):
    def post(self):
        dirname = 'test_images'
        os.mkdir(os.path.join(os.getcwd(), dirname))
        if 'image' not in request.files:
            return jsonify({'message': 'No image found!'})
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(dirname,
                                   f'image.{filename.split(".")[-1]}'))
            detectedObjects = getDetectedObjects()
            return jsonify({'detected_objects': detectedObjects})
            # return redirect(url_for('imagereceiver', filename=filename))


api.add_resource(Home, '/')
api.add_resource(ImageReceiver, '/image')
