import arcpy
import pythonaddins
import os
import time

class ExtensionClass1(object):
    """Implementation for PrintToPDF_AddIn_addin.extension2 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True

##    def openDocument(self):
##        mxd = arcpy.mapping.MapDocument("CURRENT")
##        if mxd.description == 'Print to PDF':
##            arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")
##        pass    
##            mxd.activeView = "PAGE_LAYOUT" #Make sure Layout View is active
##            arcpy.RefreshActiveView() #Refresh the view
            

##            df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
##            addLayer = arcpy.mapping.Layer(r"D:\Users\Tools\MultiLayered_IAL_KML\IALs\IAL.lyr")
##            arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
            #for lyr in arcpy.mapping.ListLayers(mxd):
##            layers = arcpy.mapping.ListLayers(mxd, "", "Layers"):
##                print layers
##                time.sleep(1)
##            os.system('taskkill /IM Arcmap*')
        #arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")
            #os.system("pause")
            #os.system('taskkill /IM Arcmap*')#is killing it too soon
            #time.sleep(15)
##        pass

    def beforeCloseDocument(self):
        arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")
            
##    def beforeCloseDocument(self):
##        mxd = arcpy.mapping.MapDocument("CURRENT")
##        if mxd.description == 'Print to PDF':
##            for lyr in arcpy.mapping.ListLayers(mxd):
##                print lyr
##                time.sleep(1)
##            arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")
##        os.system('taskkill /IM Arcmap*')
##        pass



##    def itemAdded(new_item):
##        new_layer = r'D:\Users\Tools\MultiLayered_IAL_KML\IALs\IAL.lyr'
##        new_layer_name = 'Test Layer'
##        mxd = arcpy.mapping.MapDocument("CURRENT")
##        active_view = mxd.activeView
##        df = arcpy.mapping.ListDataFrames(mxd, active_view)[0]
##        if arcpy.mapping.ListLayers(mxd, new_layer_name) == []:
##            arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(new_layer))
##            arcpy.RefreshTOC()
##        else:
##            return   
##        arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")

##    def itemAdded(new_item):
##        mxd = arcpy.mapping.MapDocument("CURRENT")
##        if mxd.description == 'Print to PDF':
##            df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
##            addLayer = arcpy.mapping.Layer(r"D:\Users\Tools\MultiLayered_IAL_KML\IALs\IAL.lyr")
##            arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
##            arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")



##    def CloseDocument(self):
#os.system('taskkill /IM Arcmap*')




