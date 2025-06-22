# Use a lightweight Python image
FROM python:3.9-slim

# Create and switch to /app
WORKDIR /app

# Copy only the files we need
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI code
COPY app/ ./app

# Expose the port Cloud Run will use
EXPOSE 8080

# Start Uvicorn, pointing at app/main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--lifespan", "on"]