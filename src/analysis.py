def count_distribution(df, parameter_col, value_col, pct=False):
    """
    Create a distribution table of counts for grouped categorical values.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    parameter_col : str
        Column used for grouping rows.

    value_col : str
        Column whose value distribution is calculated.

    pct : bool, default=False
        If True, normalize counts row-wise into percentages.

    Returns
    -------
    pandas.DataFrame
        Distribution table with grouped counts or percentages.
    """

    counts = df.groupby([parameter_col, value_col]).size().unstack(fill_value=0)

    if pct:
        counts = counts.div(counts.sum(axis=1), axis=0)

    return counts


def aggregate_metric(df, group_col, value_col, agg="mean"):
    """
    Aggregate a numerical column using a specified aggregation function.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    group_col : str
        Column used for grouping data.

    value_col : str
        Numerical column to aggregate.

    agg : str, default="mean"
        Aggregation function to apply.

    Returns
    -------
    pandas.Series
        Aggregated values grouped by the specified column.
    """

    return df.groupby(group_col)[value_col].agg(agg)


def summary_metrics(df, group_col, value_col):
    """
    Generate summary statistics for grouped numerical data.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    group_col : str
        Column used for grouping data.

    value_col : str
        Numerical column for which summary statistics are calculated.

    Returns
    -------
    pandas.DataFrame
        Summary statistics including count, mean, median,
        minimum and maximum values.
    """

    return df.groupby(group_col)[value_col].agg(
        ["count", "mean", "median", "min", "max"]
    )