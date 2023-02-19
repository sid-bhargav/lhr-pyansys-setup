// ==========================================================================================
// For purposes of applying to ANSYS meshing
// start: https://www.cfd-online.com/Forums/ansys-meshing/154552-script-model-mechanical.html
// ==========================================================================================

// NOTE: FOR 2D CFD WE CURRENTLY DON'T NAME THESE MANY SELECTIONS -_-
// we will have to name all of these before running script

// these all call functions defined via ANSYS already
// can you import in JavaScript???

function yPlus(chord) {
    return
    // can this even work???
}

var Env = DS.Tree.FirstActiveBranch.Environment;
DS.Script.SelectItems(""+Env.ID);

//meshGroup. = global values

DS.Script.doInsertMeshSize();
ListView.ActivateItem("Scoping Method");
ListView.ItemValue = "Named Selection";
ListView.ActivateItem("Named Selection");
ListView.ItemValue = "Refinement Large" // requires us to name each refinement zone
ListView.ActivateItem("Type");
ListView.ItemValue = "Element Size"
ListView.ActivateItem("Element Size")
ListView.ItemSize = "0.1"

DS.Script.doInsertInflation();
ListView.ActivateItem("Scoping Method")
ListView.ItemValue = "Named Selection";;
ListView.ActivateItem("Named Selection");
ListView.ItemValue = "wing"
ListView.ActivateItem*

ListView.ActivateItem("Named Selection");
ListView.ItemValue = "main"

