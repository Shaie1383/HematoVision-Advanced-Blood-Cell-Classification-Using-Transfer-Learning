# 🧬 HematoVision: Advanced Blood Cell Classification Using Transfer Learning

**HematoVision** is a deep learning-powered web application designed to classify microscopic images of blood cells into one of four categories:

- 🔴 **Eosinophil**
- 🟢 **Lymphocyte**
- 🟡 **Monocyte**
- 🔵 **Neutrophil**

This intelligent diagnostic tool leverages **Transfer Learning** with **MobileNetV2** to deliver high-accuracy predictions in real-time, wrapped in a clean and intuitive **Flask**-based web interface.

---

## 🚀 How It Works

1. **Upload** a microscopic image of a blood cell.
2. The **model** processes the image using deep learning.
3. You **get** the predicted class along with a preview of the uploaded image.

This makes HematoVision an ideal assistant for biomedical learners, educators, and early-stage researchers.

---

## ✨ Features

- ✅ Real-time image classification  
- 🧪 Built-in preprocessing pipeline with OpenCV  
- 📊 Predicts 4 blood cell types with MobileNetV2  
- 🔧 Lightweight Flask web app  
- 🖼️ Visual result display

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Jinja2  
- **Backend**: Python, Flask  
- **Deep Learning**: TensorFlow, Keras, MobileNetV2  
- **Tools**: OpenCV, NumPy, Matplotlib  

---

## 📁 Project Structure

```plaintext
├── static/                  # CSS/JS/Image files
├── templates/              # HTML Templates
│   ├── home.html
│   └── result.html
├── BloodCell.ipynb         # Model training notebook
├── BloodCell.h5            # Trained model
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
💻 Run Locally
Clone the repo

git clone https://github.com/your-username/hematovision.git
cd hematovision
Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies


pip install -r requirements.txt
Run the app


python app.py
🖼️ Sample Output

✅ Real-time prediction

✅ Uploaded image display

✅ Predicted class shown clearly

(Add your own image here)

🔮 Future Enhancements

🧠 Add more blood cell types

📱 Deploy as a mobile app

🧪 Add confidence score and probability chart

🌐 Host on cloud (e.g., Heroku, AWS)

🙏 Acknowledgments

SmartInternz AI Virtual Internship Program

Kaggle Blood Cell Dataset

OpenAI GPT & ChatGPT for assistance in planning and documentation

👩‍💻 Created by Team LTVIP2025TMID47286 — Shaista Mulla
