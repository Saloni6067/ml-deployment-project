FROM python:3.9
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
WORKDIR /app
COPY . /app
# Expose port 8080 (Cloud Run default) and run Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]