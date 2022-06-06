"""Prepare data and compute graph_objects"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"


class Plot:
    """Class for graph_objects generation"""

    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    # @staticmethod
    # def prepare_data(dtf):
    #    pass

    def print_title(self, filename: str) -> str:
        """Generate formated graph title"""
        return filename

    def plot(self) -> go.Figure:
        """Generate graph"""
        data = self.dataset.copy()
        if data.shape[0] > 0:
            fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")
        else:
            fig = px.scatter(data)
        return fig
