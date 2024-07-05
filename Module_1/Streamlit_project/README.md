# Streamlit Project Overview

This Streamlit project is part of the `Module_1` directory, focusing on implementing a web application for object detection and word correction using Levenshtein distance. Below is a detailed overview of the project structure and key components.

## Project Structure

- `README.md`: Provides an overview and instructions for setting up and running the project.
- `source/`: Contains the source code for the project.
  - `chatbot.py`: (File not detailed in the provided excerpts)
  - `data/`: Contains data files used by the project.
    - `vocab.txt`: A vocabulary list used for word correction. Loaded by [`load_vocab`](Module_1/Streamlit_project/source/levenshtein_distance.py) function.
  - `levenshtein_distance.py`: Implements the Levenshtein distance algorithm for word correction. It includes functions like [`levenshtein`](Module_1/Streamlit_project/source/levenshtein_distance.py), [`load_vocab`](Module_1/Streamlit_project/source/levenshtein_distance.py), and a [`main`](Module_1/Streamlit_project/source/levenshtein_distance.py) function for the Streamlit interface.
  - `model/`: Contains the model files for object detection.
    - `MobileNetSSD_deploy.caffemodel`: The pre-trained model file.
    - `MobileNetSSD_deploy.prototxt.txt`: The model configuration file.
  - `object_detection.py`: Handles object detection functionalities. It includes functions like [`process_image`](Module_1/Streamlit_project/source/object_detection.py) and [`annotate_image`](Module_1/Streamlit_project/source/object_detection.py), along with a [`main`](Module_1/Streamlit_project/source/object_detection.py) function for the Streamlit interface.

## Key Features

- **Object Detection**: Utilizes the MobileNet SSD model for detecting objects in images. The detection process is handled by the `process_image` function, and the results are annotated on the images by the `annotate_image` function.
- **Word Correction**: Implements the Levenshtein distance algorithm to suggest corrections for misspelled words. The `levenshtein` function calculates the distance between two words, and the `load_vocab` function loads a list of correct words from `vocab.txt`.

## Setup and Execution

To run the Streamlit web application, navigate to the `source` directory and execute the following command:

```sh
streamlit run app.py