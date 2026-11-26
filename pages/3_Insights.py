import streamlit as st

from modules.data_import import import_csv
from modules.data_validation import validate_data
from modules.data_cleaning import clean_data
from modules.analysis import analyse_data
from modules.insight_engine import generate_insights
from modules.weekly_summary import generate_weekly_summary


st.title("💡 LifeOS Insights")

st.write("Discover understandable patterns in your activity data.")

uploaded_file = st.file_uploader(
    "Upload your activity CSV",
    type=["csv"],
    key="insights_upload"
)

if uploaded_file is not None:

    # Import uploaded data
    df, message = import_csv(uploaded_file)

    if df is None:
        st.error(message)

    else:
        # Validate uploaded data
        is_valid, validation_message = validate_data(df)

        if not is_valid:
            st.error(validation_message)

        else:
            # Clean and analyse data
            cleaned_df = clean_data(df)
            results = analyse_data(cleaned_df)

            # Generate insights
            st.subheader("Your Personal Insights")

            insights = generate_insights(results)

            for insight in insights:
                st.info(insight)

            # Generate summary
            st.subheader("Activity Summary")

            summary = generate_weekly_summary(results)

            st.text(summary)

else:
    st.info("Upload a CSV file to discover your insights.")
