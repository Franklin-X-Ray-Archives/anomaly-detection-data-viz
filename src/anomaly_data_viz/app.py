import logging

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc


from flask import Flask

server = Flask('Dash app')

app = dash.Dash(name='anomaly-data-viz',server=server ,external_stylesheets=[dbc.themes.LUX])
app.title = 'anomaly-data-viz'


#app.run_server()

var=99
