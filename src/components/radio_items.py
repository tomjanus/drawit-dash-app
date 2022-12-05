""" """
import dash
from dash import dcc, html
from . import ids


def render(app: dash.Dash) -> html.Div:
    """ """
    return html.Div([
        html.P("Colour by:"),
        dcc.RadioItems(
            id=ids.RADIO_ITEMS,
            options=[
                {'label': 'Hydropower', 'value': 'annual HP'},
                {'label': 'Flooded area', 'value': 'flood extent'},
                {'label': 'No. of crops', 'value': 'no. crops'},
                {'label': 'No. of bare soil', 'value': 'no. bare'},
                {'label': 'Land cover diversity', 'value': 'diversity'}
            ],
            value='annual HP',
            labelStyle={'display': 'inline-block'},
            className='six columns'
        )
    ], className="row")
