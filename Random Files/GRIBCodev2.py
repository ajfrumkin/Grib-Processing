# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load necessary libraries
import pygrib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import numpy as np
#import pandas as pd

#Read the GRIB File
grbs = pygrib.open('C:/Users/frumkina/Desktop/Python/snow_2018_era5land.grib')

#Create a list of the lat/lon pairs
grb = grbs.message(1)
data,lats,lons = grb.data()
print(grb)

np.savetxt("testing.csv",lons,delimiter =",")

# .shape returns a tuple with the number of grid points in the y and x directions. THe four variables below capture the length of the latitude and longitude grids in the y and x direction
lats_y_grid = lats.shape[0] # the number of latitude grid points in the y direction
lats_x_grid = lats.shape[1] # the number of latitude grid points in the x direction
lons_y_grid = lons.shape[0] # the number of longitude grid points in the y direction
lons_x_grid = lons.shape[1] # the number of longitude grid points in the x direction

Data_File = open("Coordinate_List.txt","w")
Data_File.write("Latitude" + "," + "Longitude" + "\n")
for y in range(0,lats_y_grid): #The range will start at 0 and go through one less than the number of grid points
    for x in range(0,lons_x_grid): #The range will start at 0 and go through one less than the number of grid points
        lat_float = lats.item((y,x))
        lon_float = lons.item((y,x))
        Data_File.write(str(round(lat_float,2)) + "," + str(round(lon_float,2)) + "\n")

Data_File.close()

# print(test[1])
# print(type(test[1]))
# test_tuple = (["apple","orange","cherry"],["dog","kitten","tiger"],["computer","phone","car"])
# print(test_tuple[1][1])

# grb = grbs.select(name='2 metre temperature')
# print(type(grbs))
# print(type(grb))
# print(grb[1])



# #Grabbing one particular value from aparticular timestep
# grb = grbs.message(1)
# print(grb.validDate) #this prints the message with the variable and timestamp
# data = grb.data()[0]
# print(data) #this prints the data can be 0-2 
# print(type(data)) #Prints the data type


# list = [("Date","Temperature")]
# for count in range(1,2161,1):
    
#     grb = grbs.message(count)
#     date_time = grb.validDate.strftime("%b %d %Y %H:%M:%S")
#     data, lats, lons = grb.data(lat1=45.25, lat2=45.25, lon1=7.5, lon2=7.5)
#     list.append((date_time,float(data-273.15)))



