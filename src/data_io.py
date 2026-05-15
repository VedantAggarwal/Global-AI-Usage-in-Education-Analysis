import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_dataset(data_path):
    """
    Load a dataset from the specified path.

    Parameters
    ----------
    data_path : str or pathlib.Path
        Relative path to the dataset file from the project root.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset as a dataframe.
    """

    data_path = BASE_DIR / data_path

    return pd.read_csv(data_path)


def save_dataset(df, save_path, index=False):
    """
    Save a dataframe to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe to save.

    save_path : str or pathlib.Path
        Relative path where the dataset will be saved.

    index : bool, default=False
        Whether to save dataframe index in the output file.

    Returns
    -------
    None
    """

    save_path = BASE_DIR / save_path

    df.to_csv(save_path, index=index)