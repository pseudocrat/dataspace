"""
Testing Data Functions
"""

import os
import pandas as pd


# Read data from CSV file
def read_data():
    """_summary_: Read data from CSV file

    Returns:
        _type_: _description_
    """
    dataframe = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "data.csv"))
    return dataframe


# Write data to CSV file
def write_data(dataframe):
    """_summary_: Write data to CSV file

    Args:
        dataframe (_type_): _description_
    """
    daf.to_csv(os.path.join(os.path.dirname(__file__), "data", "data.csv"), index=False)


# Add new row to CSV file
def add_row(row):
    """_summary_: Add new row to CSV file

    Args:
        row (_type_): _description_
    """
    dataframe = read_data()
    dataframe = dataframe.append(row, ignore_index=True)
    write_data(dataframe)


# Delete row from CSV file
def delete_row(row):
    """_summary_: Delete row from CSV file

    Args:
        row (_type_): _description_
    """
    dataframe = read_data()
    dataframe = dataframe.drop(row)
    write_data(dataframe)


# Update row in CSV file
def update_row(row, new_row):
    """_summary_: Update row in CSV file

    Args:
        row (_type_): _description_
        new_row (_type_): _description_
    """
    dataframe = read_data()
    dataframe.iloc[row] = new_row
    write_data(dataframe)


# Get row from CSV file
def get_row(row):
    """_summary_: Get row from CSV file

    Args:
        row (_type_): _description_

    Returns:
        _type_: _description_
    """
    dataframe = read_data()
    return dataframe.iloc[row]


# Get all rows from CSV file
def get_all_rows():
    """_summary_: Get all rows from CSV file

    Returns:
        _type_: _description_
    """
    dataframe = read_data()
    return dataframe
