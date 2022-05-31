

import logging

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc


from flask import Flask

server = Flask("Dash app")

app = dash.Dash(
    name="anomaly-data-viz", server=server, external_stylesheets=[dbc.themes.LUX]
)
app.title = "anomaly-data-viz"


# app.run_server()



navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
#    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("How it works"), dbc.PopoverBody("anomaly detection data viz" )
        ])
    ])),
    ## links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href= "github.com" , target="_blank"),
    ])
])


# Output
body = dbc.Row([
        ## input
        dbc.Col(md=3, children=[
            #inputs, 
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


app.layout = dbc.Container(fluid=True, children=[
    html.H1("Anomaly data viz", id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    body
])
