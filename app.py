from flask import Flask, request, jsonify, render_template
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model("brain_tumor_model.h5")
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']

def preprocess(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    img_array = preprocess(filepath)

    pred = model.predict(img_array)
    prediction = class_names[np.argmax(pred)]
    confidence = float(np.max(pred) * 100)

    return jsonify({
        "prediction": prediction,
        "confidence": confidence,
        "image": file.filename,
        "probs": pred.tolist()[0]
    })

if __name__ == "__main__":
    app.run(debug=True)