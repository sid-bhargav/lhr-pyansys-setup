# DATA PROCESSOR FOR ALL INFO

import yplus as yp
import pandas as pd

print(yp.calc(5, 9))


class DataProcessor(object):
    def __init__(self, design_table, named_selections): # treat inputs as file paths (with \\ for paths)
        self.dt = pd.read_excel(design_table)
        self.ns = pd.read_excel(named_selections)

    def preprocess(self):
        pass
