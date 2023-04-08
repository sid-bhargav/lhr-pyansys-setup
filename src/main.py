
import json

import data_processor as dp

# PREPROCESSING
# IMPLEMENTATION 1: JSON FILE
def preprocessing(filename):

    with open(filename, 'r') as paths_json:
        paths = json.load(paths_json)
    
    processor = dp.DataProcessor(paths["design_table"], paths["named_selections"])


# mesh

# cfd


if __name__ == '__main__':
    preprocessing('paths.json')
    pass