""" """
import dash
from dash import html, dcc
import pandas as pd
from . import ids


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """Render a download button for downloading the results dataframe."""

    @app.callback(
        dash.dependencies.Output(ids.DOWNLOADER, "data"),
        dash.dependencies.Input(ids.DOWNLAOAD_BUTTON, "n_clicks"),
        prevent_initial_call=True,
    )
    def download_results(n_clicks):
        return dcc.send_data_frame(
            results.to_csv, "drawit_optim_results.csv")

    return html.Div(
        [
            html.Button("Download DATA", id=ids.DOWNLAOAD_BUTTON),
            dcc.Download(id=ids.DOWNLOADER),
        ], className="two columns", style={'padding': '25px'}
    )
