# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:43:08 2020

@author: frumkina
"""

import pygrib
import numpy as np
import pandas as pd

#Read the GRIB File
grbs = pygrib.open("C:/Users/frumkina/Desktop/Python/Grib Files/2mTemps_ERA5_2019_DEC.grib")

#Select one grib message. They all have the same grid
grb = grbs.message(1)

#Get a numpy array of the latitudes and longitudes
latitudes = grb.distinctLatitudes
longitudes = grb.distinctLongitudes

#Open the file you are writing to and give it a unique name
Data_File = open('C:/Users/frumkina/Desktop/Python/Grib Files/Cordinate Lists/TESTING.txt',"w")

#Write the header
Data_File.write("Latitude" + "," + "Longitude" + "\n")

#Loop through all of the latitude and longitude pairs and write them to a comma seperated file
for y in latitudes: #The range will start at 0 and go through one less than the number of grid points
    for x in longitudes: #The range will start at 0 and go through one less than the number of grid points
        Data_File.write(str(round(y,2)) + "," + str(round(x,2)) + "\n")

#CLose the file
Data_File.close()