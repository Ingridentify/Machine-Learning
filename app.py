from random import shuffle
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

app = FastAPI(
    title="Ingridentify",
    description="API for Ingridentify",
    version="1.0",
    contact={
        "name": "Capstone M296BSY1298",
        "url": "https://github.com/Ingridentify",
    },
)

# set the shuffle off
shuffle = False

model_path = 'model.h5'
model = tf.keras.models.load_model(model_path)

# Define fruit and vegetable classes
class_labels = {
    0: 'Apple', 1: 'Banana', 2: 'Broccoli', 3: 'Carrots', 4: 'Cauliflower',
    5: 'Chili', 6: 'Coconut', 7: 'Cucumber', 8: 'Custard apple', 9: 'Dates',
    10: 'Dragon', 11: 'Egg', 12: 'Garlic', 13: 'Grape', 14: 'Green Lemon',
    15: 'Jackfruit', 16: 'Kiwi', 17: 'Mango', 18: 'Okra', 19: 'Onion',
    20: 'Orange', 21: 'Papaya', 22: 'Peanut', 23: 'Pineapple', 24: 'Pomegranate',
    25: 'Star Fruit', 26: 'Strawberry', 27: 'Sweet Potato', 28: 'Watermelon',
    29: 'White Mushroom'
}

def preprocess_image(image):
    img = Image.open(image.file).convert("RGB")
    img = img.resize((150, 150)) 
    img_array = np.asarray(img)
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0) 
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_array = preprocess_image(file)
        predictions = model.predict(image_array)
        class_index = np.argmax(predictions[0])
        confidence = predictions[0][class_index] * 100
        predicted_item = class_labels.get(class_index, "Unknown Item")

        return JSONResponse(content={
            "predicted_item": predicted_item,
            "confidence": f"{round(confidence, 2)}"
        })

    except Exception as e:
        return JSONResponse(content={
            "error": f"An error occurred: {str(e)}"
        }, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)