# RAG Project Overview

This project, located in the `RAG_project` folder, leverages the vicuna-7b language model (LLM) for a question-answering system specifically designed to work with PDF files. Utilizing the Retrieval-Augmented Generation (RAG) approach, the system aims to provide accurate answers by retrieving relevant information from the provided PDF documents.

## Key Features

- **Language Model**: Utilizes `vicuna-7b-v1.5`, a powerful language model, for generating answers.
- **File Processing**: Supports PDF file uploads for question-answering tasks.
- **RAG Approach**: Employs Retrieval-Augmented Generation to enhance answer accuracy by retrieving relevant information from the uploaded documents.

## Getting Started

To get started with this project, follow the steps below:

1. **Clone the Repository**: Ensure you have the project cloned to your local machine.
2. **Install Dependencies**: A `requirements.txt` file will be provided. Install the necessary dependencies by running `pip install -r requirements.txt` in your terminal.
3. **Run the Application**: Navigate to the `RAG_project` directory and run `app.py` to start the application.

## Usage

1. **Upload a PDF**: Upon starting the application, you will be prompted to upload a PDF file.
2. **Ask Questions**: After uploading, you can start asking questions related to the content of the PDF file.
3. **Receive Answers**: The system will process your questions and provide answers based on the content of the uploaded PDF.

## Requirements

The project requires the following main dependencies:

- `torch`
- `transformers`
- `chainlit`
- `langchain`

A detailed list of all dependencies will be provided in the `requirements.txt` file.

To develop a demon using ngrok, install localtunnel using npm in `localtunnel.txt` file

## To host a local run using ngrok, follow this instructions
1. Create an account on ngrok
2. Get personal secret authentication key
3. Running all code block **Do not cancel notebook run during this process**
4. Click on `Your app is available at http://localhost:8000` to accessing your demo

This magic method will create an UI file using chainlit
```python
%%writefile app.py
```
