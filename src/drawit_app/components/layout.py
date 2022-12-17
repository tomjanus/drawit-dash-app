""" """
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from . import (
    radio_items, parallel_plot, data_table, heatmap, pie_chart, introduction,
    plot_3d, dropdowns, download_button, body)


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


def create_header(app: Dash) -> dbc.Row:
    """ """
    header = dbc.Row([
        dbc.Col(html.H1('DRAW-IT'), width=6),
        dbc.Col(
            html.Img(
                src=app.get_asset_url('img/logo_big.gif'),
                style={"width": "100%"}),
            align="center", width=2),
        dbc.Col(
            html.Img(
                src=app.get_asset_url(
                    'img/university-of-southampton-vector-logo-small.png'),
                style={"width": "100%"}),
            align="center", width=2),
        dbc.Col(
            html.Img(
                src=app.get_asset_url('img/juelich_sc.jpg'),
                style={"width": "100%"}),
            align="center", width=2)
        ], style={
            "margin-bottom": "15px", "margin-top": "0px",
            'padding-top': '30px'})
    return header


def create_footer(app: Dash) -> dbc.Row:
    """ """
    footer = dbc.Row(
        [
            dbc.Col(html.P([
                html.I("Created by:  "),
                "Tomasz Janus, University of Manchester"])),
            dbc.Col(
                html.Header([
                    html.A(
                        href="https://github.com/tomjanus",
                        title="Check my GitHub",
                        children=[
                            html.Img(
                                alt="Link to my Github Page",
                                src=app.get_asset_url(
                                    'img/GitHub-Mark-32px.png'))
                        ], style={'margin-right': 10}),
                    html.A(
                        href="mailto:tomasz.k.janus@gmail.com",
                        title="Send me a message",
                        children=[
                            html.Img(
                                alt="Link to my Mailbox address",
                                src=app.get_asset_url(
                                    'img/gmail-32px.png'))
                        ], style={'margin-right': 10}),
                    html.A(
                        href="https://www.linkedin.com/in/tomasz-janus-6443b7198/",
                        title="Visit my LinkedIn profile",
                        children=[
                            html.Img(
                                alt="Link to my LinkedIn Page",
                                src=app.get_asset_url(
                                    'img/linkedin-32px.png'))])
                    ])
            )], style={'margin-top': '10pt', 'margin-bottom': '10pt'})
    return footer


def add_introduction(app: Dash) -> dbc.Row:
    """ """
    return dbc.Row(introduction.render(app))


def create_layout(app: Dash, data: pd.DataFrame) -> None:
    app.layout = dbc.Container([
        create_header(app),
        introduction.render(app),
        body.render(app, data),
        create_footer(app)
    ], fluid="xl")

"""
        dbc.Popover(
            popover_children,
            target="focus-target",
            body=True,
            trigger="focus", """
