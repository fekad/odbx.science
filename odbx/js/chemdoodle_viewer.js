var cifFile = document.getElementById("viewer").getAttribute("data-cif");
var canvas_x = document.getElementById("viewer").getAttribute("canvas-x");
var canvas_y = document.getElementById("viewer").getAttribute("canvas-y");
var canvas = new ChemDoodle.TransformCanvas3D('canvas', canvas_x, canvas_y);
var crystal = ChemDoodle.readCIF(cifFile);
canvas.specs.set3DRepresentation('Ball and Stick');
canvas.specs.backgroundColor = 'white';
canvas.specs.atoms_useJMOLColors = true;
canvas.specs.projectionPerspective_3D = false;
canvas.specs.projectionOrthoWidth_3D = 100;
canvas.specs.shadow_3D = true;
canvas.specs.bonds_renderAsLines_3D = false;
canvas.specs.bonds_cylinderDiameter_3D = 0.1;
canvas.specs.antialias_3D = true;
canvas.specs.atoms_materialShininess_3D = 1000;
canvas.specs.bonds_materialShininess_3D = 1000;
canvas.specs.flat_color_3D = false;
canvas.specs.outline_3D = false;
canvas.shapes_lineWidth = 2;
canvas.shapes_color = '#FF0000';
canvas.compass_display = true;
canvas.loadContent([crystal.molecule], [crystal.unitCell]);
