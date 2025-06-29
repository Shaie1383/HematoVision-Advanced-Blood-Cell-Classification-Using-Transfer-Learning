from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)
model = load_model("blood_cell.h5")

classes = ['Eosinophil', 'Lymphocyte', 'Monocyte', 'Neutrophil']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    file_path = 'static/' + file.filename
    file.save(file_path)

    image = cv2.imread(file_path)
    image = cv2.resize(image, (224,224))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    prediction = model.predict(image)
    predicted_class = classes[np.argmax(prediction)]
    confidence = float(np.max(prediction)) * 100

    result = {
        "class_name": predicted_class,
        "confidence": f"{confidence:.2f}%",
        "image_path": file.filename
    }

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
