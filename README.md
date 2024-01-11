# Gemini Pro Streamlit App

## Introduction

The Gemini Pro Streamlit App is a powerful tool that leverages the capabilities of Google's latest large language model, Gemini Pro, to provide users with comprehensive answers to their questions based on information extracted from multiple PDF documents.

## Features

- **Multiple PDF Reading:** The app allows users to upload and read data from multiple PDF documents simultaneously. This enables users to consolidate information from various sources and gain insights across different documents.

- **FAISS Database Integration:** The app utilizes the FAISS (Facebook AI Similarity Search) database to store the embeddings of the PDF documents. This enables efficient and fast retrieval of relevant information based on user queries.

- **Question Answering:** Users can ask questions related to the information contained in the uploaded PDF documents. The app utilizes Gemini Pro's language understanding and reasoning capabilities to generate comprehensive and informative answers.

- **Contextualized Responses:** The app provides contextualized responses by referencing the specific sections or pages of the PDF documents that contain the relevant information. This helps users understand the context and source of the answers.

- **User-Friendly Interface:** The app features a user-friendly interface that makes it easy for users to upload PDF documents, ask questions, and receive answers. The app is designed to be accessible and intuitive for users of all levels.

## Usage

To use the app, follow these simple steps:

1. Clone the repository to your local machine using the following command:

git clone https://github.com/your-username/gemini-pro-streamlit-app.git


2. Install the required Python packages by running the following command in the project directory:

pip install -r requirements.txt


3. Start the Streamlit app by running the following command in the project directory:

streamlit run app.py


4. Once the app is running, you can access it by visiting the following URL in your browser:

http://localhost:8501


5. Upload the PDF documents you want to analyze by clicking the "Choose Files" button.

6. Ask your questions in the "Ask a Question" field.

7. Click the "Submit" button to receive answers to your questions.

## Deployment

To deploy the app, you can follow these steps:

1. Create a Streamlit Cloud account if you don't have one already.

2. Log in to your Streamlit Cloud account and click on the "New App" button.

3. Select the "Upload Code" option and choose the directory where your app's code is located.

4. Click on the "Deploy" button to start the deployment process.

5. Once the deployment is complete, you will receive a link to your deployed app.

## Contributing

Contributions to this project are welcome and appreciated. To contribute, please follow these guidelines:

1. Fork the repository to your GitHub account.

2. Create a new branch for your changes.

3. Make your changes and commit them to your branch.

4. Open a pull request to merge your changes into the main branch.

## License

This project is licensed under the MIT License.
