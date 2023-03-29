import ansys.fluent.core as pyfluent

ansys = pyansys.run_ansys()


wb = workbench.open('FWNG2023_2.wbpj')


sc = SpaceClaim.getSpaceClaim()

geometries = []

named_selections = []

for geometry in geometries:
    sc.importFile(geometry)


sc.close()
mesh = wb.getMeshing()

mesh.setMeshingTechnique("Triangular")
mesh.setBoundaryLayer(True)


mesh.
mesh.run()
mesh.close()



fluent = wb.getFluent()



fluent.close()


