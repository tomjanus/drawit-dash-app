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
from components.layout import create_layout
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from utils import load_outputs

local_data_path = os.path.join('data/', 'outputs_all_nondom.csv')
external_data_path = "https://raw.githubusercontent.com/tomjanus/drawit-dash-app/main/src/drawit_app/data/outputs_all_nondom.csv"
external_stylesheets = [
    dbc.themes.LUX,
    'https://codepen.io/chriddyp/pen/bWLwgP.css']
load_figure_template('LUX')

if os.path.exists(local_data_path):
    input_file_path = local_data_path
else:
    input_file_path = external_data_path

data = load_outputs(input_file_path)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
create_layout(app, data)

server = app.server
app.title = 'Multicriteria land cover design results'


if __name__ == '__main__':
    app.run_server(debug=True)
