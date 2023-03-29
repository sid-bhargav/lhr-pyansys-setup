# data processor

import data_processor as dp
import mesh
import cfd
import post

processor = dp.DataProcessor(None, None)

# mesh

# run fluent simulation
mesh_directory = "src/test.msh"
cfd.solve(mesh_directory, setup="2d")
