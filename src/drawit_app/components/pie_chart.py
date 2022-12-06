""" """
import dash
from dash import html, dcc
import plotly.express as px
from dash.exceptions import PreventUpdate
import pandas as pd
from . import ids
from . import constants

hovertemplate_single_piechart = (
    '<i>Landuse type</i>: <b>%{customdata}</b>' +
    "<extra></extra>")


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """ """
    # Calback for creating a pie chart based on the row selected in the table
    @app.callback(
        dash.dependencies.Output(ids.PIE_CHART, "figure"),
        [dash.dependencies.Input(ids.PARETO_3D, "clickData")])
    def update_pie_chart(selected_point):
        if selected_point is None:
            selected_row_index = 0
        else:
            selected_row_index = selected_point['points'][0]['pointNumber']

        pie_df = results[constants.var_for_pie_chart].iloc[
            [selected_row_index]]*100
        pie_df.rename(columns=constants.labels_dict_pie_chart, inplace=True)
        pie_df .reset_index(inplace=True)
        pie_df = pd.melt(
            pie_df, id_vars=['index'], var_name='land_cover',
            value_name='fraction')

        fig1 = px.pie(
            pie_df,
            values='fraction', #pie_df.values[0],
            names='land_cover',
            color='land_cover',
            color_discrete_sequence=px.colors.sequential.RdBu,
            color_discrete_map=constants.piechart_color_map_label)
        fig1.update_layout(margin=dict(l=20, r=20, t=0, b=0))
        fig1.update_traces(hovertemplate=hovertemplate_single_piechart)
        return fig1

    return html.Div([
        dcc.Graph(id=ids.PIE_CHART, style={'width': '60vh', 'height': '60vh'}),
    ], style={'padding': '0px', 'text-align': 'center',
              'margin-top': '-10px', 'padding-top': '-30px'},
        className="four columns offset-by-one")
