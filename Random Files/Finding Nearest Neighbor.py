# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:36:50 2019

@author: frumkina
"""

#Import Necessary modules
import pygrib
import numpy as np

#open the grib file
grbs = pygrib.open('C:/Users/frumkina/Desktop/Python/snow_2018_era5land.grib')

#Grab 1 grib message from which to exctract the coordinates
grb = grbs.message(1)

#Save the latitude and longitude to numpy arrays
lats,lons = grb.latlons()
lats_list = lats[:,0]
lons_list = lons[0,:]

#Get the users desired coordinates
lat = 51.89
lon = -0.42

nearest_lon = np.argmin((lons_list-lon)**2)
#nearest_lon = nearest_lon[0]
nearest_lat = np.argmin((lats_list-lat)**2)
#nearest_lat = nearest_lat[0]
