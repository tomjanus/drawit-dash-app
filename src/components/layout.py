""" """
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from . import (
    radio_items, parallel_plot, data_table, heatmap, pie_chart, introduction,
    plot_3d, dropdowns, download_button)


DIAGRAM_DESCRIPTION = '''
The land cover design problem considers five competing objectives: $f_1(x)$ =
hydropower (HP) production, $f_2(x)$ = flooded area, $f_3(x)$ = crop production,
$f_4(x)$ = solar power (SP) production, $f_5(x)$ = land cover diversity. The
decision variable $x$ is a $10$ x $1$ vector of land covers on the hillslope.
The boundary conditions on the hillslope are atmospheric forcings and base flow
$q_b$. The mass balance in the hydroelectric reservoir in the water resource
model considers water sources: hillslope runoff flow $q_{in}$ and rainfall $q_r$
and water sink due to evaporation from the reservoir surface $q_e$. The flow
entering the turbine is denoted $q_{HP}$ while the spill flow bypassing the
turbine is denoted $q_s$. Water release to HP turbine is governed by a reservoir
water release curve that adjusts $q_{HP}$ as a function of reservoir volume.
'''


def create_layout(app: Dash, data: pd.DataFrame) -> None:
    """Create main application layout"""
    app.layout = html.Div([
        html.Div([
            html.H1(children='DRAW-IT',
                    className='six columns'),
            html.Div([
                html.Img(
                    src=app.get_asset_url('img/logo_big.gif'),
                    style={"display": "block", "padding": "10px"},
                    className='two columns'),
                html.Img(
                    src=app.get_asset_url(
                        'img/university-of-southampton-vector-logo-small.png'),
                    style={"display": "block",
                           "padding": "10px",
                           "margin-top": "5px"},
                    className='two columns'),
                html.Img(
                    src=app.get_asset_url('img/juelich.jpg'),
                    style={"display": "block", "padding": "10px",
                           "margin-top": "5px"},
                    className='two columns'),
            ]),

            html.Div([
                introduction.render(app),
                html.H6(
                    children='The block diagram representing the connection \
                        between Parflow/CLM and Pywr models is given below',
                    className='twelve columns',
                    style={"text-align": "center"}),

                html.Img(
                    src=app.get_asset_url('img/combined_model_diagram_simplified.svg'),
                    style={"border": "1px solid #ddd",
                           "display": "block",
                           "border-radius": "4px",
                           "padding": "15px",
                           "margin-left": "auto",
                           "margin-right": "auto",
                           "width": "55%"}),
            ], className="row"),

            html.Div([
                dcc.Markdown(children=DIAGRAM_DESCRIPTION, mathjax=True)
            ], className="row"),

            html.Div([
                html.H3(children='Multiobjective optimisation results',
                        className='ten columns',
                        style={"text-align": "center"}),
                download_button.render(app, data),
            ], className="row"),

            radio_items.render(app),

            html.Div([
                parallel_plot.render(app, results=data),
                data_table.render(app, results=data),
            ], style={'padding': '0px'}, className="row"),

            html.Div([
                html.Div([
                    plot_3d.render(app, data)
                ], style={'padding': '0px'}, className="sixcolumns"),
                html.Div([
                    html.H5(
                        children="Spatial distribution of land covers on the hillslope",
                        style={'textAlign': 'center'}),
                    heatmap.render(app, results=data),
                    html.H5(
                        children="Composition of land covers on the hillslope",
                        style={'textAlign': 'center'}),
                    pie_chart.render(app, results=data)
                ])
            ], style={'padding': '0px'}, className="row"),

            html.Div([
                dropdowns.render(app),
            ], style={'padding': '0px'}, className="row"),

            html.Div(
                dbc.Row(
                    [
                        dbc.Col(html.Div("Authored by: Tomasz Janus"),
                                style={'margin-top': 10}),
                        dbc.Col(html.Div("Please, visit my GitHub page: "),
                                width=3,
                                style={'display': 'inline-block',
                                       'text-align': 'justify',
                                       'margin-right': 10}),
                        dbc.Col(html.A(
                            href="https://github.com/tomjanus",
                            children=[
                                html.Img(
                                    alt="Link to my Github Page",
                                    src=app.get_asset_url(
                                        'img/GitHub-Mark-32px.png')
                                )
                            ]), style={
                                'display': 'inline-block',
                                'text-align': 'justify'}),
                    ]
                ),
            ),
        ], style={'margin': '40px'}),
    ])
