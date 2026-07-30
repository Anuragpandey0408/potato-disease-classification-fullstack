# 🥔 Potato Disease Classification Fullstack

🚧 **Work In Progress** 🚧  
This repository is under active development and not yet feature-complete. Contributions, suggestions, and feedback are welcome.

---

## ✨ Features

- 📷 **Image Upload API** - Upload potato leaf images for disease detection
- ⚡ **Real-time Prediction** - Fast inference using trained TensorFlow model
- 🔗 **RESTful API** - Simple HTTP endpoints for integration
- 🧠 **Disease Classification** - Detects Early Blight, Late Blight, and Healthy leaves
- 📊 **Confidence Scoring** - Returns prediction confidence levels
- 🏥 **Health Check Endpoint** - API status monitoring

### Planned Features
- 📊 Dashboard for viewing results and history
- 🖥️ Web frontend interface
- 📈 Model performance metrics

---

## 🛠️ Tech Stack

- **Backend API:** FastAPI, Python
- **Machine Learning:** TensorFlow/Keras, NumPy, Pillow
- **Model Training:** Jupyter Notebook, Matplotlib
- **API Server:** Uvicorn
- **Other Tools:** REST API, GitHub Actions

---

## 🚀 Setup Instructions

> **Note:** The setup steps below may change as development progresses.

### Prerequisites

- Python 3.8+ (compatible with TensorFlow 2.20.0)
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/Anuragpandey0408/potato-disease-classification-fullstack.git
cd potato-disease-classification-fullstack
```

### API Setup

```bash
cd api
pip install -r requirements.txt
python main.py
```

The API will be available at `http://localhost:8000`

### Model Training (Optional)

If you want to retrain the model:

```bash
cd training
# Open potato-disease-classification-model.ipynb in Jupyter Notebook
jupyter notebook potato-disease-classification-model.ipynb
```

---

## 🧑‍💻 Usage

### API Endpoints

The API will be running at `http://localhost:8000`

- **Health Check:** `GET /ping`
- **Disease Prediction:** `POST /predict`

### Making Predictions

1. Start the API server (see Setup Instructions above)
2. Send a POST request to `/predict` with a potato leaf image file
3. The API will return the disease classification and confidence score

### Example using curl:

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path/to/your/potato_leaf_image.jpg"
```

### Response Format:

```json
{
  "class": "Early Blight",
  "confidence": 0.95
}
```

### Supported Disease Classes:
- **Early Blight**
- **Late Blight** 
- **Healthy**

---

## 🏗️ Project Structure

```
potato-disease-classification-fullstack/
├── api/                    # FastAPI backend server
│   ├── main.py            # Main API application
│   └── requirements.txt   # Python dependencies
├── training/              # Model training notebooks and data
│   ├── potato-disease-classification-model.ipynb
│   └── PlantVillage/      # Dataset directory
├── saved_models/          # Trained model files
│   └── 1.keras           # Pre-trained TensorFlow model
└── README.md             # Project documentation
```

---

## 🧠 Model Information

- **Model Type:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow/Keras
- **Input Size:** 256x256x3 (RGB images)
- **Classes:** 3 (Early Blight, Late Blight, Healthy)
- **Training Data:** PlantVillage dataset
- **Model File:** `saved_models/1.keras`

---

## 🤝 Contributing

Contributions are encouraged! Please fork the repository and open a pull request, or create an issue for discussion.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Maintainer: [Anuragpandey0408](https://github.com/Anuragpandey0408)  
Email: anuragpandey077269@gmail.com

---

*Potato Disease Classification Fullstack – Empowering agriculture with AI.*
