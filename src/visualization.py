import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def save_figure(fig, fig_path, dpi=300):
    """
    Save a matplotlib figure to the specified path.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure object to save.

    fig_path : str or pathlib.Path
        Relative path where the figure will be saved.

    dpi : int, default=300
        Resolution of the saved figure.

    Returns
    -------
    None
    """

    save_path = BASE_DIR / fig_path
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")


def create_figure_grid(nrows, ncols, figsize=(10, 6)):
    """
    Create a grid of matplotlib subplots.

    Parameters
    ----------
    nrows : int
        Number of subplot rows.

    ncols : int
        Number of subplot columns.

    figsize : tuple, default=(10, 6)
        Figure size in inches.

    Returns
    -------
    tuple
        Tuple containing:
        - matplotlib figure object
        - array of subplot axes
    """

    fig, axes = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        figsize=figsize
    )

    return fig, axes


def plot_grouped_bar(
    ax,
    df,
    x_col,
    y_cols,
    title=None,
    xlabel=None,
    ylabel="Value",
    rotation=45
):
    """
    Create a grouped bar chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object for plotting.

    df : pandas.DataFrame
        Input dataframe.

    x_col : str
        Column used for x-axis categories.

    y_cols : list
        Numerical columns to plot as grouped bars.

    title : str, optional
        Plot title.

    xlabel : str, optional
        Label for x-axis.

    ylabel : str, default="Value"
        Label for y-axis.

    rotation : int, default=45
        Rotation angle for x-axis tick labels.

    Returns
    -------
    None
    """

    plot_df = df.set_index(x_col)[y_cols]
    plot_df.plot(kind="bar", ax=ax)

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=rotation)

    ax.legend(
        title="AI Tool",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        fontsize=8
    )


def plot_line(
    ax,
    df,
    x_col,
    y_cols,
    title=None,
    xlabel=None,
    ylabel="Value"
):
    """
    Create a line plot for multiple numerical columns.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object for plotting.

    df : pandas.DataFrame
        Input dataframe.

    x_col : str
        Column used for x-axis.

    y_cols : list
        Numerical columns to plot as lines.

    title : str, optional
        Plot title.

    xlabel : str, optional
        Label for x-axis.

    ylabel : str, default="Value"
        Label for y-axis.

    Returns
    -------
    None
    """

    for col in y_cols:
        ax.plot(df[x_col], df[col], marker="o", label=col)

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel)
    ax.legend()


def plot_scatter(
    ax,
    df,
    x_col,
    y_col,
    hue=None,
    legend=True,
    title=None,
    xlabel=None,
    ylabel=None
):
    """
    Create a scatter plot using seaborn.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object for plotting.

    df : pandas.DataFrame
        Input dataframe.

    x_col : str
        Column used for x-axis.

    y_col : str
        Column used for y-axis.

    hue : str, optional
        Column used for color grouping.

    legend : bool, default=True
        Whether to display legend.

    title : str, optional
        Plot title.

    xlabel : str, optional
        Label for x-axis.

    ylabel : str, optional
        Label for y-axis.

    Returns
    -------
    None
    """

    sns.scatterplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=hue,
        ax=ax,
        legend=legend
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel if ylabel else y_col)