"""Load the results from the Excel file into pandas dataframe"""
import pandas as pd


def load_outputs(path: str) -> pd.DataFrame:
    """ """
    return pd.read_csv(path, index_col=0)
