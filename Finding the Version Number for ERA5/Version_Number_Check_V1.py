# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:52:10 2020

@author: frumkina
"""

#Load necessary libraries
import pygrib
import numpy as np
import pandas as pd

#Read the GRIB File
grbs = pygrib.open("C:/Users/frumkina/Desktop/Python/Grib Files/T2M_Jan14thDownload.grib")

Data_File = open('C:/Users/frumkina/Desktop/Python/Grib Processing Scripts/Finding the Version Number for ERA5/Version Exctraction/Jan14thExctraction.txt',"w")

for grb in grbs:
    print(grb.validDate, ", ", grb.experimentVersionNumber)
    Data_File.write(str(grb.validDate) + ", " + str(grb.experimentVersionNumber) + "\n")
    
Data_File.close()