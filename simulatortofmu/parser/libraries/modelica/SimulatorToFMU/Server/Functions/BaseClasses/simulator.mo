within SimulatorToFMU.Server.Functions.BaseClasses;
function simulator "Function that communicates with the SimulatorToFMU Python API"
  input ServerObject obj "Memory that holds the Python object";
  input Real    modTim "Model time";
  input Real    dblInpVal[max(1, nDblInp)] "Input variables values to be sent to SimulatorToFMU";
  input String  dblOutNam[max(1, nDblOut)] "Output variables names to be read from SimulatorToFMU";
  input String  dblInpNam[max(1, nDblInp)] "Input variables names to be sent to SimulatorToFMU";
  input Integer nDblInp(min=0) "Number of double inputs to send to SimulatorToFMU";
  input Integer nDblOut(min=0) "Number of double outputs to read from SimulatorToFMU";
  input Boolean resWri  "Flag for enabling results writing. true: write results, false: else";
  output Real   dblOutVal[max(1, nDblOut)] "Double output values read from SimulatorToFMU";
  external "C" modelicaToSimulator( modTim,
                                    nDblInp,
                                    dblInpNam,
                                    dblInpVal,
                                    nDblOut,
                                    dblOutNam,
                                    dblOutVal,
                                    resWri,
                                    obj)
    annotation (Library={"curl", "simulatortofmuserver"},
      LibraryDirectory="modelica://SimulatorToFMU/Resources/Library",
      IncludeDirectory="modelica://SimulatorToFMU/Resources/C-Sources",
      Include="#include \"serverWrapper.c\"");
  annotation (Documentation(info="<html>
<p>
This function.simulators data with a Simulator through its Python API.
See
<a href=\"modelica://SimulatorToFMU.Python27.UsersGuide\">
SimulatorToFMU.Python27.UsersGuide</a>
for instructions, and
<a href=\"modelica://SimulatorToFMU.Python27.Functions.Examples\">
SimulatorToFMU.Python27.Functions.Examples</a>
for examples.
</p>
</html>", revisions="<html>
<ul>
<li>
October 17, 2016, by Thierry S. Nouidui:<br/>
First implementation.
</li>
</ul>
</html>"));
end simulator;
