# PYFLUENT SETUP BASED OFF OF EXAMPLE
# 2D EXAMPLE

import os
import ansys.fluent.core as pyfluent
from pprint import pprint

processor_thinkpad = 16
solver = pyfluent.launch_fluent(precision='double', processor_count=processor_thinkpad, mode='solver')

solver.setup.models.viscous.is_active()
solver.setup.models.viscous.model.is_read_only()

mesh_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'references/FFF-83/MECH/FFF-83.1.msh'))

# validate ANSYS versions that may require different inputs
twentythree_check = solver.get_fluent_version() >= '23.1.0'
twentytwo_check = solver.get_fluent_version () == '22.2.0'

# check to make sure mesh elements are sound
solver.file.read(file_type="case", file_name=mesh_filename)
solver.tui.mesh.check()

tui = solver.tui

# viscous model
solver.setup.models.energy = {'enabled' : False}
solver.setup.models.viscous.model = 'k-omega-standard'
# pprint(solver.setup.models.print_state())

# set working units for mesh
tui.define.units('length', 'mm')

tui.define.boundary_conditions.list_zones()

# set up boundary conditions
solver.setup.boundary_conditions.velocity_inlet['inlet'].vmag = {"option": "constant or expression", "constant": 13} if twentytwo_check else 13 # m/s
solver.setup.boundary_conditions.velocity_inlet['inlet'].print_state()

solver.setup.boundary_conditions.pressure_outlet['outlet'].prevent_reverse_flow = True
solver.setup.boundary_conditions.pressure_outlet['outlet'].print_state()

solver.setup.boundary_conditions.wall['ground'].motion_bc = "Moving Wall"
solver.setup.boundary_conditions.wall['ground'].vmag = {"option": "constant or expression", "constant": 13} if twentytwo_check else 13 # m/s
solver.setup.boundary_conditions.wall['ground'].component_of_wall_translation = -1
#solver.setup.boundary_conditions.wall['ground'].print_state()

solver.setup.boundary_conditions.wall['slip_wall'].shear_bc = "Specified Shear"
solver.setup.boundary_conditions.wall['slip_wall'].print_state()

solver.setup.boundary_conditions.wall['wing'].shear_bc = "No Slip"
#pprint(solver.setup.boundary_conditions.pressure_outlet['outlet'].prevent_reverse_flow)



solver.tui.solve.monitors.residual.plot("no")

# initialize with hybrid initialization
solver.solution.initialization.hybrid_initialize()


# run calculation
solver.solution.run_calculation.iterate(iter_count=300) if twentythree_check else solver.solution.run_calculation.iterate(number_of_iterations=300)

solver.exit()

