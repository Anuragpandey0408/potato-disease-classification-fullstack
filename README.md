# Potato Disease Classification Fullstack

> Updated: API hardening, simple static UI, and Dockerfile added under api/ (branch: feature/api-hardening-and-frontend)

(Original README contents omitted here for brevity — see root README.md for full project description.)

## API (updated)

From the `api/` directory the repository contains a FastAPI app that serves predictions from a Keras model and a small static UI for quick testing.

Quick start (Python):

```bash
cd api
pip install -r requirements.txt
# Ensure the model file is available at ../saved_models/1.keras or set MODEL_PATH env var
python main.py
```

Docker (recommended for consistent environment):

```bash
# from repo root
docker build -t potato-api -f api/Dockerfile .
# mount saved_models directory so the container can access the model
docker run -p 8000:8000 -v $(pwd)/saved_models:/app/../saved_models potato-api
```

Visit http://localhost:8000 to use the simple upload UI.
