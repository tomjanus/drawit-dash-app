""" """
from typing import List, Dict
import plotly.express as px

OBJECTIVES: List[str] = [
    'annual HP', 'flood extent', 'no. crops', 'no. bare', 'diversity']

labels_parallel_plot = [
    "HP prod. [MWh]", "flooded area [ha]", "no. of crops [-]",
    "no. of bare soils [-]", "land cover diversity [-]"]

parallel_plot_vars = dict(zip(OBJECTIVES, labels_parallel_plot))

var_for_pie_chart = ['frac. forests', 'frac. grass', 'frac. crops',
                     'frac. bare']
piechart_color_map_var: Dict[str, str] = {
    'frac. crops': '#46BC85',
    'frac. bare': '#FAE739',
    'frac. forests': '#531763',
    'frac. grass': '#427498'}

# Dictionary between variables and labels used to translate values in pie_df
piechart_labels = ['Crops', 'Bare Soil', 'Mixed Forests', 'Grasslands']
labels_dict_pie_chart = dict(
    zip(piechart_color_map_var.keys(), piechart_labels))

piechart_color_map_label = dict(zip(
    piechart_labels,
    piechart_color_map_var.values()))

var_for_heatmap = ['tile 1', 'tile 2', 'tile 3', 'tile 4', 'tile 5',
                   'tile 6', 'tile 7', 'tile 8', 'tile 9', 'tile 10']

landuse_dict = dict(dict(zip(
    [0, 1, 2, 3],
    ['mixed forests', 'grasslands', 'croplands', 'bare soil'])))

colorscales = px.colors.named_colorscales()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
