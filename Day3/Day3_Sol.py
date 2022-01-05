import rhinoscriptsyntax as rs
import Rhino
import time
 
 
#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
## This is used to print the method names ###
for func in dir(gh):
    if not func.startswith('_'): print func
rs.EnableRedraw(True)


for i in range(1,13):
    #SetSliderValue("GUID",Number)
    ## Your code here
    gh.SetSliderValue("00b4b0b5-5b2f-4f78-9ed7-c54afaeb3a8f",i)
    gh.RunSolver("Day3.gh")
    
    
    time.sleep(1)

