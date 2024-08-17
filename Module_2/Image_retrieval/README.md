# Image Retrieval Project

This project focuses on retrieving similar images from a dataset using various similarity measures. The project is part of the `Module_2` directory and aims to provide a comprehensive solution for image retrieval. Retrieved image is based on CLIP and vectorDB

## Project Structure

- `README.md`: Provides an overview and instructions for setting up and running the project.
- `Simple_img_retrieval/`: Contains scripts and utilities for simple image retrieval methods.
  - `simple_utils.py`: Utility functions for image retrieval using L1, L2, cosine similarity, and correlation coefficient.
  - `simple_query.py`: Functions to read images and perform image retrieval.
- `Enhanced_img_retrieval/`: Contains scripts and utilities for enhanced image retrieval methods.
  - `enhanced_utils.py`: Utility functions for image retrieval using advanced embedding techniques.
- `data/`: Contains sample images and datasets used for training and testing the image retrieval models.
- `utils/`: Contains additional utility scripts for data preprocessing and visualization.
  - `query.py`: Functions to read images and perform image retrieval.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or later
- NumPy
- OpenCV
- PIL
- Matplotlib
- Streamlit
- ChromaDB 

## Installation

First, install the necessary Python packages if you haven't already:

```sh
pip install -r requirements.txt