# PYFLUENT SETUP BASED OFF OF EXAMPLE
# 2D EXAMPLE


import ansys.fluent.core as pyfluent

processor_thinkpad = 16
solver = pyfluent.launch_fluent(precision='double', processor_count=processor_thinkpad, mode='solver')


# validate ANSYS versions that may require different inputs
solver_check = solver.get_fluent_version() >= '23.1.0'
twentytwo_check = solver.get_fluent_version () == '22.2.0'


# check to make sure mesh elements are sound
solver.tui.mesh.check()


# set working units for mesh
solver.tui.define.units('length', 'mm')


# set up boundary conditions
solver.setup.boundary_conditions.velocity_inlet['inlet'].vmag = {} if solver_check else {}
solver.setup.boundary_conditions.pressure_outlet['outlet'].vmag = {} if solver_check else {}


# initialize with hybrid initialization
solver.solution.initialization.hybrid_initialize()


# run calculation
solver.solution.run_calculation.iterate(iter_count=300) if solver_check else solver.solution.run_calculation.iterate(number_of_iterations=300)


solver.exit()

