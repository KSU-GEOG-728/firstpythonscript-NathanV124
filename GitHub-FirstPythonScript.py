#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Nathan Verrill
    Description:  This script calculates the total stream miles for all streams in the Flint Hills.
    Date created: 09/11/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace= "C:/Users/ntverrill/Documents/GitHub/firstpythonscript-NathanV124/GitHub-FirstPythonScript/GitHub-FirstPythonScript.gdb"

#this selects the region we want to work with. This case it's the Flint hills.
selectRegion = arcpy.management.SelectLayerByAttribute("ks_ecoregions", "NEW_SELECTION","US_L3NAME = 'Flint Hills'")

#Creates a buffer around the selected region
createBuffer = arcpy.analysis.Buffer(selectRegion, 'buffer_area', "10 kilometers" )

#Clips the buffer around the region into it's own layer
createClip = arcpy.analysis.Clip('ks_major_rivers', 'buffer_area', 'clipped_area')

#creates a variable equal to 0
total_length_meters = 0

#Iterates through the cursor and creates a sum of all of the rows together. 
with arcpy.da.SearchCursor('clipped_area', ['shape@LENGTH']) as cursor:

#loops for each row    
    for row in cursor:
        total_length_meters += row[0]

#Converts meters to miles 
total_length_miles =  total_length_meters / 1609.34

#prints total number of miles
print(f"Total miles: {total_length_miles}")
