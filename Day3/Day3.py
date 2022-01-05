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
    
    
    time.sleep(1)

