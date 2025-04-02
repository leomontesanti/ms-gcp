# FastAPI Microservice on Google Cloud Run

## Overview
This is a simple FastAPI-based microservice deployed on **Google Cloud Run**. The service provides a health check endpoint and a root endpoint.

## Features
- Lightweight **FastAPI** framework
- Dockerized for easy deployment
- Deployed on **Google Cloud Run**
- Exposes two endpoints:
  - `/v1/` → Returns a simple message
  - `/v1/health` → Returns a health check status

## Installation & Running Locally

### **1. Clone the repository**
```bash
 git clone <your-repo-url>
 cd fastapi-gcp
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the application**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### **4. Test the API**
Visit:
- http://127.0.0.1:8000/v1/
- http://127.0.0.1:8000/v1/health

## Docker Setup

### **1. Build the Docker image**
```bash
docker build -t fastapi-gcp .
```

### **2. Run the container**
```bash
docker run -p 8000:8000 fastapi-gcp
```

## Deployment to Google Cloud Run

### **1. Authenticate with Google Cloud**
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### **2. Enable required services**
```bash
gcloud services enable run.googleapis.com
```

### **3. Build & Push the Image to Google Container Registry**
```bash
PROJECT_ID=$(gcloud config get-value project)
REGION="us-central1"
docker build -t gcr.io/$PROJECT_ID/fastapi-gcp .
docker push gcr.io/$PROJECT_ID/fastapi-gcp
```

### **4. Deploy to Cloud Run**
```bash
gcloud run deploy fastapi-gcp \
    --image gcr.io/$PROJECT_ID/fastapi-gcp \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated
```

### **5. Get the Public URL**
After deployment, GCP will provide a public URL. Access it in your browser.

## License
This project is licensed under the MIT License.

