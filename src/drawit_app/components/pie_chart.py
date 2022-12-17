""" """
import dash
from dash import html, dcc, ctx
import plotly.express as px
import pandas as pd
from . import ids
from . import constants

hovertemplate_single_piechart = (
    '<i>Landuse type</i>: <b>%{customdata}</b>' +
    "<extra></extra>")


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """ """

    def create_pie_chart(row_index: int) -> px.pie:
        """ """
        pie_df = results[constants.var_for_pie_chart].iloc[
            [row_index]]*100
        pie_df.rename(columns=constants.labels_dict_pie_chart, inplace=True)
        pie_df .reset_index(inplace=True)
        pie_df = pd.melt(
            pie_df, id_vars=['index'], var_name='land_cover',
            value_name='fraction')
        fig1 = px.pie(
            pie_df,
            values='fraction',
            names='land_cover',
            color='land_cover',
            color_discrete_sequence=px.colors.sequential.RdBu,
            color_discrete_map=constants.piechart_color_map_label)
        fig1.update_layout(margin=dict(l=20, r=20, t=0, b=0))
        fig1.update_traces(hovertemplate=hovertemplate_single_piechart)
        return fig1

    # Calback for creating a pie chart based on the row selected in the table
    @app.callback(
        dash.dependencies.Output(ids.PIE_CHART, "figure"),
        [dash.dependencies.Input(ids.PARETO_3D, "clickData"),
         dash.dependencies.Input(ids.DATA_TABLE, 'data'),
         dash.dependencies.Input(ids.DATA_TABLE, 'selected_rows')])
    def update_pie_chart(selected_point, data, selected_rows) -> px.pie:
        """ """
        trigger_id = ctx.triggered_id
        # Perform different actions depending on whether the Callback
        # is triggered by the table or by the 3D plot
        if trigger_id == ids.PARETO_3D:
            if selected_point is None:
                selected_row_index = 0
            else:
                selected_row_index = selected_point['points'][0]['pointNumber']
        elif trigger_id == ids.DATA_TABLE:
            index_column = data[selected_rows[0]]['index']
            selected_row_index = index_column
        else:
            selected_row_index = 0
        return create_pie_chart(selected_row_index)

    return html.Div([
        dcc.Graph(id=ids.PIE_CHART, style={'width': '60vh', 'height': '60vh'}),
    ], style={'padding': '0px', 'text-align': 'center',
              'margin-top': '-10px', 'padding-top': '-40px'})
