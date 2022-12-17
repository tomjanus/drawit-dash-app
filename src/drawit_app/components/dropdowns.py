"""Render dropdown components controlling the 3d plot of the pareto surface"""
from typing import Tuple
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from . import ids
from . import constants

options = [
    {'label': label, 'value': value} for value, label in zip(
        constants.parallel_plot_vars.keys(),
        constants.parallel_plot_vars.values())
    ]


def render(app: dash.Dash) -> dbc.Row:
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

    # Only display the row in conjuction with the 3D plot
    @app.callback(
        dash.dependencies.Output(ids.DROPDOWNS_ROW, "style"),
        dash.dependencies.Input(ids.TABLE_3D_PLOT_TAB, "active_tab"),
    )
    def hide_dropdowns(active_tab: str) -> dict:
        """ """
        if active_tab == "table-tab":
            # Hide the dropdowns
             style = {'display': 'none'}
        elif active_tab == "plot-tab":
            # show the dropdowns
             style = {'padding': '0px', 'margin-bottom': '10px'}
        else:
            # Hide the dropdowns
            style = {'display': 'none'}
        return style

    def create_dropdowns() -> dbc.Row:
        """ """
        return dbc.Row([
            dbc.Col([
                "x-axis",
                dcc.Dropdown(
                    options=options, value=options[0]['value'],
                    id=ids.X_AXIS_DROPDOWN_3D, clearable=False)],
                    style={'margin-left': '20px', 'margin-right': '10px'}),
            dbc.Col([
                "y-axis",
                dcc.Dropdown(
                    options=options, value=options[3]['value'],
                    id=ids.Y_AXIS_DROPDOWN_3D, clearable=False)],
                    style={'margin-left': '10px', 'margin-right': '10px'}),
            dbc.Col([
                "z-axis",
                dcc.Dropdown(
                    options=options, value=options[1]['value'],
                    id=ids.Z_AXIS_DROPDOWN_3D, clearable=False)],
                    style={'margin-left': '10px', 'margin-right': '10px'}),
            dbc.Col([
                "color",
                dcc.Dropdown(
                    options=options, value=options[0]['value'],
                    id=ids.COLOR_DROPDOWN_3D, clearable=False)],
                    style={'margin-left': '10px', 'margin-right': '10px'}),
            dbc.Col([
                "Reset",
                html.Button(
                    children=["Reset to Defaults"],
                    id=ids.RESET_TO_DEFAULTS,
                    n_clicks=0)],
                    style={'margin-left': '10px', 'margin-right': '10px'})
            ], id=ids.DROPDOWNS_ROW)

    return create_dropdowns()
