import os
import streamlit as st
import pandas as pd

from modules.privacy import export_data, delete_export


st.title("🔐 LifeOS Data Privacy")

st.write(
    "Your personal data belongs to you. "
    "LifeOS is designed with privacy in mind."
)

st.subheader("Privacy Principles")

st.markdown("""
- Your uploaded CSV is processed locally by this app.
- Insights are generated from your uploaded data.
- No medical diagnosis or treatment recommendations are provided.
- You can export your data.
""")

st.divider()

st.subheader("Export Your Data")

uploaded_file = st.file_uploader(
    "Upload a CSV file to export",
    type=["csv"],
    key="privacy_upload"
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    filename = "lifeos_export.csv"

    export_data(df, filename)

    with open(filename, "rb") as file:
        st.download_button(
            "Download Your Data",
            data=file,
            file_name=filename,
            mime="text/csv"
        )

    st.success("Your export file is ready.")

    if st.button("Delete Exported File"):
        deleted = delete_export(filename)

        if deleted:
            st.success("Exported file deleted.")
        else:
            st.warning("No exported file was found.")

st.divider()

st.subheader("Data Control")

st.write(
    "LifeOS currently exports and deletes the CSV export file. "
    "Database-record deletion will be handled separately."
)
