""" """
import dash
from dash import html, dcc
from dash.exceptions import PreventUpdate
from plotly import graph_objs as go
import pandas as pd
from . import ids
from . import constants


hovertemplate_single_heatmap = (
    '<i>Landuse type</i>: <b>%{text}</b>' +
    "<extra></extra>")


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """ """

    @app.callback(
        dash.dependencies.Output(ids.HEATMAP, "figure"),
        [dash.dependencies.Input(ids.PARETO_3D, 'clickData')])
    def update_heatmap(selected_point):
        if selected_point is None:
            selected_row_index = 0
        else:
            selected_row_index = selected_point['points'][0]['pointNumber']

        heatmap_df = results[constants.var_for_heatmap].iloc[[selected_row_index]]
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

    return html.Div([
        dcc.Graph(id=ids.HEATMAP)
    ], className="six columns")
