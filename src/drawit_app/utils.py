""" """
import sys
import pathlib
import pandas as pd


def get_package_file(*folders: str) -> pathlib.PosixPath:
    """Imports package data using importlib functionality.

    Args:
        *folders: comma-separated strings representing path to the packaged data
            file.
    Returns:
        A os-indepenent posix path of the data file.
    """
    # Import the package based on Python's version
    if sys.version_info < (3, 9):
        # importlib.resources either doesn't exist or lacks the files()
        # function, so use the PyPI version:
        import importlib_resources
    else:
        # importlib.resources has files(), so use that:
        import importlib.resources as importlib_resources

    pkg = importlib_resources.files("")
    # Append folders to package-wide posix path
    pkg = pathlib.Path.joinpath(pkg, '/'.join(folders))
    return pkg


def load_outputs(path: str) -> pd.DataFrame:
    """
    Loads tabular data in a csv file and returns pandas.DataFrame
    """
    return pd.read_csv(path, index_col=0)
