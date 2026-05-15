import pandas as pd


def check_null_columns(df):
    """
    Identify columns containing null values and calculate their percentage.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    pandas.DataFrame
        Dataframe containing null counts and null percentages
        for columns with missing values.
    """

    temp = df.isnull().sum()
    temp = temp[temp != 0]

    temp = pd.DataFrame(temp, columns=["null_count"])

    temp["null_pct"] = temp["null_count"] / len(df) * 100

    return temp


def check_column_type(df):
    """
    Separate object and numerical columns from a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    tuple
        Tuple containing:
        - list of object columns
        - list of numerical columns
    """

    obj_cols = df.select_dtypes(include="object").columns.tolist()

    num_cols = df.select_dtypes(include="number").columns.tolist()

    return obj_cols, num_cols


def fill_null(df, fill_mapping):
    """
    Fill missing values in a dataframe using specified mappings.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    fill_mapping : dict
        Dictionary specifying column-value mappings
        for filling null values.

    Returns
    -------
    pandas.DataFrame
        Dataframe with missing values filled.
    """

    df = df.copy()

    return df.fillna(fill_mapping)


def apply_mapping(df, column_mapping):
    """
    Apply value mappings to specified dataframe columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    column_mapping : dict
        Dictionary containing column-wise replacement mappings.

    Returns
    -------
    pandas.DataFrame
        Dataframe with transformed column values.
    """

    df = df.copy()

    for col, mapping in column_mapping.items():
        df[col] = df[col].replace(mapping)

    return df