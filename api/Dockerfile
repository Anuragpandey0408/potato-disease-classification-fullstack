FROM python:3.11-slim

WORKDIR /app

# system deps for pillow
RUN apt-get update && apt-get install -y build-essential libjpeg-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

COPY api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy API code
COPY api/ ./

# ensure saved_models are copied or mounted at runtime
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
