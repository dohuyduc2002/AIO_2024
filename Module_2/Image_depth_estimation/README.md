# Image Depth Estimation Project

This project focuses on estimating the depth of objects in images using deep learning techniques. The project is part of the `Module_2` directory and aims to provide a comprehensive solution for depth estimation from single images. This project uses 3 seperate approaches using Pixel-wise, window-wise and cosine similarity for estimate depth of a image from different point of views

## Project Structure

- `README.md`: Provides an overview and instructions for setting up and running the project.
- `Window_based_inference.ipynb`: A Jupyter notebook that demonstrates the depth estimation process using a window-based inference approach.
- `data/`: Contains sample images and datasets used for training and testing the depth estimation models.
- `utils.py`: Contains utility functions for data preprocessing, algorithms, and visualization.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or later
- Jupyter Notebook
- NumPy
- OpenCV
- PyTorch

## Installation

First, install the necessary Python packages if you haven't already:

```sh
pip install -r requirements.txt