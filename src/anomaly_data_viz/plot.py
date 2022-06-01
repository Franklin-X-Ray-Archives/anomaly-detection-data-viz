
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


class Plot():

    def __init__(self, dataset ):
       self.dataset = dataset


    #@staticmethod
    #def prepare_data(dtf):
    #    pass


    def print_title(self, filename=None):
        pass


    def plot(self):
        df = self.dataset.copy()
        fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
        #fig.show()
        return fig
 
