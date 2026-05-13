import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_dataset(data_path):
    data_path = BASE_DIR / data_path
    return pd.read_csv(data_path)


def save_dataset(df, save_path, index=False):
    save_path = BASE_DIR / save_path
    df.to_csv(save_path, index=index)