# can call as an external function (import)
import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples
import os

from ansys.fluent.visualization import set_config
from ansys.fluent.visualization.matplotlib import Plots
from ansys.fluent.visualization.pyvista import Graphics

#def visualization_mesh(filepath, surfaces_list):
set_config(blocking=True, set_view_on_display="isometric")

# download files and launch fluent
import_case = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'references/FFF-120/Fluent/FFF-120.1-1.cas.h5'))
import_data = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'references/FFF-120/Fluent/FFF-120.1-1-00132.dat.h5'))

solver_session = pyfluent.launch_fluent(
  precision="double", processor_count=16, start_transcript=False, mode="solver"
)

solver_session.tui.file.read_case(import_case)
solver_session.tui.file.read_data(import_data)

# create graphics object
graphics = Graphics(session=solver_session)

# graphics object for mesh display
mesh1 = graphics.Meshes["mesh-1"]
velocity_contour = graphics.Meshes["velocity-contour"]

# edges
mesh1.show_edges = True

# surfaces list
mesh1.surfaces_list = [
    'gurney', 
    'plane-20', 
    'plane-21', 
    'plane-22', 
    'plane-36', 
    'plane-37', 
    'plane-38', 
    'plane-39', 
    'inlet', 
    'outlet', 
    'symmetry', 
    'slipwall', 
    'ground', 
    'main', 
    'endplate_large', 
    'endplate_small', 
    'wheel', 
    'contactpatch', 
    'wing2'
]
mesh1.display("window-1")

surf_vel_contour = graphics.Surfaces["xy-plane"]
surf_vel_contour.definition.type = "iso-surface"
iso_surf3 = surf_vel_contour.definition.iso_surface
iso_surf3.field = "velocity-magnitude"
iso_surf3.rendering = "contour"
iso_surf3.iso_value = 0.0
surf_vel_contour.display("window-2")


