import os
import warnings

import plotly
import plotly.express as px
import plotly.graph_objects as go

from .dims import GOLDEN_SLIDE, set_dim

filepath = os.path.dirname(os.path.abspath(__file__))


def _format(
    fig: plotly.graph_objs._figure.Figure,
    width: float = GOLDEN_SLIDE["width"],
    fraction_of_line_width: float = 1,
    ratio: float = (5**0.5 - 1) / 2,
) -> None:
    """
    Fetches information from current pyplot to verify and impose format.

    Args:
        plt (matplotlib.pyplot): Pyplot object
        width (float): Textwidth of the report to make fontsizes match.
        fraction_of_line_width (float, optional): Fraction of the document width
            which you wish the figure to occupy.  Defaults to 1.
        ratio (float, optional): Fraction of figure width that the figure height
            should be. Defaults to (5 ** 0.5 - 1)/2.
    Returns:
        None: alters plt to ensure good formatting.
    """

    if fig.layout.title.text is None:
        warnings.warn("Title is not specified!")
    if fig.layout.xaxis.title.text is None:
        warnings.warn("X-axis label not specified!")
    if fig.layout.yaxis.title.text is None:
        warnings.warn("Y-axis label not specified!")

    if fig.layout.title.text is not None:
        new_title = " ".join(fig.layout.title.text.split("_")).capitalize()
        fig.update_layout(title=new_title)
    if fig.layout.xaxis.title.text is not None:
        new_xlabel = " ".join(fig.layout.xaxis.title.text.split("_")).capitalize()
        fig.update_layout(xaxis_title=new_xlabel)
    if fig.layout.yaxis.title.text is not None:
        new_ylabel = " ".join(fig.layout.yaxis.title.text.split("_")).capitalize()
        fig.update_layout(yaxis_title=new_ylabel)

    fig.update_layout(
        width=width * fraction_of_line_width * 1.38,
        height=width * ratio * 1.38,
        margin=dict(l=10, r=10, t=40, b=10),
        font=dict(family="Arial", size=15),
    )


plotly.format = _format
