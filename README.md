# AI_Converse-Data-Lab
LLM Powered Data Analysis
AIConverse Data Lab - Streamlit Application
Introduction
AIConverse Data Lab is a Streamlit-based web application designed to leverage the power of Large Language Models (LLMs) to interact and analyze data in a conversational manner. This application allows users to upload a CSV file and pose queries to their dataset using natural language processing. The app integrates OpenAI's models through the PandasAI interface, providing an intuitive and powerful tool for data analysis.

Features
CSV File Upload: Users can upload their data in CSV format.
Data Display: Uploaded data is displayed in an interactive table.
Conversational Data Query: Users can type natural language queries to interact with their data.
Integration with OpenAI: Uses OpenAI's Large Language Models for processing queries.
Results Display: The answers to queries are displayed in a user-friendly format.
Installation
To set up the AIConverse Data Lab on your local machine, follow these steps:

Clone the Repository: Clone the code repository to your local machine.

Environment Setup:

Install Python and necessary packages (Streamlit, pandas, matplotlib, dotenv).
Use pip install for package installation.
API Key Configuration:

Get an API key from OpenAI.
Store the API key in an .env file using the variable name OPENAI_API_KEY.
Running the Application:

Run the app using Streamlit: streamlit run your_app.py
Usage
Start the Application: Open the application in your web browser.
Upload CSV File: Use the file uploader to import your CSV data.
View Data: Inspect the uploaded data in the displayed table.
Enter Query: Type your query in the text area provided.
Get Results: Click the "Chat with Data" button to process your query and view the results.
Customization
You can customize the application by modifying the Streamlit interface, integrating different LLMs, or expanding the types of queries that can be processed.

Conclusion
AIConverse Data Lab offers a unique way to interact with datasets, making data analysis more accessible and conversational. This application is suitable for data analysts, researchers, and anyone interested in exploring data through natural language queries.
