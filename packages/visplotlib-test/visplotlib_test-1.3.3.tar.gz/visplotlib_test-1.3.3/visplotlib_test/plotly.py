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
        fig (plotly.graph_objs._figure.Figure): plotly object
        width (float): Textwidth of the report to make fontsizes match.
        fraction_of_line_width (float, optional): Fraction of the document width
            which you wish the figure to occupy.  Defaults to 1.
        ratio (float, optional): Fraction of figure width that the figure height
            should be. Defaults to (5 ** 0.5 - 1)/2.
    Returns:
        None: alters plt to ensure good formatting.
    """
    subgraph_num = len([x for x in fig.to_dict()["layout"].keys() if "xaxis" in x])

    if fig.layout.title.text is None:
        warnings.warn("Title is not specified!")
    if fig.layout.xaxis.title.text is None:
        warnings.warn("X-axis label not specified!")
    if fig.layout.yaxis.title.text is None:
        warnings.warn("Y-axis label not specified!")

    if fig.layout.title.text is not None:
        new_title = " ".join(fig.layout.title.text.split("_")).capitalize()
        fig.update_layout(title=new_title, title_font_color="#162b5d")
    if fig.layout.xaxis.title.text is not None:
        new_xlabel = " ".join(fig.layout.xaxis.title.text.split("_")).capitalize()
        fig.update_layout(xaxis_title=new_xlabel)
    if fig.layout.yaxis.title.text is not None:
        new_ylabel = " ".join(fig.layout.yaxis.title.text.split("_")).capitalize()
        fig.update_layout(yaxis_title=new_ylabel)
    if fig.layout.legend:
        fig.update_layout(legend_font_color="#162b5d")

    if subgraph_num > 1:
        for i in range(2, subgraph_num + 1):
            if fig.layout[f"xaxis{i}"].title.text is None:
                warnings.warn(f"X-axis label of subgraph{i} label not specified!")
            if fig.layout[f"yaxis{i}"].title.text is None:
                warnings.warn(f"Y-axis label of subgraph{i} not specified!")

            if fig.layout[f"xaxis{i}"].title.text is not None:
                new_xlabel = " ".join(
                    fig.layout[f"xaxis{i}"].title.text.split("_")
                ).capitalize()
                fig.layout[f"xaxis{i}"].title.text = new_xlabel

            if fig.layout[f"yaxis{i}"].title.text is not None:
                new_ylabel = " ".join(
                    fig.layout[f"yaxis{i}"].title.text.split("_")
                ).capitalize()
                fig.layout[f"yaxis{i}"].title.text = new_xlabel

    fig.update_layout(
        width=width * fraction_of_line_width * 1.34,
        height=width * ratio * 1.34,
        margin=dict(l=10, r=10, t=40, b=10),
        font=dict(family="Arial", size=15),
    )


plotly.format = _format
