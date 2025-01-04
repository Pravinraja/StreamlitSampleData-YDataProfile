import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Set the page title and layout
st.set_page_config(page_title='Profiling Report', layout='wide')

# Add a title to the app
st.title('Data Profiling Report')

# File upload widget
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Generate the profiling report
    profile = ProfileReport(df, title="Profiling Report")

    # Display the report in the Streamlit app
    st_profile_report(profile)
else:
    st.info('Please upload a CSV file to generate the profiling report.')