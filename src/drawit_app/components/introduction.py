""" """
import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from . import ids


SHORT_DESCRIPTION = '''
### **D**esigning **R**esilient and **A**daptable \
    **W**ater management - **I**ntegrated & Interactive **T**ools

This web-page can be used for interactive visual exploration of the key results
obtained from part of a research project entitled [**DRAW-IT:** **D**esigning
**R**esilient and **A**daptive **W**ater management: **I**ntegrated &
Interactive Tools]
(https://www.ukclimateresilience.org/projects/draw-it-designing-resilient-and-adaptable-water-management-integrated-interactive-tools/)

The study linked a mechanistic distributed **hydrologic model** of a hillslope
built in [Parflow](https://parflow.org/) with a **water resources management
model** created with [Pywr](https://github.com/pywr/pywr).
Parflow is integrated with a state-of-the art **land model**
[CLM](https://www.cesm.ucar.edu/models/clm/) which allows us to evaluate how
different types of land covers impact water and energy dynamics in a catchment.

The resulting integrated hydrologic, land and water resources model was embedded
in a many-objective **MultiObjective Evolutionary Algorithm (MOEA)** in order to
find land cover combinations that optimally balance food, energy, biodiversity
and flood resilience aspects of catchment management. This study implemented a
multiobjective genetic algorithm [NSGA-III]
(https://ieeexplore.ieee.org/document/6600851).

The study reveals patterns in the composition of land covers and their
spatial distributions in optimized solutions for different mixes of objectives.
These land cover patterns result from complex bi-directional spatially
distributed interactions between land and subsurface processes.

The study highlights the added benefit of considering subsurface-land
interactions in multi-sector water-food-energy-environment **NEXUS** studies - see
e.g [FAO](https://www.fao.org/land-water/water/watergovernance/waterfoodenergynexus/en/)
and [UN-Water](https://www.unwater.org/water-facts/water-food-and-energy).

This work has been described in detail in our manuscript currently undergoing
peer-review entitled:
*Multicriteria land cover design in multi-sector systems via coupled distributed
land and water management models* by:
Tomasz Janus, James Tomlinson, Daniela Anghileri, Justin Sheffield,
Stefan Kollet, and Julien Harou.
'''

SLOPE_DIAGRAM_TITLE = 'Typical groundwater table depth profile in \
    relation to surface elevation and root depth'
METHODOLOGY_DIAGRAM_TITLE = 'Multi-criteria optimised land use design framework'
COMBINED_MODEL_DIAGRAM_TITLE = 'Flow of information between Parflow/CLM, Pywr \
    and MOEA'

figure_title_map = {
    0: SLOPE_DIAGRAM_TITLE,
    1: METHODOLOGY_DIAGRAM_TITLE,
    2: COMBINED_MODEL_DIAGRAM_TITLE}

METHODOLOGY_DESCRIPTION = '''
The hydrologic model produces runoff as a response to atmospheric forcing and
as a function of hydrologic parameters and land use. This runoff becomes an
input to the water resources model. Decisions undertaken in the water resources
model such as e.g. water abstraction become boundary conditions in the
hydrologic model, creating a closed-loop coupling between both systems. The
selected outputs and state variables from both models are used to formulate
design criteria which become objective functions for the multi-objective
optimization algorithm **(MOEA)**.

Since the objectives are conflicting, improvement of one objective causes
deterioration of one or more other objectives. Therefore,
the optimizer looks not for a single optimal land use decision (solution) but
for the set of Pareto optimal solutions. A solution is said to be Pareto optimal
aka. *nondominated*, iff at least one of its objective functions is better than
the corresponding objective in all remaining points in the solution space. To
ascertain that the results are close to the true Pareto surface, i.e. a
global set of optimal solutions is found, optimisation procedure is normally
initialised from multiple starting points (seeds).

Those individual sets of
nondominated solutions are filtered to produce a list of optimal land use
decision portfolios.
'''

