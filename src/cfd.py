# FLUENT

import os
import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples


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

    # ==================================================
    #               Simulation Settings
    # ==================================================

    # validate ANSYS versions that may require different inputs
    twentythree_check = solver.get_fluent_version() >= "23.1.0"
    twentytwo_check = solver.get_fluent_version() == "22.2.0"

    # setting boundry conditions

    # set units to mm
    solver.tui.define.units("length", "mm")

    # viscous model/disable heat transfer
    solver.setup.models.energy.enabled = False
    solver.setup.models.viscous.model = "k-omega-standard"

    # units: m/s
    solver.setup.boundary_conditions.velocity_inlet["ns_inlet"].vmag = (
        {"option": "constant or expression", "constant": 13} if twentytwo_check else 13
    )
    print("Intlet:")
    solver.setup.boundary_conditions.velocity_inlet["ns_inlet"].print_state()

    solver.setup.boundary_conditions.pressure_outlet[
        "ns_outlet"
    ].prevent_reverse_flow = True
    print("Outlet:")
    solver.setup.boundary_conditions.pressure_outlet["ns_outlet"].print_state()

    solver.setup.boundary_conditions.wall["ns_ground"].motion_bc = "Moving Wall"
    solver.setup.boundary_conditions.wall["ns_ground"].vmag = (
        {"option": "constant or expression", "constant": 13} if twentytwo_check else 13
    )  # m/s
    solver.setup.boundary_conditions.wall["ns_ground"].component_of_wall_translation[
        0
    ] = -1
    print("Ground:")
    solver.setup.boundary_conditions.wall["ns_ground"].print_state()

    solver.setup.boundary_conditions.wall["ns_slipwall"].shear_bc = "Specified Shear"
    print("Slip Wall:")
    solver.setup.boundary_conditions.wall["ns_slipwall"].print_state()

    wing_ns = "ns_wing"
    wings = []
    wing_num = 3

    for i in range(wing_num):
        wings.append(wing_ns + str(i + 1))

    print(wings)

    for wing in wings:
        solver.setup.boundary_conditions.wall[wing].shear_bc = "No Slip"
        # print(solver.setup.boundary_conditions.pressure_outlet['outlet'].prevent_reverse_flow)
        solver.setup.boundary_conditions.wall[wing].print_state()

    """TODO: setup simulation"""

    # ==================================================
    #                 Run Simulation
    # ==================================================

    # solver.tui.solve.monitors.residual.plot("no")

    # initialize the flow field using hybrid initialization
    """TODO MAKE IT INITIALIZE 15 PASSES"""
    solver.solution.initialization.hybrid_initialize()

    # solve for 150 iterations
    solver.solution.run_calculation.iterate.get_attr("arguments")
    if solver.get_fluent_version() >= "23.1.0":
        solver.solution.run_calculation.iterate(iter_count=settings["iterations"])
    else:
        solver.solution.run_calculation.iterate(
            number_of_iterations=settings["iterations"]
        )

    solver.exit()


def main():
    mesh_directory = "src/test.msh"
    solve(mesh_directory)


if __name__ == "__main__":
    main()
