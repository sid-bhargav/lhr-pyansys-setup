# FLUENT

import os
import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

# decide whether code runs 2d or 3d setup.
setup = "2d"

# inputs for certain fields depending on solver version
if setup == "2d":
    settings = {"version": "2d", "iterations": 600}
else:
    settings = {"version": "3d", "iterations": 600}

# example mesh
import_filename = examples.download_file("mixing_elbow.msh.h5", "pyfluent/mixing_elbow")

# test mesh
test_dir = "src/test.msh"

# create 2d solver
solver = pyfluent.launch_fluent(
    version=settings["version"], precision="double", processor_count=2, mode="solver"
)

# verify that case file is sound
solver.file.read(file_type="case", file_name=test_dir)
solver.tui.mesh.check()

# set units to mm
solver.tui.define.units("length", "mm")

# disable heat transfer
solver.setup.models.energy.enabled = False

"""TODO: setup simulation"""

# ==================================================
#                Run Calculations
# ==================================================

# # initialize the flow field using hybrid initialization
# solver.solution.initialization.hybrid_initialize()

# # solve for 150 iterations
# solver.solution.run_calculation.iterate.get_attr("arguments")
# if solver.get_fluent_version() >= "23.1.0":
#     solver.solution.run_calculation.iterate(iter_count=settings["iterations"])
# else:
#     solver.solution.run_calculation.iterate(number_of_iterations=settings["iterations"])

solver.exit()
