
import os
import pandas as pd


def export_data(df, filename="lifeos_export.csv"):
    """
    Allow users to export their personal data.
    """

    df.to_csv(filename, index=False)

    return filename


def delete_export(filename):
    """
    Delete an exported data file.
    """

    if os.path.exists(filename):
        os.remove(filename)
        return True

    return False
