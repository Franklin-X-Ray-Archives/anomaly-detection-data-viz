import logging

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc


app = dash.Dash(name='anomaly-data-viz', external_stylesheets=[dbc.themes.LUX])
app.title = 'anomaly-data-viz'


#app.run_server()

var=99
