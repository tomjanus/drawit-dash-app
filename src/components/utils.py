""" """
from typing import Dict, List
import pandas as pd
from . import constants


class ParallelPlotSelector:
    """ """
    def __init__(self, raw_data: pd.DataFrame):
        """ """
        self.raw_data = raw_data[constants.OBJECTIVES]
        self.selection: Dict[int, List[List[int]]] = {}
        self.dim_column_map = {
            v: k for k, v in constants.parallel_plot_vars.items()}
        self.filtered_data = self.raw_data

    def update_selection(self, col_label: str, limits) -> None:
        """ """
        self.selection[col_label] = limits

    def filter_data(self) -> None:
        """ """
        for col_index, limits_list in self.selection.items():
            filtered_data_loc = self.filtered_data.copy()
            counter: int = 0
            for l_limit, u_limit in limits_list:
                aux = self.filtered_data[
                    (self.filtered_data[
                        self.dim_column_map[col_index]] >= l_limit) &
                    (self.filtered_data[
                        self.dim_column_map[col_index]] <= u_limit)]
                if counter == 0:
                    filtered_data_loc = aux
                else:
                    filtered_data_loc = pd.concat([filtered_data_loc, aux])
                counter += 1
            self.filtered_data = filtered_data_loc