SLOPE_DIAGRAM_DESCRIPTION = '''
Mass and heat exchange processes on the surface that drive the watershed
hydrology are dependent on land use and on groundwater levels.
The schematic, borrowed from [11](https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2007WR006004)
explains why watershed hydrology is dependent on spatial configurations of land
uses and consequently, why distributed hydrologic and land use models might be
desired in model-based multi-criteria land-use design applications.

Three distinct zones are formed with respect to the proximity to groundwater.
These zones are characterised by different dominant processes.
In **Zone 1**, groundwater is shallow and neither transpiration nor evaporation
from soil are water-limited.
Access to water by some of the vegetation types such as crops or grass having
shorter root depths become water-limited in **Zone 2** whilst biological activity
of other vegetation types such as trees remains not water-limited.
Zone 2 is characterised with heavy coupling between land-energy fluxes
and groundwater level.
In **Zone 3**, groundwater is deep and thus disconnected from the land
surface. Consequently, transpiration and evaporation in Zone 3 are lower than in
Zone 1 and Zone 2. The variability of water table level in Zone 3 is lower than
in Zone 1 and Zone 2 since subsurface hydrology in Zone 3 is less dependent on
the processes happening on the surface level. Zone 3 also exhibits slower
response to groundwater recharge as a result of longer residence times in the
vadose zone.
'''

COMBINED_MODEL_DESCRIPTION = '''
The land cover design problem considers five competing objectives: $f_1(x)$ =
hydropower (HP) production in the hydroelectric reservoir (reservoir node),
$f_2(x)$ = flooded area in the river section passing through a hypothetical
settlement (city node), $f_3(x)$ = crop production,
$f_4(x)$ = solar power (SP) production, $f_5(x)$ = land cover diversity. The
decision variable $x$ is a $10$ x $1$ vector of land covers on the hillslope.
The boundary conditions on the hillslope are atmospheric forcings and base flow
$q_b$.

The mass balance in the hydroelectric reservoir in the water resource
model considers water sources: hillslope runoff flow $q_{in}$ and rainfall $q_r$
and water sink due to evaporation from the reservoir surface $q_e$. The flow
entering the turbine is denoted $q_{HP}$ while the spill flow bypassing the
turbine is denoted $q_s$. Water release to HP turbine is governed by a reservoir
water release curve that adjusts $q_{HP}$ as a function of reservoir volume.
The amount of hydroelectric energy is proportional to the product of $q_{HP}$
and the reservoir water level. The water level is computed from the reservoir
volume using the bathymetric level-volume relationship.
'''

figure_description_map = {
    0: SLOPE_DIAGRAM_DESCRIPTION,
    1: METHODOLOGY_DESCRIPTION,
    2: COMBINED_MODEL_DESCRIPTION}


def render(app: Dash) -> dbc.Row:
    """ """
    @app.callback(
        dash.dependencies.Output(ids.CARROUSEL_TITLES, "children"),
        dash.dependencies.Input(ids.CARROUSEL, "active_index"),)
    def update_title(carrousel_index) -> str:
        """ """
        if carrousel_index is None:
            carrousel_index = 0
        return figure_title_map[carrousel_index]

    @app.callback(
        dash.dependencies.Output(ids.CARROUSEL_DESCRIPTIONS, "children"),
        dash.dependencies.Input(ids.CARROUSEL, "active_index"),)
    def update_description(carrousel_index) -> str:
        """ """
        if carrousel_index is None:
            carrousel_index = 0
        return figure_description_map[carrousel_index]

    item = dbc.Accordion([
        dbc.AccordionItem([
            html.Div(
                dcc.Markdown(
                    children=SHORT_DESCRIPTION,
                    style={'text-align': 'justify'}),
            )],
            title="SHORT DESCRIPTION", style={"margin-bottom": "3pt"}),
        dbc.AccordionItem([
            html.H6(
                id=ids.CARROUSEL_TITLES,
                style={
                    "text-align": "center",
                    "margin-bottom": "10pt"}),
            dbc.Carousel(
                id=ids.CARROUSEL,
                items=[
                    {"key": "1",
                     "src": app.get_asset_url(
                            'img/slope_trees-800-450.png')},
                    {"key": "2",
                     "src": app.get_asset_url(
                        'img/methodology_diagram-800-450.png')},
                    {"key": "3",
                     "src": app.get_asset_url(
                        'img/combined_model-800-450.png')}],
                controls=True,
                indicators=True,
                variant="dark",
                style={"margin-left": "auto",
                       "margin-right": "auto",
                       "margin-top": "auto",
                       "margin-bottom": "auto",
                       "width": "60%"}
            ),
            dcc.Markdown(
                id=ids.CARROUSEL_DESCRIPTIONS,
                style={'text-align': 'justify'},
                mathjax=True)
            ], title="INTRODUCTION"),
    ], start_collapsed=False)
    return dbc.Row(item)
