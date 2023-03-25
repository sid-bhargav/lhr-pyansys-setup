# Longhorn Racing Combustion `pyansys` Setup

Longhorn Racing Combustion setup to use pyansys and SOLIDWORKS design tables to automate the simulation of multiple CFD set ups. The setup is currently in development and does not currently work.

## Process

### 1. Using `Named Selection Manager` To Create Named Selections in SOLIDWORKS

We want to be able to create named selections without opening the Ansys Workbench GUI so that we can run simulations through `pyansys`. To do this, we need to do a few things.

First, we need to make sure that Ansys and SOLIDWORKS can work together and produce/read CAD part files that have been formatted using the Named Selection Manager tool through the Ansys add-in.

In SOLIDWORKS go to, `Tools > Add-ins...` and make sure that `Ansys 2022 R2` is selected under `Other Add-ins`.

In Ansys Workbench go to `Tools > Options... > Geometry Import` and scroll down and make sure `Named Selection` is selected, and the filtering prefix is NS.

Produce named selections in SOLIDWORKS by opening the Named Selection Manager from `Tools > Ansys 2022 R2 > Named Selection Manager`.

Press `F5` on the keyboard so that you can select the specific type of geometry you would like to name select, and once you have finished your desired selection press create and give your selection a name.

> Make sure the name of your named selection is formatted as, 'NS\_\[nameSelection\].' Our program uses Camel Case.

Our naming convention:
| Selection | Our Nomenclature |
|---------------|------------------|
| Ground | NS_ground |
| Slip Wall | NS_slipWall |
| Inlet | NS_inlet |
| Outlet | NS_outlet |
| Wing 1 | NS_wing1 |
| Trailing Edge | NS_trailingEdge |

Ansys should now be able to import the geometry of a `.SLDPRT` file along with the Named Selections you had assigned to it.

### 2. Configuring Ansys to Mesh 2D `SLDPRT` files

In Ansys Workbench go to `Tools > Options... > Geometry Import` and in `Advanced Options` set `Analysis Type` to 2D.

> If you do not do this step, the meshing will not work. If you are getting an error about the mesh failing since the model is comprised of surface bodies and not solid bodies, you haven't set `Analysis Type` to 2D.

### 3. `data.in` Formatting

line 0: design table
line 1: named selections directory

## `pyansys` Documentation

`pyansys` docs: https://docs.pyansys.com/

`pyfluent` docs: https://fluent.docs.pyansys.com/release/0.12/

`pyfluent-parametric` docs: https://parametric.fluent.docs.pyansys.com/release/0.6/
