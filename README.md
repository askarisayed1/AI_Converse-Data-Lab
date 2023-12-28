
# __AIConverse Data Lab - Streamlit Application__

## __Introduction__

> AIConverse Data Lab is a Streamlit-based web application designed to leverage the power of Large Language     Models (LLMs) to interact and analyze data in a conversational manner. This application allows users to upload a CSV file and pose queries to their dataset using natural language processing. The app integrates OpenAI's models through the PandasAI interface, providing an intuitive and powerful tool for data analysis.

__Features__
1. CSV File Upload: Users can upload their data in CSV format.
2. Data Display: Uploaded data is displayed in an interactive table.
3. Conversational Data Query: Users can type natural language queries to interact with their data.
4. Integration with OpenAI: Uses OpenAI's Large Language Models for processing queries.
5. Results Display: The answers to queries are displayed in a user-friendly format.

__Installation__

## ___To set up the AIConverse Data Lab on your local machine, follow these steps:___

1. Clone the Repository: Clone the code repository to your local machine.

2. Environment Setup:

    1. Install Python 3.8+
    2. Use pip install -r requirements.txt
    3. API Key Configuration:

    >. Get an API key from OpenAI. https://platform.openai.com/api-keys

    >. Store the API key in an .env file using the variable name OPENAI_API_KEY.


## __By using Docker:-__
1. docker pull askarisayed/aiconverse:latest
2. To Run the Image-: docker run -d -p 8501:8501 askarisayed/aiconverse:latest
3. To Stop the Running Container - docker stop container_id
4. To get Container ID use docker ps -a


## __Running the Application__:

1. __Run the app using Streamlit: streamlit run your_app.py__

__Usage__
1. Start the Application: Open the application in your web browser.
2. Upload CSV File: Use the file uploader to import your CSV data.
3. View Data: Inspect the uploaded data in the displayed table.
4. cEnter Query: Type your query in the text area provided.
5. Get Results: Click the "Chat with Data" button to process your query and view the results.
Customization
6. You can customize the application by modifying the Streamlit interface, integrating different LLMs, or  expanding the types of queries that can be processed.


## __Conclusion__
AIConverse Data Lab offers a unique way to interact with datasets, making data analysis more accessible and conversational. This application is suitable for data analysts, researchers, and anyone interested in exploring data through natural language queries.


## __Future_Scope-:__

1.Integration of Open-Source Large Language Models (LLMs): To develop a cost-effective approach for data analysis, leveraging open-source LLMs could significantly reduce expenses while maintaining high-quality analytical capabilities.

2. Incorporating Various Data Sources: Enhancing the robustness of the system by adding diverse data sources. This would allow for more comprehensive data analysis and insights, catering to a wider range of data-driven applications.

