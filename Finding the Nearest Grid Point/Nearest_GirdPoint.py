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
grbs = pygrib.open("C:/Users/frumkina/Desktop/Python/Grib Files/T2m_End_of_2019.grib")

#Select one message as they all have the same grid
grb = grbs.message(1)

latitudes = grb.distinctLatitudes
longitudes = grb.distinctLongitudes

#Get the users desired coordinates
lat = 32.9
lon = -80.0

#Convert lon to 0-360
if lon < 0:
    lon = 360+lon

#Find the nearest gridpoint using np.argmin
#This gives you the index number of the nearest point
nearest_lon = np.argmin((longitudes-lon)**2)
nearest_lon_Degrees = longitudes[nearest_lon]
nearest_lat = np.argmin((latitudes-lat)**2)
nearest_lat_Degrees = latitudes[nearest_lat]
