from flask import Flask, request, jsonify
from model_logic import predict_image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Run AI detection
    result = predict_image(file_path)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)