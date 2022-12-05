""" """
import collections
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from . import ids
from . import constants
from .utils import ParallelPlotSelector


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """ """

    @app.callback(
        dash.dependencies.Output(ids.DATA_TABLE, 'data'),
        [dash.dependencies.Input(ids.PARALLEL_PLOT, 'restyleData')],
        [dash.dependencies.State(ids.PARALLEL_PLOT, 'figure')])
    def read_parallel_data(restyle_data, par_coordinate_data) -> dict:
        """Update data in a table if data selector is applied to
        the parallel plot"""
        data_limits = []
        pps = ParallelPlotSelector(raw_data=results)
        if restyle_data:
            # Get the label, col_index and constraints into a dict
            figure_vals = par_coordinate_data['data'][0]['dimensions']
            for index, data in enumerate(figure_vals):
                col_index = index
                col_label = data['label']
                constraint_range = data.get('constraintrange', None)
                if constraint_range:
                    if not isinstance(constraint_range[0], collections.Sequence):
                        constraint_range = [constraint_range]
                    data_limits.append(
                        {'col_index': col_index,
                         'col_label': col_label,
                         'constraints': constraint_range})
            for item in data_limits:
                pps.update_selection(
                    col_label=item['col_label'], limits=item['constraints'])
            pps.filter_data()
            pps.filtered_data.reset_index(inplace=True)
        return pps.filtered_data.reset_index().round(2).to_dict('records')

    # Callback for colouring parallel plot based on the selected objective function
    @app.callback(
        dash.dependencies.Output(ids.PARALLEL_PLOT, 'figure'),
        [dash.dependencies.Input(ids.RADIO_ITEMS, 'value')])
    def update_parallel_plot(selector):
        figure = px.parallel_coordinates(
            results[constants.OBJECTIVES],
            labels=constants.parallel_plot_vars,
            color=selector,
            color_continuous_scale=px.colors.cyclical.IceFire,
        )
        return figure

    return html.Div([
        dcc.Graph(
            id=ids.PARALLEL_PLOT
        ),
        ], style={'padding': '0px'}, className="seven columns"
    )
