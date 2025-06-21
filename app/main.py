from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

app = FastAPI()
model = tf.keras.models.load_model("app/model.h5")  # load your MNIST model

def read_imagefile(file_bytes):
    img = Image.open(BytesIO(file_bytes)).convert("L")     # grayscale
    img = img.resize((28,28))
    arr = np.expand_dims(np.array(img) / 255.0, axis=(0, -1))
    return arr

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    data = await file.read()
    image = read_imagefile(data)
    preds = model.predict(image).tolist()[0]
    predicted_class = int(np.argmax(preds))
    return {"predictions": preds, "class": predicted_class}
