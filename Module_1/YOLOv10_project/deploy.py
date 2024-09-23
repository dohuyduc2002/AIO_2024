import streamlit as st
import cv2
import numpy as np
from PIL import Image
import streamlit as st
from ultralytics import YOLOv10
<<<<<<< Updated upstream
import torch
=======
>>>>>>> Stashed changes

MODEL_PATH = "./models/best.pt"


def process_image(image):
    model = YOLOv10(MODEL_PATH)
    result = model(image)[0]
<<<<<<< Updated upstream
    result.save('./output.png')
=======
    result.save('./predicts/output.png')
>>>>>>> Stashed changes


def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption="Uploaded Image")

        image = Image.open(file)
        image = np.array(image)
        process_image(image)
<<<<<<< Updated upstream
        predict_image = cv2.imread('./output.png')
=======
        predict_image = cv2.imread('./predicts/output.png')
>>>>>>> Stashed changes
        st.image(predict_image, caption="Predict Image")


if __name__ == "__main__":
    main()