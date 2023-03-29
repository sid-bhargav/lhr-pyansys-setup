# FLUENT

import os
import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

# decide whether code runs 2d or 3d setup.


def solve(mesh_dir, setup="2d"):
    # inputs for certain fields depending on solver version
    if setup == "2d":
        settings = {"version": "2d", "iterations": 600}
    else:
        settings = {"version": "3d", "iterations": 600}

    # ==================================================
    #                  Create Solver
    # ==================================================

    solver = pyfluent.launch_fluent(
        version=settings["version"],
        precision="double",
        processor_count=2,
        mode="solver",
    )

    # verify that case file is sound
    solver.file.read(file_type="case", file_name=mesh_dir)
    solver.tui.mesh.check()

    # set units to mm
    solver.tui.define.units("length", "mm")

    # disable heat transfer
    solver.setup.models.energy.enabled = False

    # ==================================================
    #               Simulation Settings
    # ==================================================

    """TODO: setup simulation"""

    # ==================================================
    #                 Run Simulation
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


def main():
    mesh_directory = "src/test.msh"

    solve(mesh_directory)


if __name__ == "__main__":
    main()
