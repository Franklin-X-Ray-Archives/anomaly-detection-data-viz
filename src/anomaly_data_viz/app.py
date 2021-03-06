"""Dash app definition."""

import json
from dataclasses import dataclass

import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output, State
from flask import Flask

from anomaly_data_viz.plot import Plot
from anomaly_data_viz.utils import upload_file


@dataclass
class App:
    """Dash app instance."""

    server: Flask = Flask("Dash app")

    appConfig = {
        "name": "anomaly-data-viz",
        "assets_folder": "static",
        "title": "anomaly-data-viz",
    }

    app = dash.Dash(server=server, external_stylesheets=[dbc.themes.LUX], **appConfig)

    styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

    navbar = dbc.Nav(
        className="nav nav-pills",
        children=[
            # logo/home
            dbc.NavItem(
                html.Img(
                    src=app.get_asset_url("iimas.png"),
                    height="40px",
                )
            ),
            # about
            dbc.NavItem(
                html.Div(
                    [
                        dbc.NavLink("About", href="/", id="about-popover", active=False),
                        dbc.Popover(
                            id="about",
                            is_open=False,
                            target="about-popover",
                            children=[
                                dbc.PopoverHeader("How it works"),
                                dbc.PopoverBody("anomaly detection data viz"),
                            ],
                        ),
                    ]
                )
            ),
            # links
            dbc.DropdownMenu(
                label="Links",
                nav=True,
                children=[
                    dbc.DropdownMenuItem(
                        [html.I(className="fa fa-github"), "  Code"],
                        href="www.google.com",
                        target="_blank",
                    ),
                ],
            ),
        ],
    )

    # Callbacks
    @app.callback(
        output=[
            Output(component_id="about", component_property="is_open"),
            Output(component_id="about-popover", component_property="active"),
        ],
        inputs=[Input(component_id="about-popover", component_property="n_clicks")],
        state=[State("about", "is_open"), State("about-popover", "active")],
    )
    def about_popover(is_clicked: bool, is_open: bool, active: bool) -> tuple[bool, bool]:  # type: ignore[misc]
        """Display about popover on navbar."""
        if is_clicked:
            return not is_open, active
        return is_open, active

    # ----------------Body

    inputs = dbc.Form(
        [
            # upload a file
            html.Br(),
            dbc.Label(" Upload your file", html_for="upload-file"),
            dcc.Upload(
                id="upload-file",
                children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
            ),
            html.Div(id="file-name", style={"marginLeft": "20px"}),
            # run button
            html.Br(),
            html.Br(),
            dbc.Col(dbc.Button("run", id="run", color="primary")),
        ]
    )

    # Output
    body = dbc.Row(
        [
            # input
            dbc.Col(
                md=3,
                children=[
                    inputs,
                    html.Br(),
                    html.Br(),
                    html.Br(),
                ],
            ),
            # output
            dbc.Col(
                md=9,
                children=[
                    dbc.Spinner(
                        [
                            # title
                            html.H6(id="title"),
                            # download
                            dbc.Badge(
                                html.A(
                                    "Download",
                                    id="download-excel",
                                    download="tables.xlsx",
                                    href="",
                                    target="_blank",
                                ),
                                color="success",
                                pill=True,
                            ),
                            # plot
                            dcc.Graph(id="plot"),
                        ],
                        color="primary",
                        type="grow",
                    ),
                ],
            ),
        ]
    )

    # Callbacks
    @app.callback(
        output=[Output(component_id="file-name", component_property="children")],
        inputs=[Input(component_id="upload-file", component_property="filename")],
    )
    def upload_event(filename: str) -> list[str]:  # type: ignore[misc]
        """Display name of uploaded file."""
        div = "" if filename is None else f"Using file: {filename}"
        return [div]

    @app.callback(
        output=[
            Output(component_id="title", component_property="children"),
            Output(component_id="plot", component_property="figure"),
        ],
        inputs=[Input(component_id="run", component_property="n_clicks")],
        state=[State("upload-file", "contents"), State("upload-file", "filename")],
    )
    def results(n_clicks: int, contents: str, filename: str) -> tuple[str, go.Figure]:  # type: ignore[misc]
        """Load input data and compute graph."""
        print("times", n_clicks)
        if contents is not None:
            dataset = upload_file(contents, filename)
        else:
            dataset = upload_file("", "")

        figure = Plot(dataset)
        return "filename", figure.plot()

    @app.callback(Output(component_id="selected-data", component_property="children"), Input("plot", "selectedData"))
    def display_selected_data(selected_data: dict[str, str]) -> str:  # type: ignore[misc]
        """Get and display users's selected data."""
        print("selected_data object:", selected_data)
        return (
            json.dumps(selected_data, indent=2)
            if selected_data is not None
            else json.dumps({"points": "No points selected"})
        )

    # -----------Layout
    app.layout = dbc.Container(
        fluid=True,
        children=[
            html.H1("Anomaly data viz", id="nav-pills"),
            navbar,
            html.Br(),
            html.Br(),
            html.Br(),
            body,
            html.Div(
                className="row",
                children=[
                    html.Div(
                        [
                            dcc.Markdown(
                                """
                **Selection Data**

                Choose the lasso or rectangle tool in the graph's menu bar and then select points in the graph.

                Hold down the shift button while clicking to accumulates/un-accumulates data.
            """
                            ),
                            html.Pre(id="selected-data", style=styles["pre"]),
                        ]
                    )
                ],
            ),
        ],
    )
