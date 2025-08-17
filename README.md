Read the **ML-Deployment-Project-Saloni** file for project details
# MNIST Digit Prediction API (FastAPI + TensorFlow)

This project deploys a TensorFlow-trained digit classification model (based on the MNIST dataset) using a FastAPI web server. The server accepts image files via POST requests and returns the predicted digit.

## Project Features

- MNIST digit classification model trained with TensorFlow/Keras.
- FastAPI application for serving predictions.
- Docker container for environment consistency.
- Accepts image file uploads and responds with prediction as JSON.

## Project Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4783c815-0fc0-4eaa-8df9-237de21b5706" />


Make sure you have the following installed:

- Python 3.9
- Docker
- curl (for API testing)
- Git

## Getting Started (Run Locally)

### 1. Clone the Repository

```bash
cd ml-deployment-project
```

### 2. Create a virtual environment
```bash
py -3.9 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install all dependencies
```bash
pip install -r requirements.txt
```
### 4. Build and Run the Docker Image
```bash
docker build --no-cache -t mnist-api-local .
docker run --rm -p 8080:8080 -e PORT=8080 mnist-api-local
```
once it starts running in a seperate terminal run this:
```bash
curl.exe -X POST -F "file=@digit.png" http://localhost:8080/predict-image
```
digit.png is a sample test image which is fetched using get_image.py. You can replace it with anyother grey scale 28x28 pixel image of a handwritten diget or fetch another one using get_image.py.

## To run using GCP
```bash 
curl.exe -X POST -F "file=@digit.png" "https://mnist-gateway-a1xxbu86.uc.gateway.dev/predict-image?key=$your_key”
```
Replace $your_key with your gcp access key 


