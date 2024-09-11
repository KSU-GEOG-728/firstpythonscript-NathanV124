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
acrpy.env.workspace= "C:/Users/ntverrill/Documents/GitHub/firstpythonscript-NathanV124/GitHub-FirstPythonScript.gdb"

selectRegion = arcpy.management.SelectLayerByAttribute("ks_ecoregions", "NEW_SELECTION","US_L3NAME = 'Flint Hills'")
createBuffer = arcpy.analysis.Buffer('ks_ecoregions', 'buffer_area', "10 kilometers" )
createClip = arcpy.analysis.Clip('ks_major_rivers', 'buffer_area', 'clipped_area')
arcpy.management.CalculateField('clipped_area', 'TotalLength', '!shape.length!')