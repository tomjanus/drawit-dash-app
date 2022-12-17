""" """
import dash
from dash import html
from dash import dash_table as dt
import pandas as pd
from . import ids
from . import constants


def render(app: dash.Dash, results: pd.DataFrame) -> html.Div:
    """ """
    if 'index' not in results.columns:
        results = results.reset_index()
    objectives_with_index = ['index']
    objectives_with_index.extend(constants.OBJECTIVES)
    return html.Div([
        dt.DataTable(
            columns=[{"name": i, "id": i} for i in
                     results[objectives_with_index].columns],
            data=results[objectives_with_index].round(2).to_dict('records'),
            sort_action='native',
            row_selectable='single',
            fixed_rows={'headers': False},
            page_current=0,
            page_size=11,
            id=ids.DATA_TABLE,
            page_action='native',
            selected_rows=[0],
            style_table={'height': '370px', 'overflowY': 'auto'},
            style_cell={'minWidth': 75, 'width': 95}
        ),
    ])
