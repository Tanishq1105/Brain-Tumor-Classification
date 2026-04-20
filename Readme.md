# 🧠 Brain Tumor Detection & Classification System

An end-to-end deep learning project that detects and classifies brain tumors from MRI images using a CNN model, deployed via a Flask web application with an interactive frontend.

---

## 🚀 Features

* 🔍 Upload MRI images for analysis
* 🧠 Predict tumor type:

  * Glioma
  * Meningioma
  * Pituitary
  * No Tumor
* 📊 Confidence score + class probabilities
* ⚡ Real-time prediction (no page reload)
* 🌐 Interactive web dashboard (Flask + JavaScript)
* 🖼️ Image preview with results

---

## 🧠 Model Details

* Architecture: CNN (TensorFlow/Keras)
* Input Size: 224 × 224
* Classes: 4
* Accuracy: ~75% (Test Set)

---

## 🏗️ Tech Stack

* **Backend:** Python, Flask
* **ML/DL:** TensorFlow, Keras
* **Frontend:** HTML, CSS, JavaScript
* **Other:** NumPy, PIL

---

## 📁 Project Structure

```bash
brain_tumor_project/
│
├── app.py
├── brain_tumor_model.h5
├── static/
│   └── uploads/
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/brain-tumor-project.git
cd brain-tumor-project
```

### 2️⃣ Create environment (recommended)

```bash
conda create -n brain_tumor_env python=3.10
conda activate brain_tumor_env
```

### 3️⃣ Install dependencies

```bash
pip install tensorflow flask numpy pillow
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📸 Demo

*(Add screenshots here)*

Example:

* Upload MRI image
* Get prediction + confidence
* View probability distribution

---

## 🧠 How It Works

1. User uploads MRI image
2. Image is preprocessed (resize + normalize)
3. CNN model predicts probabilities
4. Flask API returns prediction
5. Frontend displays results dynamically

---

## 📈 Future Improvements

* 🔥 Use transfer learning (EfficientNet, ResNet)
* 🧠 Add Grad-CAM (Explainable AI)
* 📊 Improve accuracy with larger dataset
* 🌍 Deploy online (Render / AWS)
* 🖼️ Add segmentation (tumor localization)

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be used for real medical diagnosis.

---

## 👨‍💻 Author

**Tanishq Kumar Sinha**



