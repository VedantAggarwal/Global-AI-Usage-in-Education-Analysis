import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def save_figure(fig, fig_path, dpi=300):
    save_path = BASE_DIR / fig_path
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")


def create_figure_grid(nrows, ncols, figsize=(10, 6)):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    return fig, axes


def plot_grouped_bar(ax, df, x_col, y_cols, title=None, xlabel=None, ylabel="Value", rotation=45):
    
    plot_df = df.set_index(x_col)[y_cols]
    plot_df.plot(kind="bar", ax=ax)

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=rotation)
    ax.legend(title="AI Tool", bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)


def plot_line(ax, df, x_col, y_cols, title=None, xlabel=None, ylabel="Value"):

    for col in y_cols:
        ax.plot(df[x_col], df[col], marker="o", label=col)

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel)
    ax.legend()
    

def plot_scatter(ax, df, x_col, y_col, hue=None, legend=True, title=None, xlabel=None, ylabel=None):
    
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, ax=ax, legend=legend)

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x_col)
    ax.set_ylabel(ylabel if ylabel else y_col)