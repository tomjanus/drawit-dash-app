""" """
import dash
from dash import dcc, ctx
from plotly import graph_objs as go
import pandas as pd
from . import ids
from . import constants


hovertemplate_single_heatmap = (
    '<i>Landuse type</i>: <b>%{text}</b>' +
    "<extra></extra>")


def render(app: dash.Dash, results: pd.DataFrame) -> dcc.Graph:
    """ """

    def create_heatmap(row_index) -> go.Figure:
        heatmap_df = results[constants.var_for_heatmap].iloc[[row_index]]
        heatmap_entries = heatmap_df.to_numpy().squeeze()
        hover_list = [constants.landuse_dict[
            heatmap_entries[i]] for i in range(len(heatmap_entries))]
        layout = go.Layout(xaxis_range=[0, 9])
        fig2 = go.Figure(
            data=go.Heatmap(
                z=heatmap_df,
                hoverongaps=False,
                y=[''],
                x=constants.var_for_heatmap,
                hoverinfo='text',
                text=[hover_list],
                colorscale='Viridis',
                hovertemplate=hovertemplate_single_heatmap,
                colorbar_thickness=20), layout=layout)
        fig2.update_xaxes(
            gridcolor='black',
            ticks="outside",
            tickson="boundaries",
            ticklen=20)
        fig2.update_xaxes(range=[-0.5, 9.5])
        fig2.update_traces(
            zmax=3, zmin=0, opacity=0.9, xgap=0.1, showscale=False)
        fig2.update_layout(
            autosize=True, margin=dict(l=10, r=10, b=50, t=0, pad=0),
            height=100)
        return fig2

    @app.callback(
        dash.dependencies.Output(ids.HEATMAP, "figure"),
        [dash.dependencies.Input(ids.PARETO_3D, 'clickData'),
         dash.dependencies.Input(ids.DATA_TABLE, 'data'),
         dash.dependencies.Input(ids.DATA_TABLE, 'selected_rows')])
    def update_heatmap(selected_point, data, selected_rows):
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
        return create_heatmap(selected_row_index)

    return dcc.Graph(id=ids.HEATMAP)
