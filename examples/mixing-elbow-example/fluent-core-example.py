#!/usr/bin/python3

# https://fluent.docs.pyansys.com/release/0.12/examples/00-fluent/mixing_elbow_settings_api.html#launch-fluent

import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

# import example object
import_filename = examples.download_file("mixing_elbow.msh.h5", "pyfluent/mixing_elbow")

# launch fluent
solver = pyfluent.launch_fluent(precision="double", processor_count=2, mode="solver")

# import mesh and perform mesh check
solver.file.read(file_type="case", file_name=import_filename)
solver.tui.mesh.check()

# set units to inches
solver.tui.define.units("length", "in")

# enable heat transfer
solver.setup.models.energy.enabled = True

# create material
if solver.get_fluent_version() == "22.2.0":
  solver.setup.materials.copy_database_material_by_name(
    type="fluid", name="water-liquid"
  )
else:
  solver.setup.materials.database.copy_by_name(type="fluid", name="water-liquid")

# cell zone conditions
solver.setup.cell_zone_conditions.fluid["elbow-fluid"].material = "water-liquid"

# boundry conditions

# cold inlet (cold-inlet), Setting: Value:
# Velocity Specification Method: Magnitude, Normal to Boundary
# Velocity Magnitude: 0.4 [m/s]
# Specification Method: Intensity and Hydraulic Diameter
# Turbulent Intensity: 5 [%]
# Hydraulic Diameter: 4 [inch]
# Temperature: 293.15 [K]

if solver.get_fluent_version() == "22.2.0":
  solver.setup.boundary_conditions.velocity_inlet["cold-inlet"].vmag = {
    "option": "constant or expression",
    "constant": 0.4,
  }
else:
  solver.setup.boundary_conditions.velocity_inlet["cold-inlet"].vmag = 0.4
solver.setup.boundary_conditions.velocity_inlet[
  "cold-inlet"
].ke_spec = "Intensity and Hydraulic Diameter"
solver.setup.boundary_conditions.velocity_inlet["cold-inlet"].turb_intensity = 0.05
solver.setup.boundary_conditions.velocity_inlet[
  "cold-inlet"
].turb_hydraulic_diam = "4 [in]"
if solver.get_fluent_version() == "22.2.0":
  solver.setup.boundary_conditions.velocity_inlet["cold-inlet"].t = {
    "option": "constant or expression",
    "constant": 293.15,
  }
else:
  solver.setup.boundary_conditions.velocity_inlet["cold-inlet"].t = 293.15

# hot inlet (hot-inlet), Setting: Value:
# Velocity Specification Method: Magnitude, Normal to Boundary
# Velocity Magnitude: 1.2 [m/s]
# Specification Method: Intensity and Hydraulic Diameter
# Turbulent Intensity: 5 [%]
# Hydraulic Diameter: 1 [inch]
# Temperature: 313.15 [K]

if solver.get_fluent_version() == "22.2.0":
  solver.setup.boundary_conditions.velocity_inlet["hot-inlet"].vmag = {
    "option": "constant or expression",
    "constant": 1.2,
  }
else:
  solver.setup.boundary_conditions.velocity_inlet["hot-inlet"].vmag = 1.2
solver.setup.boundary_conditions.velocity_inlet[
  "hot-inlet"
].ke_spec = "Intensity and Hydraulic Diameter"
solver.setup.boundary_conditions.velocity_inlet[
  "hot-inlet"
].turb_hydraulic_diam = "1 [in]"
if solver.get_fluent_version() == "22.2.0":
  solver.setup.boundary_conditions.velocity_inlet["hot-inlet"].t = {
    "option": "constant or expression",
    "constant": 313.15,
  }
else:
  solver.setup.boundary_conditions.velocity_inlet["hot-inlet"].t = 313.15

# pressure outlet (outlet), Setting: Value:
# Backflow Turbulent Intensity: 5 [%]
# Backflow Turbulent Viscosity Ratio: 4

solver.setup.boundary_conditions.pressure_outlet["outlet"].turb_viscosity_ratio = 4

solver.tui.solve.monitors.residual.plot("no")

# initialize flow field
solver.solution.initialization.hybrid_initialize()

# solve for 150 iterations
solver.solution.run_calculation.iterate.get_attr("arguments")
if solver.get_fluent_version() >= "23.1.0":
  solver.solution.run_calculation.iterate(iter_count=150)
else:
  solver.solution.run_calculation.iterate(number_of_iterations=150)

# create velocity vectors
solver.results.graphics.vector["velocity_vector_symmetry"] = {}
solver.results.graphics.vector["velocity_vector_symmetry"].print_state()
solver.results.graphics.vector["velocity_vector_symmetry"].field = "temperature"
solver.results.graphics.vector["velocity_vector_symmetry"].surfaces_list = [
  "symmetry-xyplane",
]
solver.results.graphics.vector["velocity_vector_symmetry"].scale.scale_f = 4
solver.results.graphics.vector["velocity_vector_symmetry"].style = "arrow"

# compute mass flow rate
solver.solution.report_definitions.flux["mass_flow_rate"] = {}
solver.solution.report_definitions.flux["mass_flow_rate"].zone_names.get_attr(
  "allowed-values"
)
solver.solution.report_definitions.flux["mass_flow_rate"].zone_names = [
  "cold-inlet",
  "hot-inlet",
  "outlet",
]
solver.solution.report_definitions.flux["mass_flow_rate"].print_state()
solver.solution.report_definitions.compute(report_defs=["mass_flow_rate"])

solver.exit()
