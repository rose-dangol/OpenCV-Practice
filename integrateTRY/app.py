from flask import Flask, request, jsonify
from flask_cors import CORS
import face_recognition
import numpy as np
import base64
import cv2
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/detect-face', methods=['POST'])
def detect_face():
    data = request.get_json()
    img_data = data['image']
    img_bytes = base64.b64decode(img_data.split(',')[1])
    img = Image.open(BytesIO(img_bytes))
    img_np = np.array(img)

    # Convert from RGB to BGR
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    face_locations = face_recognition.face_locations(img_cv)
    return jsonify({'faces_detected': len(face_locations)})

if __name__ == '__main__':
    app.run(port=5000)
