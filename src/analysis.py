def count_distribution(df, parameter_col, value_col, pct=False):
    counts = df.groupby([parameter_col, value_col]).size().unstack(fill_value=0)
    if pct:
        counts = counts.div(counts.sum(axis=1), axis=0)
    return counts


def aggregate_metric(df, group_col, value_col, agg="mean"):
    return df.groupby(group_col)[value_col].agg(agg)


def summary_metrics(df, group_col, value_col):
    return df.groupby(group_col)[value_col].agg(
        ["count", "mean", "median", "min", "max"]
    )
