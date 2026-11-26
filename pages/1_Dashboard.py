import streamlit as st
import pandas as pd

from modules.data_import import import_csv
from modules.data_validation import validate_data
from modules.data_cleaning import clean_data
from modules.analysis import analyse_data
from modules.charts import create_chart


st.title("📊 LifeOS Dashboard")

st.write("Understand your daily activity through your data.")

# Upload activity CSV
uploaded_file = st.file_uploader(
    "Upload your activity CSV",
    type=["csv"],
    key="dashboard_upload"
)

if uploaded_file is not None:

    # Import CSV data
    df, message = import_csv(uploaded_file)

    if df is None:
        st.error(message)

    else:
        # Validate uploaded data
        is_valid, validation_message = validate_data(df)

        if not is_valid:
            st.error(validation_message)

        else:
            st.success(validation_message)

            # Clean the uploaded data
            cleaned_df = clean_data(df)

            # Analyse cleaned data
            results = analyse_data(cleaned_df)

            st.subheader("Your Activity Data")
            st.dataframe(cleaned_df, use_container_width=True)

            st.subheader("Activity Statistics")
            st.json(results)

            # Display charts for numeric columns
            numeric_columns = cleaned_df.select_dtypes(
                include="number"
            ).columns.tolist()

            if numeric_columns:
                selected_column = st.selectbox(
                    "Choose a metric to explore",
                    numeric_columns
                )

                chart = create_chart(
                    cleaned_df,
                    selected_column
                )

                if chart is not None:
                    st.plotly_chart(
                        chart,
                        use_container_width=True
                    )
            else:
                st.info("No numeric columns available for charts.")

else:
    st.info("Upload a CSV file to view your dashboard.")
