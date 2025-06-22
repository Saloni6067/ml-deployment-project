from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = FastAPI()

# Load model
model = tf.keras.models.load_model("app/model.h5")

@app.get("/")
def root():
    return {"message": "MNIST API is running!"}

@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("L")  # grayscale

        image = image.resize((28, 28))  # resize to MNIST format
        img_array = np.array(image) / 255.0  # normalize
        img_array = img_array.reshape(1, 28, 28)  # shape for model

        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)

        return JSONResponse(content={"prediction": int(predicted_class)})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
