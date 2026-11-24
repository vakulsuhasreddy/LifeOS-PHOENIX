import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="LifeOS",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 LifeOS")
st.subheader("Your Life. Your Data. Your Intelligence.")

st.write(
    "A privacy-focused personal intelligence "
    "platform that helps you understand your daily habits."
)

st.info("Welcome to LifeOS – Track 3: Know Thyself")

uploaded_file = st.file_uploader(
    "Upload your personal activity CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("CSV uploaded successfully!")

    st.subheader("Your Data")
    st.dataframe(df)

    st.subheader("Data Summary")
    st.write(df.describe(include="all"))

else:
    st.write("Upload a CSV file to begin analysing your data.")
