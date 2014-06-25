import arcpy
import pythonaddins

class ExtensionClass1(object):
    """Implementation for PrintToPDF_AddIn_addin.extension2 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True

    def openDocument(self):
        mxd = arcpy.mapping.MapDocument("CURRENT")
        if mxd.description == 'Print to PDF':
            arcpy.mapping.PrintMap(mxd, r"Adobe PDF", "PAGE_LAYOUT")





