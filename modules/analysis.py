import pandas as pd


def analyse_data(df):
    """
    Analyse cleaned personal activity data.
    """

    # Store analysis results
    results = {}

    # Select numeric columns
    numeric_columns = df.select_dtypes(include="number")

    # Calculate statistics for numeric columns
    for column in numeric_columns.columns:
        results[column] = {
            "average": numeric_columns[column].mean(),
            "minimum": numeric_columns[column].min(),
            "maximum": numeric_columns[column].max(),
            "total": numeric_columns[column].sum()
        }

    return results
