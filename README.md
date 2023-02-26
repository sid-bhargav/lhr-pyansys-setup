# Longhorn Racing Combustion `pyansys` Setup

Longhorn Racing Combustion setup to use pyansys and SOLIDWORKS design tables to automate the simulation of multiple CFD set ups. 

# Process

## 1. Using `Named Selection Manager` to create named selections in SOLIDWORKS

We want to be able to create named selections without opening the Ansys Workbench GUI so that we can run simulations through `pyansys`. To do this, we need to do a few things.

First, we need to make sure that Ansys and SOLIDWORKs can work together and produce/read CAD part files that have been formatted using the Named Selection Manager tool through the Ansys add-in. To do this we need to set up the Ansys add-in suite in SOLIDWORKS.

In SOLIDWORKS go to, `Tools > Add-ins...` and make sure that `Ansys 2022 R2` is selected under `Other Add-ins`.

In Ansys go to, `Options` and then navigate to the `Geometry Import` page. Scroll down and make sure `Named Selection` is selected, and the filtering prefix is NS. 

Produce named selections in SOLIDWORKS by opening the Named Selection Manager from `Tools > Ansys 2022 R2 > Named Selection Manager`.

Press `F5` on the keyboard so that you can select the specific type of geometry you would like to name select, and once you have finished your desired selection press create and give your selection a name.

> Make sure the name of your named selection is formatted as, 'NS_[NameSelection].'

Ansys should now be able to import the geometry of a `.SLDPRT` file along with the Named Selections you had assigned to it. 

# `pyansys` Documentation

`pyansys` docs: https://docs.pyansys.com/

`pyfluent` docs: https://fluent.docs.pyansys.com/release/0.12/

`pyfluent-parametric` docs: https://parametric.fluent.docs.pyansys.com/release/0.6/