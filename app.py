from flask import Flask, request, jsonify, redirect, url_for, flash
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

import os
from image_identifier import getDetectedObjects
from decouple import config

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
        os.mkdir(os.path.join(os.getcwd(), config('IMG_DIR')))
        if 'image' not in request.files:
            return jsonify({'message': 'No image found!'})
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(config('IMG_DIR'),
                                   f'image.{filename.split(".")[-1]}'))
            detectedObjects = getDetectedObjects()
            return jsonify({'detected_objects': detectedObjects})

api.add_resource(Home, '/')
api.add_resource(ImageReceiver, '/image')
