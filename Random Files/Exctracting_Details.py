# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load necessary libraries
import pygrib
import numpy as np
import pandas as pd

#Read the GRIB File
grbs = pygrib.open('C:\Users\frumkina\Desktop\Python\Grib Files\2m_temperature_2018_SC_Area.grib')

##### The code below create a text file with the lat/lon pairs
grb = grbs.message(1)
lats,lons = grb.latlons()
print(grb)

#np.savetxt("testing.csv",lons,delimiter =",")

# .shape returns a tuple with the number of grid points in the y and x directions. THe four variables below capture the length of the latitude and longitude grids in the y and x direction
lats_y_grid = lats.shape[0] # the number of latitude grid points in the y direction
lats_x_grid = lats.shape[1] # the number of latitude grid points in the x direction
lons_y_grid = lons.shape[0] # the number of longitude grid points in the y direction
lons_x_grid = lons.shape[1] # the number of longitude grid points in the x direction

Data_File = open("C:\Users\frumkina\Desktop\Python\Grib Files\Cordinate Lists\2m_temperature_2018_SC_Area.txt","w")
Data_File.write("Latitude" + "," + "Longitude" + "\n")
for y in range(0,lats_y_grid): #The range will start at 0 and go through one less than the number of grid points
    for x in range(0,lons_x_grid): #The range will start at 0 and go through one less than the number of grid points
        lat_float = lats.item((y,x))
        lon_float = lons.item((y,x))
        Data_File.write(str(round(lat_float,2)) + "," + str(round(lon_float,2)) + "\n")

Data_File.close()
##### End of lat/lon text file creation code


#### Find the nearest latitude and longitude in index form for use in the data exctraction
#Grab 1 grib message from which to exctract the coordinates
grb = grbs.message(1)

#Save the latitude and longitude to numpy arrays
lats,lons = grb.latlons()
lats_list = lats[:,0]
lons_list = lons[0,:]

#Get the users desired coordinates
lat = 51.89
lon = -0.42

#Find the nearest gridpoint
nearest_lon = np.argmin((lons_list-lon)**2)
nearest_lat = np.argmin((lats_list-lat)**2)


#### End of the nearest point code



#### The code below finds out how many timesteps are in the selected grib file
grb = str(grbs.select(name='Snow depth')[-1])
print(type(grb))
last_step_list = grb.split(":")
last_value = int(last_step_list[0]) #saves the count to a useable variable
print(last_value)
#### End of the timestep counting code


#### The code below extracts the data for the given lat/lon pair. It uses "last_value" identified in the earlier pice of code.
Data_File = open("C:\Users\frumkina\Desktop\Python\Times Series Exctractions\2m_temperature_2018_SC_Area.txt","w")

for count in range(1,(last_value+1),1):
    print(count)
    grb = grbs.message(count)
    date_time = grb.validDate.strftime("%m/%d/%Y,%H:%M:%S,")
    data,lats,lons = grb.data()
    Data_File.write(date_time + str(round(float(data[nearest_lat,nearest_lon]*100),1)) + "\n")

Data_File.close()


