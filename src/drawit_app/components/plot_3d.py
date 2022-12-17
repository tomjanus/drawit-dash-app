""" """
from typing import List
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objects as go
from . import ids
from . import constants

labels_from_objectives = constants.parallel_plot_vars
objectives_from_labels = {
    value: label for label, value in labels_from_objectives.items()}


def render(app: dash.Dash, results: pd.DataFrame) -> dcc.Graph:
    """ """

    @app.callback(
        dash.dependencies.Output(ids.PARETO_3D, "figure"),
        dash.dependencies.Input(ids.X_AXIS_DROPDOWN_3D, "value"),
        dash.dependencies.Input(ids.Y_AXIS_DROPDOWN_3D, "value"),
        dash.dependencies.Input(ids.Z_AXIS_DROPDOWN_3D, "value"),
        dash.dependencies.Input(ids.COLOR_DROPDOWN_3D, "value"),
        dash.dependencies.Input(ids.DATA_TABLE, "derived_virtual_data"))
    def update_pareto_plot(
            x_label: str, y_label: str, z_label: str, color_dim: str,
            filtered_data: pd.DataFrame):
        """ """
        if not x_label:
            raise PreventUpdate

        if filtered_data is not None:
            filtered_indices = [item['index'] for item in filtered_data]
        else:
            filtered_indices = []

        results_incl = results.filter(items=filtered_indices, axis=0)
        results_excl = pd.merge(
            results, results_incl, indicator=True, how='outer').query(
                '_merge=="left_only"').drop('_merge', axis=1)

        # Prepare data for plotting the filtered results
        x_values = results_incl[x_label]
        y_values = results_incl[y_label]
        z_values = results_incl[z_label]
        color_values = results_incl[color_dim]

        # Prepare data for plotting the filtered out results
        x_values_excl = results_excl[x_label]
        y_values_excl = results_excl[y_label]
        z_values_excl = results_excl[z_label]

        # Update hover text
        hovertext: List[str] = []
        for _, row in results.iterrows():
            x_label_txt = labels_from_objectives[constants.OBJECTIVES[0]]
            x_value_txt = row[constants.OBJECTIVES[0]]
            y_label_txt = labels_from_objectives[constants.OBJECTIVES[1]]
            y_value_txt = row[constants.OBJECTIVES[1]]
            z_label_txt = labels_from_objectives[constants.OBJECTIVES[2]]
            z_value_txt = row[constants.OBJECTIVES[2]]
            color_label_txt = labels_from_objectives[constants.OBJECTIVES[3]]
            color_value_txt = row[constants.OBJECTIVES[3]]
            size_label_txt = labels_from_objectives[constants.OBJECTIVES[4]]
            size_value_txt = row[constants.OBJECTIVES[4]]
            text = f"""
            {x_label_txt}: {x_value_txt:.2f} <br>
            {y_label_txt}: {y_value_txt:.2f} <br>
            {z_label_txt}: {z_value_txt:.0f} <br>
            {color_label_txt}: {color_value_txt:.0f} <br>
            {size_label_txt}: {size_value_txt:.0f}
            """
            hovertext.append(text)

        fig = go.Figure()
        fig.add_trace(
            go.Scatter3d(
                x=x_values_excl,
                y=y_values_excl,
                z=z_values_excl,
                mode='markers',
                hoverinfo='skip',
                hovertext=hovertext,
                marker=dict(
                    size=4,
                    color='grey',
                    colorscale='Viridis',   # choose a colorscale
                    opacity=0.3),
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=x_values,
                y=y_values,
                z=z_values,
                mode='markers',
                hoverinfo="text",
                hovertext=hovertext,
                marker=dict(
                    size=4,
                    color=color_values,
                    colorscale='Viridis',   # choose a colorscale
                    opacity=0.8
                )
            )
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0.08)',
            plot_bgcolor='rgba(0,0,0,0.08)',
            coloraxis={"colorbar": {"x": -0.2, "len": 0.5, "y": 0.8}}, #I think this is for contours
            margin=dict(l=0, r=0, b=0, t=0),
            hovermode="x unified",
            showlegend=False,
            hoverlabel=dict(
                bgcolor='rgba(255,255,255,0.85)',
                font=dict(color='black'),
                font_size=12,
                font_family="Rockwell"
            ),
            scene=dict(
                xaxis=dict(
                     title=labels_from_objectives[x_label],
                     backgroundcolor="rgba(0, 0, 0, 0.02)",
                     gridcolor="white",
                     showbackground=True,
                     zerolinecolor="white",),
                yaxis=dict(
                    title=labels_from_objectives[y_label],
                    backgroundcolor="rgba(0, 0, 0, 0.02)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white"),
                zaxis=dict(
                    title=labels_from_objectives[z_label],
                    backgroundcolor="rgba(0, 0, 0, 0.02)",
                    gridcolor="white",
                    showbackground=True,
                    zerolinecolor="white",),),
            )
        return fig
    return dcc.Graph(id=ids.PARETO_3D)
