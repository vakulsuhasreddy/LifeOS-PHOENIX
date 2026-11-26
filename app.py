import streamlit as st
from pathlib import Path

# Configure LifeOS application
st.set_page_config(
    page_title="LifeOS",
    page_icon="🌱",
    layout="wide"
)

# Main heading
st.title("🌱 LifeOS")

st.subheader("Your Life. Your Data. Your Intelligence.")

st.write(
    "A privacy-focused personal intelligence platform "
    "that helps you understand your daily habits."
)

st.info("Welcome to LifeOS – Track 3: Know Thyself")

st.divider()

# Project introduction
st.header("Understand Yourself Better")

st.write(
    "LifeOS converts your personal activity data into "
    "understandable patterns and useful insights."
)

# Main features
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Personal Dashboard")
    st.write("Explore your activity data and interactive charts.")

    st.subheader("📖 Habit Journal")
    st.write("Record and track your daily habits.")

with col2:
    st.subheader("💡 Smart Insights")
    st.write("Discover patterns using explainable rules.")

    st.subheader("🔐 Data Privacy")
    st.write("Export your data and manage your data files.")

st.divider()

# Sample dataset download
st.header("Try LifeOS")

sample_file = Path("sample_data/sample_activity.csv")

if sample_file.exists():
    with open(sample_file, "rb") as file:
        st.download_button(
            label="Download Sample Activity CSV",
            data=file,
            file_name="sample_activity.csv",
            mime="text/csv"
        )

st.caption(
    "LifeOS is a personal activity insights tool, "
    "not a medical diagnosis system."
)

st.success(
    "Choose a page from the sidebar to explore LifeOS."
)
    
