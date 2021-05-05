# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load necessary libraries
import pygrib
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Read the GRIB File
grbs = pygrib.open("C:/Users/frumkina/Desktop/Python/Grib Files/T2m_End_of_2019.grib")

# #Check the first few messages
# for grb in grbs:
#     print(grb)

#Print the grb keys
#print(grb.keys())

# print(grb.experimentVersionNumber)
# print(grb.validDate)
# latitudes = grb.distinctLatitudes
# print(latitudes)
# longitudes = grb.distinctLongitudes
# print(longitudes)
# print(grb.latLonValues)
# print(grb.totalLength)


# ##### The code below create a text file with the lat/lon pairs
# grb = grbs.message(1)
# lats,lons = grb.latlons()
# print(grb)

# Data_File = open('C:/Users/frumkina/Desktop/Python/Grib Files/Cordinate Lists/T2m_End_of_2019.txt',"w")
# Data_File.write("Latitude" + "," + "Longitude" + "\n")
# for y in latitudes: #The range will start at 0 and go through one less than the number of grid points
#     for x in longitudes: #The range will start at 0 and go through one less than the number of grid points
#         Data_File.write(str(round(y,2)) + "," + str(round(x,2)) + "\n")

# Data_File.close()
# ##### End of lat/lon text file creation code



# #### The code below finds out how many timesteps are in the selected grib file
# grb = str(grbs.select(name='2 metre temperature')[-1])
# print(type(grb))
# last_step_list = grb.split(":")
# last_value = int(last_step_list[0]) #saves the count to a useable variable
# print(last_value)
# #### End of the timestep counting code


# #### The code below extracts the data for the given lat/lon pair. It uses "last_value" identified in the earlier pice of code.
# Data_File = open("C:/Users/frumkina/Desktop/Python/Times Series Exctractions/2m_temperature_2018_SC_Area.txt","w")

# for count in range(1,(last_value+1),1):
#     print(count)
#     grb = grbs.message(count)
#     date_time = grb.validDate.strftime("%m/%d/%Y,%H:%M:%S,")
#     data,lats,lons = grb.data()
#     Data_File.write(date_time + str(round(float((data[nearest_lat,nearest_lon]-273.15) * (9/5) + 32),1)) + "\n")

# Data_File.close()



grb = grbs.message(2000)
lats,lons = grb.latlons()
t2m=(grb.values-273.15) * (9/5) + 32
print(t2m)
fig, ax = plt.subplots(figsize=(10,8))
m = Basemap(resolution='i', projection='lcc', llcrnrlon=232.6,llcrnrlat=21.9,urcrnrlon=303.5,urcrnrlat=54,lat_0=38.8,lon_0=262.7)
x,y = m(lons,lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
cs = m.contourf(x,y,t2m,np.linspace(70,90,40),cmap=plt.cm.jet)
cb = m.colorbar()
t = plt.title('2m Temperature @ ' + str(grb.validDate))
