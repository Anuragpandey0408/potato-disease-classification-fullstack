from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from io import BytesIO
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
MODEL_PATH = os.environ.get("MODEL_PATH", "../saved_models/1.keras")
IMAGE_SIZE = int(os.environ.get("IMAGE_SIZE", 256))
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

app = FastAPI(title="Potato Disease Classifier")

# Allow simple CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve a tiny static UI from api/static
if os.path.isdir("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")


_model = None

def load_model(path: str):
    global _model
    if _model is None:
        try:
            logger.info(f"Loading model from: {path}")
            _model = tf.keras.models.load_model(path)
            logger.info("Model loaded successfully.")
        except Exception as e:
            logger.exception("Failed to load model")
            raise
    return _model

def preprocess_image(data: bytes, image_size: int = IMAGE_SIZE) -> np.ndarray:
    try:
        img = Image.open(BytesIO(data)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Unable to read image file")
    # Resize and scale
    img = img.resize((image_size, image_size))
    arr = np.asarray(img).astype("float32") / 255.0
    # model expects batch dimension
    return np.expand_dims(arr, 0)

@app.get("/health")
async def health():
    status = {"status": "ok"}
    try:
        if os.path.exists(MODEL_PATH):
            status["model_path_exists"] = True
        else:
            status["model_path_exists"] = False
    except Exception:
        status["model_path_exists"] = False
    return status

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Basic content-type check
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    data = await file.read()
    img_batch = preprocess_image(data)

    try:
        model = load_model(MODEL_PATH)
    except Exception:
        raise HTTPException(status_code=500, detail="Model failed to load on server")

    try:
        preds = model.predict(img_batch)
    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Model prediction failed")

    predicted_index = int(np.argmax(preds[0]))
    predicted_class = CLASS_NAMES[predicted_index] if predicted_index < len(CLASS_NAMES) else str(predicted_index)
    confidence = float(np.max(preds[0]))

    return JSONResponse({"class": predicted_class, "confidence": confidence})

# Optional: simple root that returns the UI if not mounted
@app.get("/", response_class=HTMLResponse)
async def root():
    if os.path.exists("static/index.html"):
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<html><body><h3>Potato Disease Classifier API</h3><p>Visit /predict to POST an image.</p></body></html>")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
