import pandas as pd


def clean_data(df):
    """
    Clean uploaded activity data before analysis.
    """

    # Create a copy so original data is not modified
    df = df.copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Fill missing numeric values with column averages
    for column in df.select_dtypes(include="number").columns:
        df[column] = df[column].fillna(df[column].mean())

    # Fill missing text values with 'Not provided'
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].fillna("Not provided")

    return df
