import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

from ansys.fluent.visualization import set_config
from ansys.fluent.visualization.matplotlib import Plots
from ansys.fluent.visualization.pyvista import Graphics

set_config(blocking=True, set_view_on_display="isometric")

# download files and launch fluent
import_case = examples.download_file(
  filename="exhaust_system.cas.h5", directory="pyfluent/exhaust_system"
)

import_data = examples.download_file(
  filename="exhaust_system.dat.h5", directory="pyfluent/exhaust_system"
)

solver_session = pyfluent.launch_fluent(
  precision="double", processor_count=2, start_transcript=False, mode="solver"
)

solver_session.tui.file.read_case(import_case)
solver_session.tui.file.read_data(import_data)

# create graphics object
graphics = Graphics(session=solver_session)

# graphics object for mesh display
mesh1 = graphics.Meshes["mesh-1"]

# edges
mesh1.show_edges = True

temperature_contour = graphics.Contours["contour-temperature"]
temperature_contour.field = "temperature"
temperature_contour.surfaces_list = ["mid-plane-x", "outlet-plane"]
temperature_contour.display("window-3")