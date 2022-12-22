"""Structure of the body of the page"""
from dash import html, Dash, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from . import ids
from . import (
    radio_items, parallel_plot, data_table, plot_3d, dropdowns, heatmap,
    pie_chart, download_button)

DOWNLOAD_BUTTON_TEXT = '''
If you wish to explore and analyse the land use optimization results presented
on this page with your own algorithms and methods, you can download the raw
data in CSV format by clicking on the button below.
'''

MAIN_OUTCOMES_TEXT = '''
- Spatial distribution of land cover along a hillslope and thus, in a watershed,
can strongly influence the performance of multisector water resources systems.
- Consequently, multi-sector (e.g. water-energy-food-ecosystems) ‘nexus’
design frameworks can benefit from spatially-distributed coupled land-hydrologic
models since catchments can exhibit complex non-intuitive behaviour in response
to land cover planning decisions.
- On the other hand, computer-assisted land use planning is likely to be less
effective if one uses conceptual models lacking the spatial hydrologic connections.
'''


def render(app: Dash, data: pd.DataFrame) -> dbc.Accordion:
    """ """
    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                html.P(
                    "Table of selected nondominated results",
                    className="card-text"),
                data_table.render(app, results=data),
            ]
        ),
        className="mt-3",
    )

    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                plot_3d.render(app, data),
                dbc.Tooltip(
                        "Visualisation of the pareto front. "
                        "Solutions filtered out in the parallel axis plot "
                        "are greyed out.",
                        target=ids.PARETO_3D,
                        placement="top",
                        autohide=True,
                        style={
                            "font-size": "10pt",
                            "font-family": "monospace",
                            "background-color": "rgba(0,0,0,0.6)"
                            }
                    )
            ]
        ),
        className="mt-3",
    )

    item = dbc.Accordion([
        dbc.AccordionItem([
            dbc.Row([
                dbc.Col([
                    radio_items.render(app),
                    parallel_plot.render(app, results=data),
                    dbc.Tooltip(
                            "Visualisation of objectives in the nondominated "
                            "solution set. Solutions can be filtered"
                            " by selecting value ranges on each axis.",
                            target=ids.PARALLEL_PLOT,
                            placement="top",
                            autohide=True,
                            style={
                                "font-size": "10pt",
                                "font-family": "monospace",
                                "background-color": "rgba(0,0,0,0.6)"
                                }
                        )], width=6),
                dbc.Col([
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                tab1_content, tab_id="table-tab",
                                label="Table"),
                            dbc.Tab(
                                tab2_content, tab_id="plot-tab",
                                label="3D Pareto Surface"),
                        ], active_tab='table-tab', id=ids.TABLE_3D_PLOT_TAB
                    ),
                ], style={'padding': 0}, width=6)
            ]),
            dbc.Row(dropdowns.render(app)),

            dbc.Row([
                dbc.Col([
                    html.H5(
                        children="Spatial distribution of land covers",
                        style={'textAlign': 'center'}),
                    heatmap.render(app, results=data)], width=7),
                dbc.Col([
                    html.H5(
                        children="Composition of land covers",
                        style={'textAlign': 'center'}),
                    pie_chart.render(app, results=data)
                ], width=5)
            ], style={'padding': '0px'})


            ],
                title="MULTIOBJECTIVE OPTIMIZATION RESULTS"),
        dbc.AccordionItem([
            dcc.Markdown(
                children=MAIN_OUTCOMES_TEXT,
                style={'text-align': 'justify'},
                mathjax=True),
            dbc.Row([
                dbc.Col("", width=6),
                dbc.Col([
                    html.P(DOWNLOAD_BUTTON_TEXT),
                    download_button.render(app, results=data)
                ], width=6, style={'margin-top': "10pt"})
            ])
        ], title="MAIN OUTCOMES")
    ], flush=False, start_collapsed=True)
    return item
