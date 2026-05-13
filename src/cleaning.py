import pandas as pd

def check_null_columns(df):
    temp = df.isnull().sum()
    temp = temp[temp != 0]
    temp = pd.DataFrame(temp, columns=["null_count"])
    temp["null_pct"] = temp["null_count"] / len(df) * 100
    return temp


def check_column_type(df):
    obj_cols = df.select_dtypes(include="object").columns.tolist()
    num_cols = df.select_dtypes(include="number").columns.tolist()
    return obj_cols, num_cols


def fill_null(df, fill_mapping):
    df = df.copy()
    return df.fillna(fill_mapping)


def apply_mapping(df, column_mapping):
    df = df.copy()
    for col, mapping in column_mapping.items():
        df[col] = df[col].replace(mapping)
    return df