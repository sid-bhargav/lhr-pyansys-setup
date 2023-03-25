# DATA PROCESSOR FOR ALL INFO

import yplus as yp

print(yp.calc(5, 9))


class DataProcessor(object):
    def __init__(self, design_table, named_selections):
        self.dt = design_table
        self.ns = named_selections

    def preprocess(self):
        pass
