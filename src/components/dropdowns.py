"""Render dropdown components controlling the 3d plot of the pareto surface"""
from typing import Tuple
import dash
from dash import html, dcc
from . import ids
from . import constants

options = [
    {'label': label, 'value': value} for value, label in zip(
        constants.parallel_plot_vars.keys(),
        constants.parallel_plot_vars.values())
    ]


def render(app: dash.Dash) -> html.Div:
    """Render dropdowns controlling the data put onto different axes on the
    3d plot of the Pareto front."""

    @app.callback(
        [
            dash.dependencies.Output(ids.X_AXIS_DROPDOWN_3D, "value"),
            dash.dependencies.Output(ids.Y_AXIS_DROPDOWN_3D, "value"),
            dash.dependencies.Output(ids.Z_AXIS_DROPDOWN_3D, "value"),
            dash.dependencies.Output(ids.COLOR_DROPDOWN_3D, "value")
        ],
        dash.dependencies.Input(ids.RESET_TO_DEFAULTS, "n_clicks"),
    )
    def reset_to_defaults(_: int) -> Tuple[str, str, str, str]:
        x_data = options[0]['value']
        y_data = options[3]['value']
        z_data = options[1]['value']
        color_data = options[0]['value']
        return x_data, y_data, z_data, color_data

    return html.Div([
        html.Div([
            "x-axis",
            dcc.Dropdown(
                options=options, value=options[0]['value'],
                id=ids.X_AXIS_DROPDOWN_3D, clearable=False)],
                style={'padding': '0px'}, className="four columns"),
        html.Div([
            "y-axis",
            dcc.Dropdown(
                options=options, value=options[3]['value'],
                id=ids.Y_AXIS_DROPDOWN_3D, clearable=False)],
                style={'padding': '0px'}, className="four columns"),
        html.Div([
            "z-axis",
            dcc.Dropdown(
                options=options, value=options[1]['value'],
                id=ids.Z_AXIS_DROPDOWN_3D, clearable=False)],
                style={'padding': '0px'}, className="four columns"),
        html.Div([
            "color",
            dcc.Dropdown(
                options=options, value=options[0]['value'],
                id=ids.COLOR_DROPDOWN_3D, clearable=False)],
                style={'padding': '0px'}, className="four columns"),
        html.Div([
            "defaults",
            html.Button(
                children=["Reset"],
                id=ids.RESET_TO_DEFAULTS,
                n_clicks=0)],
                style={'padding': '0px'}, className="three columns")
    ], style={'padding': '0px'}, className="six columns")
