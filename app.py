import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI
import matplotlib
matplotlib.use('TkAgg')  # Replace 'TkAgg' with 'Qt5Agg', 'GTK3Agg', etc., as per your environment
import matplotlib.pyplot as plt
load_dotenv()


# Streamlit page configuration
st.set_page_config(
    page_title="🤖 AIConverse Data Lab",
    layout = "wide"
)

# Title of the Streamlit app
st.title('🤖 AIConverse Data Lab')

# Function to process data and interact with OpenAI
def chat_csv(df,prompt):
    llm = OpenAI()  # Creating an instance of OpenAI
    pandas_ai = PandasAI(llm)  # Integrating Pandas with AI
    result = pandas_ai(df, prompt=prompt)  # Generating result based on dataframe and prompt
    return result

# File uploader in Streamlit for CSV files
input_csv = st.file_uploader('Upload a Csv File', type=['csv'], accept_multiple_files=False)
if input_csv is not None:
    # Creating columns for layout
    col1, col2 = st.columns([1,1])
    
    with col1:
        st.info("Csv Uploaded Successfully")
        df = pd.read_csv(input_csv, encoding='latin-1')  # Reading the uploaded CSV file
        st.dataframe(df, use_container_width=True)  # Displaying the dataframe in Streamlit

    with col2:
        st.info("Chat With Data")
        input_text = st.text_area("Enter a Query:")  # Text area for user to enter a query
        if input_text is not None:
            if st.button("Chat with Data"):
                st.info("Your Query: " + input_text)
                result = chat_csv(df, input_text)  # Processing the query with the dataframe
                st.success(result)  # Displaying the result

