"""
DASH/Plotly application for interactive presentation of resultS from the
DRAW-IT project.

Presents results of multiobjective optimization of land cover with a combined
Parflow/CLM and Pywr models

Tomasz Janus
01 December 2022
"""
import os
import dash
from src.components.layout import create_layout
from src.data.loader import load_outputs


DATA_PATH = os.path.join('data/', 'outputs_all_nondom.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data = load_outputs(DATA_PATH)


app = dash.Dash(__name__) # , external_stylesheets=external_stylesheets
server = app.server
app.title = 'Multicriteria land cover design results'


if __name__ == '__main__':
    create_layout(app, data)
    app.run_server(debug=False, host='0.0.0.0', port=8050)
