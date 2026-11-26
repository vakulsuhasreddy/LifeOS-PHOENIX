import pandas as pd


def import_csv(uploaded_file):
    """
    Read an uploaded CSV file and return its data.
    """

    try:
        # Read CSV data using Pandas
        df = pd.read_csv(uploaded_file)

        # Return imported data
        return df, "CSV imported successfully!"

    except pd.errors.EmptyDataError:
        return None, "The uploaded CSV file is empty."

    except pd.errors.ParserError:
        return None, "Unable to read the CSV format."

    except Exception as error:
        return None, f"Import failed: {error}"
