import pandas as pd


def validate_data(df):
    """
    Check whether the uploaded CSV contains valid data.
    Returns (True, message) if valid,
    otherwise (False, error_message).
    """

    # Check whether the CSV is empty
    if df.empty:
        return False, "The uploaded CSV file is empty."

    # Check whether column names are missing
    if df.columns.isnull().any():
        return False, "Some column names are missing."

    # Check whether column names are blank
    if any(str(column).strip() == "" for column in df.columns):
        return False, "Column names cannot be blank."

    # Check for completely empty rows
    if df.dropna(how="all").empty:
        return False, "The CSV does not contain usable data."

    # Check whether duplicate column names exist
    if df.columns.duplicated().any():
        return False, "Duplicate column names were found."

    return True, "CSV data is valid and ready for analysis."
