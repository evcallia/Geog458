#Server URL
#http://qilin.geog.uw.edu:6080/arcgis/rest/services/evcallia/ReclassVectorCallia5/GPServer

import arcpy

#mytable = a valid shape file
#infield = what is to be reclassified
#outfield = name for which to create and store the reclassified value
#reclasstable = table specifying how to reclassify (lowerbound, upperbound, value)
#notfoundvalue = value to be set to if there is no row found within bounds

#grab parameters
mytable = arcpy.GetParameterAsText(0)
infield = arcpy.GetParameterAsText(1)
outfield = arcpy.GetParameterAsText(2)
reclasstable = arcpy.GetParameterAsText(3)
notfoundvalue = arcpy.GetParameterAsText(4)
output_table = arcpy.GetParameterAsText(5)

#make output file
arcpy.CopyFeatures_management (mytable, output_table)

#make new field
arcpy.AddField_management(output_table, outfield, "DOUBLE")
    
#go though mytable to find first row with infield that in within bounds specified
#cursor represents the table to be reclassified
with arcpy.da.UpdateCursor(output_table, [infield, outfield]) as cursor:
    for row in cursor:
            
        #keeps track of wheather the value was updated
        updated = False
            
        #cursorbound represents the cursor that will check if the 
        #found value is within bounds
        bounds = ["lowerbound", "upperbound", "value"]
        with arcpy.da.SearchCursor(reclasstable, bounds) as cursorbound:
            for rowbound in cursorbound:
                    
                #check if it's in bounds and if it is set value of new field
                #to the new value
                if row[0] >= rowbound[0] and row[0] <= rowbound[1]:
                    row[1] = rowbound[2]
                    cursor.updateRow(row)
                    updated = True
                    
        #if the filed to reclassify is not within any of the bounds, set to 
        #the value specified by user (notfoundvalue)            
        if updated == False:
            row[1] = notfoundvalue
            cursor.updateRow(row)
            




