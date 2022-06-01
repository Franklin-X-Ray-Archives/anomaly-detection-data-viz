

import logging

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc
from flask import Flask


from typing import Sequence, TypeVar
from config import *

from plot import *
from utils import upload_file


server = Flask("Dash app")

app = dash.Dash(
    name="anomaly-data-viz", server=server, external_stylesheets=[dbc.themes.LUX]
)
app.title = "anomaly-data-viz"




navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    dbc.NavItem(html.Img(src= "http://www.torreingenieria.unam.mx/images/logo-iimas-azul.png", height="40px")),
    ## about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("How it works"), dbc.PopoverBody("anomaly detection data viz" )
        ])
    ])),
    ## links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href=AppConfig.repository  , target="_blank"),
    ])
])


# Callbacks
@app.callback(output=[Output(component_id="about", component_property="is_open"), 
                      Output(component_id="about-popover", component_property="active")], 
              inputs=[Input(component_id="about-popover", component_property="n_clicks")], 
              state=[State("about","is_open"), State("about-popover","active")])

def about_popover(n, is_open, active):
    if n:
        return not is_open, active
    return is_open, active



########################## Body ##########################
# Input
#upload= html.Div(
#    [
#        dbc.Label(" Upload your file", html_for="upload-file"), 
#        dcc.Upload(id='upload-file', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
#               style={'width':'100%', 'height':'60px', 'lineHeight':'60px', 'borderWidth':'1px', 'borderStyle':'dashed',
#                      'borderRadius':'5px', 'textAlign':'center', 'margin':'10px'} ),
#        html.Div(id='file-name', style={"marginLeft":"20px"})
#    ],
#    className="mb-3",
#)

inputs = dbc.Form([
#    upload
    ## upload a file
    html.Br(),
    dbc.Label(" Upload your file", html_for="upload-file"), 
    dcc.Upload(id='upload-file', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
               style={'width':'100%', 'height':'60px', 'lineHeight':'60px', 'borderWidth':'1px', 'borderStyle':'dashed',
                      'borderRadius':'5px', 'textAlign':'center', 'margin':'10px'} ),
    html.Div(id='file-name', style={"marginLeft":"20px"}),

    ## run button
    html.Br(),html.Br(),
    dbc.Col(dbc.Button("run", id="run", color="primary"))
])





# Output
body = dbc.Row([
        ## input
        dbc.Col(md=3, children=[
            inputs, 
            html.Br(),html.Br(),html.Br(),
        ]),
        ## output
        dbc.Col(md=9, children=[
            dbc.Spinner([
                ### title
                html.H6(id="title"),
                ### download
                dbc.Badge(html.A('Download', id='download-excel', download="tables.xlsx", href="", target="_blank"), color="success", pill=True),
                ### plot
                dcc.Graph(id="plot")
            ], color="primary", type="grow"), 
        ])
])


# Callbacks
@app.callback(output=[
                      Output(component_id="file-name", component_property="children")
                      ],  
              inputs=[Input(component_id="upload-file", component_property="filename")]
              )
def upload_event(filename):
    div = "" if filename is None else "Using file: {}".format(filename)
    return  [div]


@app.callback(output=[Output(component_id="title", component_property="children"),
                      Output(component_id="plot", component_property="figure"  )],
              inputs=[Input(component_id="run", component_property="n_clicks")],
              state=[State("upload-file","contents"), State("upload-file","filename")])
def results(n_clicks, contents, filename):
    if contents is not None:
        dataset = upload_file(contents, filename) 
        print(dataset, type(dataset.head() ) )
    else:
        import plotly.express as px
        dataset = px.data.iris()
        
    figure = Plot(dataset)
    return "filename",  figure.plot()




#-----------Layout
app.layout = dbc.Container(fluid=True, children=[
    html.H1("Anomaly data viz", id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    body
])
