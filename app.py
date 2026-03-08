from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained CNN model
model = tf.keras.models.load_model("maize_disease_model.h5")

classes = [
    "Healthy",
    "Corn Rust",
    "Northern Leaf Blight",
    "Gray Leaf Spot"
]

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    confidence = None
    filepath = None

    if request.method == "POST":

        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            img = image.load_img(filepath, target_size=(224,224))
            img_array = image.img_to_array(img)/255.0
            img_array = np.expand_dims(img_array, axis=0)

            pred = model.predict(img_array)

            result_index = np.argmax(pred)
            prediction = classes[result_index]
            confidence = round(np.max(pred) * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image=filepath
    )


if __name__ == "__main__":
    app.run(debug=True)